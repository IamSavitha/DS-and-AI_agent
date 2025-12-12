# HW9: Redis Caching and Semantic Search - Detailed Explanation

This document provides a comprehensive, line-by-line explanation of all concepts and implementations in HW9.

---

## Table of Contents

1. [Task 1: Post View Counter with Redis](#task-1-post-view-counter-with-redis)
2. [Task 2: Semantic Caching with Redis and Ollama](#task-2-semantic-caching-with-redis-and-ollama)
3. [Core Concepts Explained](#core-concepts-explained)
4. [How to Run](#how-to-run)

---

## Task 1: Post View Counter with Redis

### Overview

Implements a high-performance view counter for blog posts using Redis as a caching layer. This demonstrates **write-through caching with batch updates**.

### File: `demo.py` - `increment_post_views` Method

```python
def increment_post_views(self, post_id: int) -> int:
```

#### Concept: Write-Through Caching Pattern

**What is it?**
- A caching strategy where writes go to both cache (Redis) and database
- In our case, we use a **batch write** variant: writes go to Redis immediately, but database updates happen periodically

**Why use it?**
- **Performance**: Redis INCR is extremely fast (microseconds) vs database writes (milliseconds)
- **Scalability**: Can handle thousands of concurrent views without database bottleneck
- **Reliability**: Periodic database sync ensures data persistence

#### Line-by-Line Explanation

```python
cache_key = f"views:post:{post_id}"
```
- **Concept**: Redis Key Naming Convention
- Creates a unique key for each post's view count
- Format: `views:post:1`, `views:post:2`, etc.
- This namespacing prevents key collisions

```python
view_count = self.redis_client.incr(cache_key)
```
- **Concept**: Atomic Operations in Redis
- `INCR` is an **atomic operation** - guaranteed to be thread-safe
- If 100 users view a post simultaneously, all increments are counted correctly
- Returns the **new value** after incrementing
- **Performance**: This operation takes microseconds vs milliseconds for database UPDATE

```python
if view_count % 10 == 0:
```
- **Concept**: Batch Write Pattern / Modulo Arithmetic
- `%` is the modulo operator (returns remainder after division)
- When `view_count` is 10, 20, 30, etc., `view_count % 10 == 0` is True
- This triggers database sync every 10 views
- **Trade-off**: We accept losing up to 9 views if Redis crashes (acceptable for analytics)

```python
self.cursor.execute("UPDATE posts SET views = ? WHERE id = ?", (view_count, post_id))
self.conn.commit()
```
- **Concept**: Parameterized Queries for SQL Injection Prevention
- `?` placeholders prevent SQL injection attacks
- Only commits every 10 views, reducing database load by 90%
- This is the "batch write" - multiple Redis writes = one database write

### Database Schema Update

```python
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT,
    views INTEGER DEFAULT 0
)
```

- **Concept**: Database Schema Design
- `views` column stores the persistent view count
- `DEFAULT 0` ensures new posts start at 0 views
- This table persists data even if Redis cache is cleared

---

## Task 2: Semantic Caching with Redis and Ollama

### Overview

Implements a **semantic caching system** that stores LLM responses and retrieves them based on **meaning similarity**, not exact text matching. This is revolutionary for LLM applications because:

- "What is ML?" and "Can you explain machine learning?" are semantically similar
- Both should return the same cached response
- Saves expensive LLM API calls (4-15x speedup)

### File: `semantic_cache.py`

### Core Concepts

#### 1. Vector Embeddings

**What are embeddings?**
- Text → Array of numbers (vector)
- Example: "cat" → `[0.2, -0.5, 0.8, ..., 0.3]` (384 numbers)
- Similar texts have similar vectors

**How are they generated?**
- SentenceTransformers uses neural networks trained on millions of text pairs
- The model learns to encode meaning into numbers
- "Cat" and "Feline" will have vectors pointing in similar directions

```python
self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
```

**Why this model?**
- `all-MiniLM-L6-v2`: Lightweight, fast, good quality
- 384 dimensions: Good balance between accuracy and speed
- Trained on diverse text for general-purpose embeddings

#### 2. Cosine Similarity

**What is it?**
- Measures the **angle** between two vectors, not their magnitude
- Range: -1 (opposite) to 1 (identical)
- Perfect for text: focuses on **direction** (meaning) not length

**Mathematical Formula:**
```
cosine_similarity = (A · B) / (||A|| * ||B||)
```

Where:
- `A · B` = dot product (sum of element-wise multiplication)
- `||A||` = magnitude (length) of vector A
- `||B||` = magnitude (length) of vector B

```python
def _cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
    dot_product = np.dot(vec1, vec2)      # A · B
    norm1 = np.linalg.norm(vec1)          # ||A||
    norm2 = np.linalg.norm(vec2)          # ||B||
    similarity = dot_product / (norm1 * norm2)  # Final calculation
    return max(0.0, min(1.0, similarity))  # Clamp to [0, 1]
```

**Example:**
- Query 1: "What is machine learning?"
- Query 2: "Can you explain machine learning?"
- Similarity: 0.92 (very similar, would hit cache with threshold 0.85)

#### 3. Redis Vector Search

**What is it?**
- Redis can store vectors and perform fast similarity search
- Uses **HNSW (Hierarchical Navigable Small World)** algorithm
- Much faster than comparing against all vectors manually

**Index Creation:**
```python
"FT.CREATE", index_name,
"ON", "HASH",                    # Store in Redis Hash data structure
"PREFIX", "1", "cache:query:",   # Only index keys starting with "cache:query:"
"SCHEMA",
    "query", "TEXT",             # Original query text (for debugging)
    "response", "TEXT",          # Cached LLM response
    "embedding", "VECTOR",       # Vector field for similarity search
        "HNSW",                  # Algorithm: Hierarchical Navigable Small World
        "6",                     # M: connections per layer (higher = more accurate, slower)
        "10",                    # EF_CONSTRUCTION: candidate list size
        "TYPE", "FLOAT32",       # 32-bit floating point numbers
        "DIM", "384",            # Vector dimension (must match embedding size)
        "DISTANCE_METRIC", "COSINE"  # Use cosine similarity for distance
```

**HNSW Algorithm:**
- Builds a graph structure connecting similar vectors
- Search starts at random node, navigates to nearest neighbors
- Much faster than brute-force comparison (O(log n) vs O(n))

#### 4. Semantic Cache Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    USER QUERY ARRIVES                        │
│              "What is machine learning?"                     │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 1: GENERATE EMBEDDING                          │
│  SentenceTransformer.encode() → [0.2, -0.5, 0.8, ...]      │
│  (384-dimensional vector representing semantic meaning)     │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│     STEP 2: SEARCH REDIS FOR SIMILAR EMBEDDINGS             │
│  FT.SEARCH with KNN query → Find top similar vectors        │
│  Calculate cosine similarity for each candidate             │
└───────────────────────────┬─────────────────────────────────┘
                            │
        ┌───────────────────┴───────────────────┐
        │                                       │
   SIMILARITY ≥ 0.85                    SIMILARITY < 0.85
        │                                       │
        ▼                                       ▼
┌───────────────────┐              ┌───────────────────────────┐
│   CACHE HIT       │              │      CACHE MISS           │
│                   │              │                           │
│ Return cached     │              │ 1. Call Ollama API        │
│ response          │              │ 2. Get LLM response       │
│ (Fast: ~10ms)     │              │ 3. Store in Redis cache   │
│                   │              │ 4. Return response        │
│ is_cached = True  │              │    (Slow: ~2000ms)        │
└───────────────────┘              │                           │
                                   │ is_cached = False         │
                                   └───────────────────────────┘
```

### Line-by-Line Code Explanation

#### Initialization

```python
self.embedding_model = SentenceTransformer(embedding_model)
```
- Loads pre-trained neural network for text-to-vector conversion
- First run downloads model (~80MB) - cached for future use
- Model is loaded into memory for fast encoding

```python
self.embedding_dim = self.embedding_model.get_sentence_embedding_dimension()
```
- Gets the size of vectors this model produces
- `all-MiniLM-L6-v2` produces 384-dimensional vectors
- Needed to configure Redis vector index correctly

#### Query Processing

```python
def query(self, user_query: str) -> Dict[str, any]:
```

**Step 1: Generate Embedding**
```python
query_embedding = self._generate_embedding(user_query)
```
- Converts text query to numerical vector
- Time: ~5-10ms
- Vector captures semantic meaning, not exact words

**Step 2: Search Cache**
```python
cached_result = self._search_similar_queries(query_embedding)
```
- Searches Redis for similar query embeddings
- Uses vector similarity search (KNN)
- Returns best match if similarity ≥ threshold (0.85)

**Step 3a: Cache Hit (Found Similar Query)**
```python
if cached_result:
    cached_response, similarity = cached_result
    return {
        "response": cached_response,
        "is_cached": True,
        "similarity": similarity,
        ...
    }
```
- Return cached LLM response immediately
- No call to Ollama needed
- Typical response time: 10-50ms (vs 1-3s for Ollama)

**Step 3b: Cache Miss (No Similar Query)**
```python
else:
    llm_response = self._call_ollama(user_query)
    self._store_in_cache(user_query, llm_response, query_embedding)
    return {
        "response": llm_response,
        "is_cached": False,
        ...
    }
```
- Call Ollama API to generate response
- Store query, response, and embedding in Redis
- Future similar queries will hit cache

#### Ollama Integration

```python
def _call_ollama(self, query: str) -> str:
    url = f"{self.ollama_url}/api/generate"
    payload = {
        "model": self.ollama_model,
        "prompt": query,
        "stream": False  # Get complete response
    }
    response = requests.post(url, json=payload)
    return response.json().get("response", "")
```

**Concepts:**
- **API Endpoint**: `/api/generate` is Ollama's text generation endpoint
- **Model Selection**: Choose which LLM to use (llama3.2, mistral, etc.)
- **Streaming**: `stream: False` means wait for complete response
- **Timeout**: 30 seconds max wait time

#### Cache Storage

```python
def _store_in_cache(self, query: str, response: str, embedding: np.ndarray):
    query_hash = hashlib.md5(query.encode()).hexdigest()
    cache_key = f"cache:query:{query_hash}"
    
    self.redis_client.hset(
        cache_key,
        mapping={
            "query": query,
            "response": response,
            "embedding": embedding.tobytes()
        }
    )
```

**Concepts:**
- **Hash Function**: MD5 creates unique identifier for query
- Same query always gets same hash → prevents duplicates
- **Redis Hash**: `HSET` stores multiple fields in one key
- **Binary Storage**: Embeddings stored as bytes (efficient)

---

## Core Concepts Explained

### 1. Caching Strategies

#### Write-Through Cache
- Writes go to both cache and database
- Ensures consistency but slower writes
- Our Task 1 uses **batch write-through**: Redis immediately, DB periodically

#### Read-Through Cache
- On cache miss, fetch from database and cache
- Used in `get_user_by_id_with_cache()` method
- Pattern: Check cache → If miss, query DB → Cache result → Return

#### Write-Back Cache
- Writes go to cache only, DB updated later
- Fastest but risk of data loss
- Not used in our implementation

### 2. Redis Data Structures

#### Strings (`GET`, `SET`, `INCR`)
- Simple key-value storage
- Used for: counters, simple values, TTL management
- Example: `views:post:1` → `"42"`

#### Hashes (`HSET`, `HGET`, `HGETALL`)
- Multiple fields in one key
- Used for: complex objects (query, response, embedding)
- Example: `cache:query:abc123` → `{query: "...", response: "...", embedding: b"..."}`

#### Sets (`SADD`, `SMEMBERS`)
- Unordered collection of unique strings
- Used for: tags, categories, unique members

#### Sorted Sets (`ZADD`, `ZRANGE`)
- Set with scores (sorted)
- Used for: leaderboards, time-series data

### 3. Vector Similarity Search

#### Why Vectors for Text?
- Traditional search: Exact keyword matching
  - "cat" matches "cat" but not "feline"
- Vector search: Semantic matching
  - "cat" and "feline" have similar vectors → both match

#### Cosine Similarity vs Other Metrics

**Cosine Similarity** (What we use)
- Measures angle between vectors
- Range: -1 to 1
- Best for: Normalized embeddings (all same length)
- **Why we use it**: SentenceTransformer embeddings are normalized

**Euclidean Distance**
- Straight-line distance in vector space
- Range: 0 to ∞
- Lower = more similar
- Better for: Non-normalized vectors

**Dot Product**
- Sum of element-wise multiplication
- Range: -∞ to ∞
- Only works if vectors are normalized

#### Threshold Selection (0.85)

- **Too low (e.g., 0.5)**: Returns irrelevant cached results
- **Too high (e.g., 0.95)**: Misses valid paraphrases
- **0.85**: Good balance - catches paraphrases but filters unrelated queries
- Can be tuned based on use case

### 4. Performance Optimization

#### Why Semantic Caching is Fast

1. **Embedding Generation**: ~10ms (local model)
2. **Vector Search**: ~5-20ms (Redis HNSW index)
3. **Cache Hit Total**: ~15-30ms

vs.

1. **LLM API Call**: ~1000-3000ms (Ollama inference)
2. **Cache Miss Total**: ~1000-3000ms

**Speedup**: 50-200x faster!

#### Batch Operations

In Task 1, we batch database writes:
- 100 views → 10 database writes (instead of 100)
- Reduces database load by 90%
- Acceptable trade-off: Can lose up to 9 views on crash

### 5. Distributed Systems Concepts

#### Atomic Operations
- `INCR` in Redis is atomic
- Multiple concurrent increments are safe
- No race conditions or lost updates

#### Cache Invalidation
- When data changes, remove from cache
- Example: `invalidate_user_cache(user_id)`
- Ensures stale data isn't served

#### TTL (Time To Live)
- Cache entries expire after set time
- Example: `setex(key, 300, value)` → expires in 300 seconds
- Balances freshness vs performance

---

## How to Run

### Prerequisites

1. **Install Redis**
```bash
# macOS
brew install redis
brew services start redis

# Linux
sudo apt-get install redis-server
sudo systemctl start redis

# Verify
redis-cli ping  # Should return "PONG"
```

2. **Install Ollama**
```bash
# Download from https://ollama.ai/
# Or use:
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a model
ollama pull llama3.2

# Start server (usually runs automatically)
ollama serve
```

3. **Install Python Dependencies**
```bash
pip install -r requirements.txt
```

### Running Task 1

```bash
python demo.py
```

Expected output:
- Shows Redis caching demos
- Demonstrates view counter incrementing
- Shows database sync every 10 views

### Running Task 2

```bash
python semantic_cache.py
```

Expected output:
- Tests 10+ diverse queries
- Shows cache hits for similar queries
- Shows cache misses for new queries
- Displays performance statistics

### Testing Semantic Cache Manually

```python
from semantic_cache import SemanticCache

cache = SemanticCache()

# First query (cache miss)
result1 = cache.query("What is machine learning?")
print(f"Cached: {result1['is_cached']}")  # False

# Similar query (cache hit)
result2 = cache.query("Can you explain machine learning?")
print(f"Cached: {result2['is_cached']}")  # True
print(f"Similarity: {result2['similarity']}")  # ~0.92

# Get statistics
stats = cache.get_stats()
print(f"Hit rate: {stats['hit_rate']}%")
print(f"Speedup: {stats['speedup_factor']}x")
```

---

## Key Takeaways

1. **Redis Caching**: Dramatically speeds up reads by storing hot data in memory
2. **Atomic Operations**: `INCR` is thread-safe for counters
3. **Batch Writes**: Reduce database load by batching updates
4. **Vector Embeddings**: Convert text to numbers that capture meaning
5. **Semantic Similarity**: Find similar queries based on meaning, not exact words
6. **Performance**: Semantic caching can be 50-200x faster than LLM calls
7. **Trade-offs**: Accept small data loss risk for massive performance gains

---

## References

- [Redis Documentation](https://redis.io/docs/)
- [SentenceTransformers](https://www.sbert.net/)
- [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [HNSW Algorithm Paper](https://arxiv.org/abs/1603.09320)
- Lecture Slides: `08-Caching.Redis.agents-caching.pptx.pdf`

---

**End of Documentation**
