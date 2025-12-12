"""
TASK 2: Semantic Caching System with Redis and Ollama

This module implements a semantic caching system that:
1. Stores Ollama LLM responses in Redis using vector embeddings
2. Uses Redis vector index for similarity search
3. Generates embeddings using SentenceTransformers
4. Searches for semantically similar queries using cosine similarity
5. Returns cached responses when similarity > threshold (0.85)
6. Calls Ollama for new queries and caches the result
7. Tracks cache hits/misses and measures performance

Concepts Covered:
- Semantic Caching: Cache based on meaning, not exact text match
- Vector Embeddings: Numerical representations of text meaning
- Cosine Similarity: Measure of similarity between vectors
- Redis Vector Search: Fast similarity search in Redis
- Write-Through Cache Pattern: Store results immediately after generation
"""

import redis
import json
import time
import numpy as np
from typing import Dict, Optional, Tuple, List
from sentence_transformers import SentenceTransformer
import requests
import hashlib


class SemanticCache:
    """
    Semantic caching system using Redis vector search and Ollama LLM.
    
    Architecture:
    1. Query comes in → Generate embedding
    2. Search Redis for similar embeddings (cosine similarity)
    3. If similarity > threshold → Return cached response (CACHE HIT)
    4. If similarity < threshold → Call Ollama → Store in Redis (CACHE MISS)
    """
    
    def __init__(
        self,
        redis_host: str = "localhost",
        redis_port: int = 6379,
        ollama_url: str = "http://localhost:11434",
        ollama_model: str = "llama3.2",
        similarity_threshold: float = 0.85,
        embedding_model: str = "all-MiniLM-L6-v2"
    ):
        """
        Initialize semantic cache system.
        
        Args:
            redis_host: Redis server hostname
            redis_port: Redis server port
            ollama_url: Ollama API endpoint
            ollama_model: Ollama model to use (e.g., llama3.2, mistral)
            similarity_threshold: Minimum similarity score (0-1) for cache hit
            embedding_model: SentenceTransformer model name for embeddings
        """
        # Connect to Redis
        self.redis_client = redis.Redis(
            host=redis_host,
            port=redis_port,
            decode_responses=False  # Keep binary for vector operations
        )
        
        try:
            self.redis_client.ping()
            print("✓ Connected to Redis successfully")
        except redis.ConnectionError:
            print("✗ Failed to connect to Redis. Make sure Redis is running!")
            raise
        
        # Initialize embedding model
        # SentenceTransformers converts text to numerical vectors (embeddings)
        # These vectors capture semantic meaning - similar texts have similar vectors
        print(f"Loading embedding model: {embedding_model}...")
        self.embedding_model = SentenceTransformer(embedding_model)
        
        # Get embedding dimension (typically 384 for all-MiniLM-L6-v2)
        # This tells us the size of vectors we'll store
        self.embedding_dim = self.embedding_model.get_sentence_embedding_dimension()
        print(f"✓ Embedding dimension: {self.embedding_dim}")
        
        # Configuration
        self.ollama_url = ollama_url
        self.ollama_model = ollama_model
        self.similarity_threshold = similarity_threshold
        
        # Create Redis index for vector search (if it doesn't exist)
        self._setup_redis_index()
        
        # Statistics tracking
        self.stats = {
            "total_queries": 0,
            "cache_hits": 0,
            "cache_misses": 0,
            "total_cache_time": 0.0,
            "total_ollama_time": 0.0
        }
    
    def _setup_redis_index(self):
        """
        Create Redis vector index for similarity search.
        
        Concept: Redis Index
        - Redis can create indexes on hash fields
        - Vector indexes enable fast similarity search using KNN (K-Nearest Neighbors)
        - We use HNSW (Hierarchical Navigable Small World) algorithm for efficient search
        """
        index_name = "semantic_cache_idx"
        
        try:
            # Check if index already exists
            existing_indexes = self.redis_client.execute_command("FT._LIST")
            if index_name.encode() in existing_indexes:
                print(f"✓ Vector index '{index_name}' already exists")
                return
        except:
            pass  # If command fails, index doesn't exist
        
        try:
            # Create index with vector field
            # FT.CREATE creates a search index
            # SCHEMA defines the fields we can search on
            # VECTOR field stores embeddings with HNSW algorithm
            index_command = [
                "FT.CREATE", index_name,
                "ON", "HASH",
                "PREFIX", "1", "cache:query:",
                "SCHEMA",
                "query", "TEXT",           # Store the original query text
                "response", "TEXT",        # Store the LLM response
                "embedding", "VECTOR",     # Vector field for similarity search
                    "HNSW",                # Algorithm: Hierarchical Navigable Small World
                    "6",                   # M: number of connections per layer
                    "10",                  # EF_CONSTRUCTION: size of candidate list during construction
                    "TYPE", "FLOAT32",     # Vector element type
                    "DIM", str(self.embedding_dim),  # Dimension of vectors
                    "DISTANCE_METRIC", "COSINE"  # Use cosine similarity
            ]
            
            self.redis_client.execute_command(*index_command)
            print(f"✓ Created Redis vector index '{index_name}'")
        except Exception as e:
            print(f"⚠ Warning: Could not create index (may already exist or RedisSearch not installed): {e}")
            print("  Continuing with fallback search method...")
    
    def _generate_embedding(self, text: str) -> np.ndarray:
        """
        Generate vector embedding for text using SentenceTransformers.
        
        Concept: Vector Embeddings
        - Converts text into a fixed-size numerical vector (e.g., 384 numbers)
        - Similar texts produce similar vectors (close in vector space)
        - Enables semantic matching - "cat" and "feline" will be similar
        
        Args:
            text: Input text to embed
            
        Returns:
            numpy array representing the text embedding
        """
        # Encode text to embedding vector
        # This is a dense representation capturing semantic meaning
        embedding = self.embedding_model.encode(text, convert_to_numpy=True)
        return embedding.astype(np.float32)
    
    def _search_similar_queries(self, query_embedding: np.ndarray) -> Optional[Tuple[str, float]]:
        """
        Search Redis for semantically similar queries using vector similarity.
        
        Concept: Vector Similarity Search
        - Compare query embedding with all cached query embeddings
        - Use cosine similarity to measure how similar they are
        - Cosine similarity ranges from -1 (opposite) to 1 (identical)
        - Values close to 1 mean semantically similar
        
        Args:
            query_embedding: Embedding vector of the current query
            
        Returns:
            Tuple of (cached_response, similarity_score) if match found, else None
        """
        index_name = "semantic_cache_idx"
        
        try:
            # Perform vector similarity search using Redis KNN
            # KNN = K-Nearest Neighbors - finds K most similar vectors
            # We want the top 1 most similar query
            search_command = [
                "FT.SEARCH", index_name,
                "*=>[KNN 1 @embedding $vec]",  # KNN query syntax
                "PARAMS", "2", "vec", query_embedding.tobytes(),  # Pass embedding as parameter
                "RETURN", "2", "query", "response",  # Return query text and response
                "SORTBY", "__embedding_score"  # Sort by similarity score
            ]
            
            result = self.redis_client.execute_command(*search_command)
            
            if result and len(result) >= 3:
                # Result format: [count, doc_id, [field, value, field, value, ...]]
                # Extract similarity score and response
                doc_id = result[1]
                fields = result[2]
                
                # Parse fields (alternating keys and values)
                field_dict = {}
                for i in range(0, len(fields), 2):
                    key = fields[i].decode() if isinstance(fields[i], bytes) else fields[i]
                    value = fields[i+1].decode() if isinstance(fields[i+1], bytes) else fields[i+1]
                    field_dict[key] = value
                
                # Get similarity score from metadata
                # Redis returns 1 - distance, so we need to convert
                # For cosine distance: similarity = 1 - distance
                # But Redis may return it differently, so we check the score
                score_key = b"__embedding_score"
                similarity = 0.0
                
                # Extract cached query and response
                cached_query = field_dict.get("query", "")
                cached_response = field_dict.get("response", "")
                
                # Get the cached embedding to calculate actual cosine similarity
                # RedisSearch returns distance, but we want similarity (1 - distance)
                # For cosine distance: similarity = 1 - distance
                # But for accuracy, we'll recalculate similarity
                doc_id_str = doc_id.decode() if isinstance(doc_id, bytes) else str(doc_id)
                cached_embedding_bytes = self.redis_client.hget(f"cache:query:{doc_id_str}", "embedding")
                
                if cached_embedding_bytes:
                    cached_embedding = np.frombuffer(cached_embedding_bytes, dtype=np.float32)
                    similarity = self._cosine_similarity(query_embedding, cached_embedding)
                    
                    if similarity >= self.similarity_threshold:
                        return (cached_response, similarity)
            
            return None
            
        except Exception as e:
            # Fallback: Manual search if RedisSearch not available
            print(f"  ⚠ Vector search failed: {e}")
            return self._fallback_search(query_embedding)
    
    def _fallback_search(self, query_embedding: np.ndarray) -> Optional[Tuple[str, float]]:
        """
        Fallback search method when RedisSearch is not available.
        Scans all cached queries and computes similarity manually.
        
        This method works without RedisSearch but is slower for large caches.
        For production, RedisSearch/RediSearch with vector indexes is recommended.
        """
        best_match = None
        best_similarity = 0.0
        
        # Scan all cache keys matching our pattern
        # scan_iter is memory-efficient (doesn't load all keys at once)
        for key in self.redis_client.scan_iter(match="cache:query:*"):
            try:
                # Get cached data from Redis hash
                cached_data = self.redis_client.hgetall(key)
                
                # Check if this entry has both embedding and response
                if b"embedding" in cached_data and b"response" in cached_data:
                    # Convert bytes back to numpy array
                    cached_embedding = np.frombuffer(cached_data[b"embedding"], dtype=np.float32)
                    
                    # Calculate cosine similarity
                    similarity = self._cosine_similarity(query_embedding, cached_embedding)
                    
                    # Track best match above threshold
                    if similarity > best_similarity and similarity >= self.similarity_threshold:
                        best_similarity = similarity
                        best_match = cached_data[b"response"].decode()
            except Exception as e:
                # Skip corrupted entries
                continue
        
        if best_match:
            return (best_match, best_similarity)
        return None
    
    def _cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """
        Calculate cosine similarity between two vectors.
        
        Concept: Cosine Similarity
        - Measures the angle between two vectors, not their magnitude
        - Range: -1 (opposite) to 1 (identical)
        - Formula: cos(θ) = (A · B) / (||A|| * ||B||)
        - Perfect for text embeddings since it focuses on direction (meaning)
        
        Args:
            vec1: First embedding vector
            vec2: Second embedding vector
            
        Returns:
            Cosine similarity score between 0 and 1
        """
        # Dot product of vectors
        dot_product = np.dot(vec1, vec2)
        
        # Magnitude (norm) of each vector
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        
        # Avoid division by zero
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        # Cosine similarity
        similarity = dot_product / (norm1 * norm2)
        
        # Ensure result is between 0 and 1 (for normalized embeddings, should already be)
        return max(0.0, min(1.0, similarity))
    
    def _call_ollama(self, query: str) -> str:
        """
        Call Ollama LLM API to generate response.
        
        Concept: LLM API Integration
        - Ollama runs LLMs locally
        - API endpoint: POST /api/generate
        - Returns streaming response (we collect all tokens)
        
        Args:
            query: User query/question
            
        Returns:
            LLM generated response
        """
        url = f"{self.ollama_url}/api/generate"
        
        payload = {
            "model": self.ollama_model,
            "prompt": query,
            "stream": False  # Get complete response at once
        }
        
        try:
            response = requests.post(url, json=payload, timeout=30)
            response.raise_for_status()
            result = response.json()
            return result.get("response", "")
        except Exception as e:
            raise Exception(f"Ollama API error: {e}. Make sure Ollama is running at {self.ollama_url}")
    
    def _store_in_cache(self, query: str, response: str, embedding: np.ndarray):
        """
        Store query, response, and embedding in Redis.
        
        Concept: Write-Through Caching
        - Immediately store result in cache after generation
        - Uses Redis Hash to store multiple fields together
        - Key format: cache:query:{hash} for uniqueness
        
        Args:
            query: Original query text
            response: LLM response
            embedding: Query embedding vector
        """
        # Generate unique key based on query hash
        # Using hash ensures same query gets same key (deduplication)
        query_hash = hashlib.md5(query.encode()).hexdigest()
        cache_key = f"cache:query:{query_hash}"
        
        # Store as Redis Hash (multiple fields in one key)
        self.redis_client.hset(
            cache_key,
            mapping={
                "query": query,
                "response": response,
                "embedding": embedding.tobytes()  # Store binary embedding
            }
        )
        
        print(f"  → Cached query and response (key: {cache_key})")
    
    def query(self, user_query: str) -> Dict[str, any]:
        """
        Main method: Query with semantic caching.
        
        Flow:
        1. Generate embedding for query
        2. Search for similar cached queries
        3. If similar found → return cached response (HIT)
        4. If not found → call Ollama → cache result → return (MISS)
        
        Args:
            user_query: User's question/query
            
        Returns:
            Dictionary containing:
            - response: LLM response text
            - is_cached: Boolean indicating cache hit/miss
            - similarity: Similarity score (if cached)
            - response_time: Time taken in seconds
        """
        self.stats["total_queries"] += 1
        start_time = time.time()
        
        print(f"\n📝 Query: {user_query}")
        
        # Step 1: Generate embedding for the query
        # This converts text to a numerical vector representing its meaning
        query_embedding = self._generate_embedding(user_query)
        
        # Step 2: Search for similar queries in cache
        # This performs fast vector similarity search
        cache_search_start = time.time()
        cached_result = self._search_similar_queries(query_embedding)
        cache_search_time = time.time() - cache_search_start
        
        if cached_result:
            # CACHE HIT: Similar query found
            cached_response, similarity = cached_result
            response_time = time.time() - start_time
            
            self.stats["cache_hits"] += 1
            self.stats["total_cache_time"] += response_time
            
            print(f"  ✓ CACHE HIT (similarity: {similarity:.3f})")
            print(f"  ⚡ Response time: {response_time:.3f}s (from cache)")
            
            return {
                "response": cached_response,
                "is_cached": True,
                "similarity": similarity,
                "response_time": response_time,
                "cache_search_time": cache_search_time
            }
        else:
            # CACHE MISS: No similar query found, call Ollama
            print(f"  ✗ CACHE MISS (no similar query found above threshold {self.similarity_threshold})")
            print(f"  → Calling Ollama ({self.ollama_model})...")
            
            ollama_start = time.time()
            llm_response = self._call_ollama(user_query)
            ollama_time = time.time() - ollama_start
            
            # Step 3: Store in cache for future queries
            self._store_in_cache(user_query, llm_response, query_embedding)
            
            response_time = time.time() - start_time
            
            self.stats["cache_misses"] += 1
            self.stats["total_ollama_time"] += ollama_time
            
            print(f"  ⏱️  Ollama time: {ollama_time:.3f}s")
            print(f"  ⏱️  Total time: {response_time:.3f}s")
            
            return {
                "response": llm_response,
                "is_cached": False,
                "similarity": None,
                "response_time": response_time,
                "ollama_time": ollama_time
            }
    
    def get_stats(self) -> Dict[str, any]:
        """Get cache performance statistics."""
        if self.stats["total_queries"] == 0:
            return self.stats
        
        hit_rate = (self.stats["cache_hits"] / self.stats["total_queries"]) * 100
        avg_cache_time = (
            self.stats["total_cache_time"] / self.stats["cache_hits"]
            if self.stats["cache_hits"] > 0 else 0
        )
        avg_ollama_time = (
            self.stats["total_ollama_time"] / self.stats["cache_misses"]
            if self.stats["cache_misses"] > 0 else 0
        )
        
        speedup = avg_ollama_time / avg_cache_time if avg_cache_time > 0 else 0
        
        return {
            **self.stats,
            "hit_rate": hit_rate,
            "avg_cache_time": avg_cache_time,
            "avg_ollama_time": avg_ollama_time,
            "speedup_factor": speedup
        }
    
    def clear_cache(self):
        """Clear all cached queries."""
        deleted = 0
        for key in self.redis_client.scan_iter(match="cache:query:*"):
            self.redis_client.delete(key)
            deleted += 1
        print(f"✓ Cleared {deleted} cached queries")


