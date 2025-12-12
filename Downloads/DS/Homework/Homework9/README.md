# HW9: Redis Caching and Semantic Search

This homework implements two caching systems:
1. **Task 1**: High-performance blog post view counter using Redis
2. **Task 2**: Semantic caching system for LLM responses using Redis vector search and Ollama

## Quick Start

### Prerequisites

1. **Redis** (required for both tasks)
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

2. **Ollama** (required for Task 2 only)
```bash
# Download from https://ollama.ai/ or:
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a model (e.g., llama3.2)
ollama pull llama3.2

# Verify Ollama is running
curl http://localhost:11434/api/tags
```

3. **Python Dependencies**
```bash
pip install -r requirements.txt
```

### Running the Code

**Task 1: Post View Counter**
```bash
python demo.py
```

**Task 2: Semantic Caching**
```bash
python semantic_cache.py
```

## Files

- `demo.py` - Task 1 implementation (view counter + original demos)
- `semantic_cache.py` - Task 2 implementation (semantic caching with Ollama)
- `requirements.txt` - Python dependencies
- `HW9_EXPLANATION.md` - Comprehensive line-by-line explanation of all concepts
- `README.md` - This file

## Task 1: Post View Counter

Implements `increment_post_views(post_id)` method that:
- Increments view count in Redis (fast, atomic operation)
- Syncs to database every 10 views (batch writes)
- Returns current view count

**Key Concepts:**
- Write-through caching with batch updates
- Atomic operations (`INCR`)
- Performance optimization (Redis microseconds vs DB milliseconds)

## Task 2: Semantic Caching

Implements semantic caching system that:
- Stores LLM responses in Redis with vector embeddings
- Searches for semantically similar queries (not exact matches)
- Returns cached responses when similarity > 0.85
- Calls Ollama for new queries and caches results
- Tracks cache hits/misses and measures performance

**Key Concepts:**
- Vector embeddings (SentenceTransformers)
- Cosine similarity for semantic matching
- Redis vector search (HNSW algorithm)
- Performance: 4-15x faster than direct LLM calls

## Testing

The semantic cache demo tests with:
- Exact duplicate queries (should hit cache)
- Paraphrased questions (should hit cache if similar enough)
- Completely new queries (should miss cache, call Ollama)

Expected output shows:
- Cache hit/miss for each query
- Similarity scores
- Response times (cache vs Ollama)
- Overall statistics (hit rate, speedup factor)

## Troubleshooting

**Redis connection error:**
- Make sure Redis is running: `redis-cli ping`
- Check host/port in code (default: localhost:6379)

**Ollama connection error:**
- Make sure Ollama is running: `curl http://localhost:11434/api/tags`
- Check model name is installed: `ollama list`
- Update `ollama_model` in code if needed

**RedisSearch/RediSearch not available:**
- The code includes a fallback search method
- It will work but may be slower for large caches
- For best performance, install RedisStack: https://redis.io/download

**Import errors:**
- Install dependencies: `pip install -r requirements.txt`
- For sentence-transformers, you may need: `pip install torch`

## Performance Expectations

**Task 1:**
- Redis INCR: ~0.1ms per increment
- Database UPDATE: ~5-10ms (only every 10 views)

**Task 2:**
- Cache hit: ~15-50ms (embedding + search)
- Cache miss (Ollama): ~1000-3000ms (LLM inference)
- Speedup: 50-200x faster with cache

## Detailed Documentation

See `HW9_EXPLANATION.md` for:
- Line-by-line code explanations
- Detailed concept explanations
- Architecture diagrams
- Mathematical formulas
- Best practices and trade-offs

## Assignment Requirements

✅ Task 1: `increment_post_views` method implemented  
✅ Task 2: Semantic caching system with Redis and Ollama  
✅ Vector embeddings using SentenceTransformers  
✅ Similarity threshold: 0.85  
✅ Cache hit/miss tracking with performance metrics  
✅ Testing with 10+ diverse queries  
✅ Documentation and explanations  
