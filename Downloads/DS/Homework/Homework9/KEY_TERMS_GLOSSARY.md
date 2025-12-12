# 📖 Key Terms Glossary - HW9: Redis Caching & Semantic Search

## Caching Concepts

### **Cache**
A temporary storage location (usually in fast memory) that holds frequently accessed data to reduce the time needed to retrieve it from slower storage systems.

### **Caching**
The process of storing data in a cache so it can be retrieved faster on subsequent requests.

### **Cache Hit**
When requested data is found in the cache, allowing for fast retrieval without accessing the slower data source.

### **Cache Miss**
When requested data is not found in the cache, requiring access to the slower data source (like a database or API).

### **Cache Invalidation**
The process of removing or updating cached data when the original data changes, ensuring users don't receive stale information.

### **TTL (Time To Live)**
The amount of time a cached item remains valid before it expires and needs to be refreshed from the source.

### **Write-Through Cache**
A caching strategy where data is written to both the cache and the underlying storage system simultaneously.

### **Read-Through Cache**
A caching strategy where, on a cache miss, data is fetched from storage and stored in the cache before being returned.

### **Write-Back Cache**
A caching strategy where writes go to the cache first and are written to storage later, improving write performance but risking data loss.

### **Batch Write**
Writing multiple operations together instead of individually, reducing the number of write operations and improving performance.

---

## Redis Terms

### **Redis**
An open-source, in-memory data structure store that can be used as a database, cache, or message broker, known for its high performance.

### **In-Memory Database**
A database that stores data in RAM instead of on disk, making it much faster but volatile (data lost on restart unless persisted).

### **Redis Key**
A unique identifier used to store and retrieve values in Redis, following a naming pattern like `user:123` or `views:post:5`.

### **Redis Hash**
A Redis data structure that stores field-value pairs within a single key, like a dictionary or object in other languages.

### **Redis String**
A Redis data structure that stores simple string values, often used for counters and simple key-value storage.

### **Atomic Operation**
An operation that is guaranteed to complete fully or not at all, even when multiple processes access it simultaneously (no partial execution).

### **INCR Command**
A Redis command that atomically increments a numeric value stored at a key, commonly used for counters and view tracking.

### **Redis CLI**
The command-line interface tool for interacting with Redis, allowing you to execute commands and check data.

### **Redis Flush**
A command that clears all data from a Redis database, useful for testing but dangerous in production.

---

## Database Terms

### **SQLite**
A lightweight, file-based database that stores data in a single file, perfect for development and small applications.

### **SQL**
Structured Query Language, the language used to interact with relational databases to query, insert, update, and delete data.

### **Parameterized Query**
A database query that uses placeholders (like `?`) for values, preventing SQL injection attacks and improving security.

### **Schema**
The structure or blueprint of a database, defining what tables exist and what columns each table has.

### **Transaction**
A sequence of database operations that are executed as a single unit - either all succeed or all fail (atomicity).

### **Commit**
The action that makes database changes permanent, saving them to disk.

---

## Vector Embeddings & Semantic Search

### **Vector Embedding**
A numerical representation of text (or other data) as an array of numbers that captures semantic meaning, allowing mathematical comparison.

### **Embedding Dimension**
The size of the vector array (e.g., 384 numbers), representing how many features are used to encode the meaning.

### **Semantic Similarity**
The measure of how similar two pieces of text are based on their meaning, not just exact word matching.

### **Semantic Caching**
A caching technique that stores and retrieves data based on semantic similarity, so similar queries (even with different wording) can use cached results.

### **SentenceTransformer**
A machine learning model that converts sentences into vector embeddings, capturing semantic meaning in numerical form.

### **Text-to-Vector Conversion**
The process of transforming text into a numerical vector using a machine learning model, enabling mathematical operations on text.

---

## Similarity Metrics

### **Cosine Similarity**
A measure of similarity between two vectors based on the cosine of the angle between them, ranging from -1 (opposite) to 1 (identical), perfect for normalized embeddings.

### **Euclidean Distance**
The straight-line distance between two points in vector space, with smaller distances indicating greater similarity.

### **Dot Product**
The sum of element-wise multiplication of two vectors, used in cosine similarity calculations.