def run_demo():
    """
    Demonstration of semantic caching system.
    
    Tests with diverse queries including:
    - Exact duplicates
    - Paraphrased questions
    - Completely new queries
    """
    print("=" * 80)
    print("SEMANTIC CACHING DEMO WITH REDIS AND OLLAMA")
    print("=" * 80)
    print("\nThis demo shows how semantic caching works:")
    print("1. First query calls Ollama (slow)")
    print("2. Similar queries return cached response (fast)")
    print("3. Completely different queries call Ollama again")
    print()
    
    # Initialize semantic cache
    try:
        cache = SemanticCache(
            ollama_model="llama3.2",  # Change to your installed model
            similarity_threshold=0.85
        )
    except Exception as e:
        print(f"Error initializing cache: {e}")
        print("\nMake sure:")
        print("1. Redis is running: redis-server")
        print("2. Ollama is running: ollama serve")
        print("3. Required packages are installed (see requirements.txt)")
        return
    
    # Test queries - diverse set as required
    test_queries = [
        # Original queries
        "What is machine learning?",
        "Explain how neural networks work",
        "What are the benefits of cloud computing?",
        
        # Paraphrased (should hit cache)
        "Can you tell me about machine learning?",  # Similar to query 1
        "How do neural networks function?",  # Similar to query 2
        "What advantages does cloud computing offer?",  # Similar to query 3
        
        # Exact duplicates (should definitely hit cache)
        "What is machine learning?",  # Exact duplicate
        "Explain how neural networks work",  # Exact duplicate
        
        # New topics (should miss cache)
        "What is Redis caching?",
        "How does vector similarity search work?",
        "Explain semantic caching in detail",
    ]
    
    print(f"Testing with {len(test_queries)} queries...\n")
    print("=" * 80)
    
    results = []
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n[Query {i}/{len(test_queries)}]")
        print("-" * 80)
        
        result = cache.query(query)
        results.append(result)
        
        # Display response (truncated for readability)
        response_preview = result["response"][:200] + "..." if len(result["response"]) > 200 else result["response"]
        print(f"\n📄 Response (preview): {response_preview}")
        
        time.sleep(0.5)  # Small delay between queries
    
    # Display statistics
    print("\n" + "=" * 80)
    print("PERFORMANCE STATISTICS")
    print("=" * 80)
    
    stats = cache.get_stats()
    
    print(f"\n📊 Overall Statistics:")
    print(f"  Total queries: {stats['total_queries']}")
    print(f"  Cache hits: {stats['cache_hits']} ({stats.get('hit_rate', 0):.1f}%)")
    print(f"  Cache misses: {stats['cache_misses']}")
    
    if stats["cache_hits"] > 0 and stats["cache_misses"] > 0:
        print(f"\n⏱️  Performance Metrics:")
        print(f"  Average cache response time: {stats['avg_cache_time']:.3f}s")
        print(f"  Average Ollama response time: {stats['avg_ollama_time']:.3f}s")
        print(f"  ⚡ Speedup factor: {stats['speedup_factor']:.1f}x faster with cache!")
    
    print("\n" + "=" * 80)
    print("Demo completed!")
    print("=" * 80)


if __name__ == "__main__":
    run_demo()
