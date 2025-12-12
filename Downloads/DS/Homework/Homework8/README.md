# Homework 8: Kafka RPC and Multi-Agent Systems

This homework implements two parts demonstrating distributed systems concepts using Apache Kafka.

## Part 1: Kafka RPC User Management Microservice

A microservice that handles CRUD operations for user management via Kafka messaging using the RPC (Remote Procedure Call) pattern.

## Part 2: Multi-Agent System with Kafka + LangChain

A 3-agent system where agents communicate through Kafka topics to process questions:
- **Planner Agent**: Creates a plan for answering questions
- **Writer Agent**: Writes draft answers using LangChain
- **Reviewer Agent**: Reviews and approves answers

---

## Prerequisites

1. **Docker** installed and running
2. **Node.js** (v14 or higher)
3. **Python** (v3.8 or higher)
4. **OpenAI API Key** (set as environment variable: `OPENAI_API_KEY`)

---

## Setup

### 1. Start Kafka and Zookeeper

```bash
docker-compose up -d
```

Verify containers are running:
```bash
docker ps
```

You should see `kafka-broker` and `kafka-zookeeper` containers.

### 2. Install Dependencies

**For Part 1 (Node.js):**
```bash
npm install
```

**For Part 2 (Python):**
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variable

```bash
export OPENAI_API_KEY="your-api-key-here"
```

---

## Part 1: User Management Microservice

### Setup Topics

```bash
npm run setup
# or
node setup-topics.js
```

This creates:
- `request_topic` - for client requests
- `response_topic` - for service responses

### Run the Service

**Terminal 1 - Start Consumer:**
```bash
npm run start:consumer
# or
node consumer.js
```

You should see:
```
✓ Producer is ready
✓ Consumer is ready and listening on 'request_topic'
🚀 Kafka Consumer Service Started
📡 Waiting for messages on 'request_topic'...
```

### Run the Demo

**Terminal 2 - Run Demo:**
```bash
node homework-demo.js
```

The demo will:
1. Create 3 users
2. List all users
3. Get a user by ID
4. Update a user
5. Delete a user
6. List users again
7. Demonstrate error handling

---

## Part 2: Multi-Agent System

### Setup Topics

Create the required Kafka topics:

```bash
# Option 1: Using kafka-topics CLI (if available)
kafka-topics --create --topic inbox --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
kafka-topics --create --topic tasks --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
kafka-topics --create --topic drafts --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
kafka-topics --create --topic final --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092

# Option 2: Using Python script
python setup-topics-part2.py
```

### Run the Agents

You need to run each agent in a **separate terminal**:

**Terminal 1 - Planner Agent:**
```bash
python planner.py
```

**Terminal 2 - Writer Agent:**
```bash
python writer.py
```

**Terminal 3 - Reviewer Agent:**
```bash
python reviewer.py
```

### Send a Question

**Terminal 4 - Send Question:**
```bash
python send_question.py "What are the key benefits of using Apache Kafka for distributed systems?"
```

Or with a custom question:
```bash
python send_question.py "Your question here"
```

### View Results

**Terminal 5 - Check Final Topic:**
```bash
# Using kafka-console-consumer
kafka-console-consumer --topic final --from-beginning --bootstrap-server localhost:9092

# Or using Python
python read_final.py
```

You should see a JSON message with:
```json
{
  "question_id": "q_1234567890",
  "original_question": "...",
  "answer": "...",
  "status": "approved",
  "quality_score": 8,
  "review": {...}
}
```

---

## File Structure

```
Homework8/
├── Part 1 - Kafka RPC/
│   ├── consumer.js          # User management service
│   ├── client.js            # RPC client wrapper
│   ├── rpc.js               # RPC implementation
│   ├── connection.js        # Kafka connection provider
│   ├── setup-topics.js      # Topic setup script
│   ├── homework-demo.js     # Demo script
│   ├── demo.js              # Original demo
│   └── package.json         # Node.js dependencies
│
├── Part 2 - Multi-Agent System/
│   ├── planner.py           # Planning agent
│   ├── writer.py            # Writing agent
│   ├── reviewer.py          # Review agent
│   ├── send_question.py     # Question sender
│   └── requirements.txt     # Python dependencies
│
├── Infrastructure/
│   ├── docker-compose.yml   # Kafka and Zookeeper
│   └── Dockerfile           # Python agent container
│
└── Documentation/
    ├── README.md            # This file
    └── HW8_CONCEPTS_EXPLANATION.md  # Detailed concepts
```

---

## Troubleshooting

### Kafka Connection Issues

**Error: "Connection refused"**
- Ensure Docker containers are running: `docker ps`
- Check Kafka is listening on port 9092: `docker logs kafka-broker`

### Topic Already Exists

**Error: "Topic already exists"**
- This is fine, topics persist
- Or delete and recreate: `kafka-topics --delete --topic <name> --bootstrap-server localhost:9092`

### OpenAI API Errors

**Error: "OPENAI_API_KEY not set"**
- Set environment variable: `export OPENAI_API_KEY="your-key"`
- Verify: `echo $OPENAI_API_KEY`

### Consumer Not Receiving Messages

- Check consumer group: Messages are distributed among consumers in same group
- Reset offsets: `kafka-consumer-groups --bootstrap-server localhost:9092 --group <group-id> --reset-offsets --to-earliest --topic <topic> --execute`

---

## Concepts Covered

### Part 1
- **Kafka RPC Pattern**: Request-response over message queues
- **Correlation IDs**: Matching requests to responses
- **Microservices**: Decoupled service architecture
- **CRUD Operations**: Create, Read, Update, Delete
- **Message Serialization**: JSON encoding/decoding

### Part 2
- **Multi-Agent Systems**: Autonomous agents working together
- **Pipeline Architecture**: Sequential processing
- **LangChain Integration**: LLM framework usage
- **Agent Communication**: Message-based coordination
- **Quality Assurance**: Review and approval workflow

---

## Screenshots for Submission

### Part 1 Screenshots:
1. Docker containers running (`docker ps`)
2. Consumer service started
3. Demo execution - Part 1 (CREATE operations)
4. Demo execution - Part 2 (GET, UPDATE, DELETE)
5. Demo execution - Part 3 (LIST and error handling)

### Part 2 Screenshots:
1. All 3 agents running in separate terminals
2. Question sent to inbox
3. Messages flowing through topics (tasks, drafts)
4. Final approved answer in `final` topic

---

## Additional Resources

- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [LangChain Documentation](https://python.langchain.com/)
- [Kafka Node.js Client](https://github.com/SOHU-Co/kafka-node)
- [Kafka Python Client](https://kafka-python.readthedocs.io/)

---

## Notes

- **In-Memory Storage**: Part 1 uses in-memory storage (resets on restart)
- **API Costs**: Part 2 uses OpenAI API (costs apply per request)
- **Concurrency**: Multiple consumers can process messages in parallel
- **Persistence**: Kafka topics persist messages (survive restarts)

---

## Author

Homework 8 Implementation
Distributed Systems Course