### **Vector Normalization**
The process of scaling a vector to unit length (magnitude of 1), often done to make cosine similarity more meaningful.

### **Similarity Threshold**
A minimum similarity score (like 0.85) that determines whether two items are considered similar enough to use cached results.

---

## Vector Search & Indexing

### **Vector Search**
The process of finding similar vectors in a database by comparing their mathematical representations rather than exact matches.

### **KNN (K-Nearest Neighbors)**
A search algorithm that finds the K most similar items to a query by comparing vectors.

### **HNSW (Hierarchical Navigable Small World)**
An algorithm used by Redis for fast vector similarity search, building a graph structure to navigate efficiently through similar vectors.

### **Vector Index**
A data structure that organizes vectors for fast similarity search, allowing queries to find similar vectors without checking every single one.

### **RedisSearch**
A Redis module that adds full-text and vector search capabilities to Redis, enabling fast similarity queries.

### **RediSearch**
The commercial version of RedisSearch with additional features and enterprise support.

### **Redis Vector Index**
A Redis index specifically configured to store and search vector embeddings efficiently.

---

## LLM & Ollama Terms

### **LLM (Large Language Model)**
A machine learning model trained on vast amounts of text that can generate human-like responses to prompts.

### **Ollama**
An open-source tool that allows you to run large language models locally on your computer, without needing cloud API access.

### **Ollama Model**
A specific LLM (like llama3.2 or mistral) that Ollama can run locally for generating text responses.

### **API Endpoint**
A specific URL where you can send requests to interact with a service, like `/api/generate` for Ollama.

### **Prompt**
The input text/question sent to an LLM to generate a response.

### **Inference**
The process of generating a response from an LLM based on a given prompt.

### **Streaming Response**
When an LLM sends its response token-by-token as it generates them, rather than waiting for the complete response.

---

## Performance Terms

### **Response Time**
The amount of time it takes to complete a request and return a response, measured in milliseconds or seconds.

### **Latency**
The delay between making a request and receiving a response, often measured in milliseconds.

### **Throughput**
The number of operations a system can handle per unit of time (e.g., requests per second).

### **Speedup Factor**
The ratio showing how much faster one method is compared to another (e.g., "10x faster" means 10 times as fast).

### **Cache Hit Rate**
The percentage of requests that find data in the cache, calculated as (cache hits / total requests) × 100%.

### **Cache Miss Rate**
The percentage of requests that don't find data in the cache, calculated as (cache misses / total requests) × 100%.

---

## Python & Programming Terms

### **NumPy**
A Python library for numerical computing that provides efficient array operations and mathematical functions.

### **JSON (JavaScript Object Notation)**
A lightweight data format for storing and exchanging data, commonly used for APIs and data serialization.

### **Serialization**
The process of converting data structures (like Python dictionaries) into a format that can be stored or transmitted (like JSON strings).

### **Deserialization**
The process of converting stored or transmitted data (like JSON strings) back into usable data structures (like Python dictionaries).

### **Type Hint**
A Python feature that indicates what type of data a variable or function parameter should be, improving code clarity.

### **Optional Type**
A type hint indicating that a value can be either a specific type or None (null).

### **Hash Function**
A function that converts data of arbitrary size into a fixed-size value (hash), often used to create unique identifiers.

### **MD5 Hash**
A cryptographic hash function that generates a unique 32-character hexadecimal string for any input, useful for creating unique cache keys.

---

## Architecture Terms

### **Client-Server Architecture**
A system design where clients (like web browsers) make requests to servers that process and respond to them.

### **Microservices**
An architectural approach where applications are built as a collection of small, independent services that communicate over APIs.

### **API (Application Programming Interface)**
A set of rules and protocols that allows different software components to communicate with each other.

### **Stateless**
A characteristic of systems that don't store client state between requests, with each request containing all necessary information.

---

## Data Structure Terms

### **Array**
An ordered collection of items (like a list), where each item can be accessed by its position (index).

### **Dictionary**
A data structure that stores key-value pairs, allowing you to look up values by their keys (like a phone book).

### **Key-Value Store**
A database that stores data as pairs of keys and values, making lookups very fast (Redis is a key-value store).

### **Namespace**
A way of organizing keys with prefixes (like `user:123` and `post:456`) to prevent naming conflicts.

---

## Error Handling Terms

### **Exception**
An error that occurs during program execution, disrupting the normal flow of the program.

### **Try-Except Block**
A Python construct that catches and handles exceptions, allowing the program to continue running even if errors occur.

### **Connection Error**
An error that occurs when a program cannot establish a connection to a remote service (like Redis or Ollama).

### **Fallback Method**
An alternative method used when the primary method fails, ensuring the system continues to work even in error conditions.

---

## Testing & Debugging Terms

### **Test Query**
A sample question or request used to verify that a system works correctly.

### **Exact Duplicate**
A query that is identical to a previously seen query, word-for-word.

### **Paraphrased Query**
A query that asks the same thing as another query but uses different words (e.g., "What is ML?" vs "Can you explain machine learning?").

### **Diverse Queries**
A collection of different types of queries (exact matches, paraphrases, and completely new topics) used to thoroughly test a system.

---

## Statistical Terms

### **Statistics**
Numerical data that summarizes the performance and behavior of a system (like hit rates, response times).

### **Average Response Time**
The mean time taken to complete requests, calculated by summing all response times and dividing by the number of requests.

### **Cache Performance Metrics**
Measurements that evaluate how well caching is working, including hit rate, response times, and speedup factors.

---

## Real-World Analogy

Think of caching like a restaurant's preparation system:

- **Cache (Redis)** = The prep station where frequently used ingredients are kept ready
- **Database** = The walk-in refrigerator where all ingredients are stored long-term
- **Cache Hit** = Finding the ingredient you need already prepared on the counter (fast!)
- **Cache Miss** = Having to go to the refrigerator to get the ingredient (slower)
- **TTL** = How long prepared ingredients stay fresh before needing to be replaced
- **Vector Embedding** = A recipe card that describes ingredients by their characteristics (not just names)
- **Semantic Caching** = Finding a similar dish recipe even if the exact name is different
- **Cosine Similarity** = Comparing how similar two recipes are based on their ingredients and methods
- **Ollama/LLM** = The head chef who creates new recipes when asked
- **Semantic Search** = Finding recipes that taste similar, even if they have different names
- **Atomic Operation (INCR)** = A ticket counter that ensures every customer gets a unique number, even when many arrive at once
- **Batch Write** = Prepping multiple meals' ingredients at once instead of one at a time
- **Cache Invalidation** = Removing outdated prepared ingredients when the recipe changes

---

## Quick Reference: Most Important Terms

1. **Cache** = Fast temporary storage for frequently accessed data
2. **Cache Hit** = Found in cache (fast), **Cache Miss** = Not in cache (slow)
3. **Redis** = In-memory database perfect for caching
4. **Vector Embedding** = Numerical representation of text that captures meaning
5. **Semantic Caching** = Cache based on meaning, not exact text matching
6. **Cosine Similarity** = Measure of how similar two vectors are (0-1 scale)
7. **Atomic Operation** = Guaranteed to complete fully or not at all (thread-safe)
8. **Write-Through Cache** = Writes go to both cache and storage
9. **Batch Write** = Multiple operations combined into one for efficiency
10. **TTL** = How long cached data remains valid before expiring
11. **HNSW** = Algorithm for fast vector similarity search in Redis
12. **Similarity Threshold** = Minimum score (like 0.85) to consider items similar
13. **Ollama** = Tool to run LLMs locally
14. **KNN Search** = Finding the K most similar items to a query
15. **Cache Hit Rate** = Percentage of requests served from cache

---

## Category Quick Find

- **Caching Basics**: Cache, Cache Hit, Cache Miss, TTL, Cache Invalidation
- **Redis**: Redis, Atomic Operation, INCR, Redis Hash, Redis Key
- **Vector Embeddings**: Vector Embedding, Semantic Similarity, SentenceTransformer
- **Similarity**: Cosine Similarity, Similarity Threshold, Euclidean Distance
- **Vector Search**: Vector Search, KNN, HNSW, Vector Index
- **LLM**: Ollama, LLM, Prompt, Inference
- **Performance**: Response Time, Speedup Factor, Cache Hit Rate, Latency
- **Database**: SQLite, SQL, Parameterized Query, Schema, Transaction
