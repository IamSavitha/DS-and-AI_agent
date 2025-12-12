# 📚 HOMEWORK 8: COMPREHENSIVE CONCEPT EXPLANATION

## Table of Contents
1. [Overview](#overview)
2. [Part 1: Kafka RPC User Management Microservice](#part-1-kafka-rpc-user-management-microservice)
3. [Part 2: Multi-Agent System with Kafka + LangChain](#part-2-multi-agent-system-with-kafka--langchain)
4. [Core Concepts](#core-concepts)
5. [Code Walkthrough - Part 1](#code-walkthrough---part-1)
6. [Code Walkthrough - Part 2](#code-walkthrough---part-2)
7. [Architecture Diagrams](#architecture-diagrams)
8. [Key Technologies](#key-technologies)

---

## Overview

Homework 8 consists of two parts that demonstrate advanced distributed systems concepts:

**Part 1**: Implements a **User Management Microservice** using **Kafka RPC (Remote Procedure Call)** pattern, demonstrating how microservices communicate asynchronously via message queues.

**Part 2**: Builds a **3-Agent Multi-Agent System** where agents communicate through Kafka topics, using LangChain and OpenAI to process questions through a pipeline: Planner → Writer → Reviewer.

### Key Technologies:
- **Apache Kafka**: Distributed event streaming platform
- **Kafka RPC Pattern**: Request-response pattern over Kafka
- **Node.js**: JavaScript runtime for Part 1
- **Python**: For Part 2 agent system
- **LangChain**: Framework for building LLM applications
- **OpenAI GPT**: Large language model for agent intelligence

---

## Part 1: Kafka RPC User Management Microservice

### Architecture Overview

```
┌─────────────┐         Kafka Topics          ┌─────────────┐
│   Client    │ ────► request_topic ────► │  Consumer   │
│  (Demo)     │                              │  (Service)  │
│             │ ◄──── response_topic ◄──── │             │
└─────────────┘                              └─────────────┘
```

### How Kafka RPC Works

1. **Client sends request** → `request_topic` with correlation ID
2. **Consumer processes** → Business logic execution
3. **Consumer sends response** → `response_topic` with same correlation ID
4. **Client receives response** → Matches correlation ID to callback

---

## Part 2: Multi-Agent System with Kafka + LangChain

### Architecture Overview

```
User Question
     │
     ▼
┌─────────┐
│ inbox   │ ────► Planner Agent ────► ┌─────────┐
└─────────┘                              │ tasks   │ ────► Writer Agent ────► ┌─────────┐
                                         └─────────┘                           │ drafts  │ ────► Reviewer Agent ────► ┌─────────┐
                                                                                └─────────┘                              │ final   │
                                                                                                                         └─────────┘
```

### Agent Pipeline Flow

1. **User** → Sends question to `inbox` topic
2. **Planner Agent** → Reads `inbox`, creates plan, sends to `tasks`
3. **Writer Agent** → Reads `tasks`, writes draft, sends to `drafts`
4. **Reviewer Agent** → Reads `drafts`, reviews, sends approved answer to `final`

---

## Core Concepts

### 1. Apache Kafka

**What is Kafka?**
Apache Kafka is a distributed event streaming platform that enables:
- **Publish-Subscribe Messaging**: Producers publish messages, consumers subscribe
- **Message Queuing**: Messages are stored in topics (like queues)
- **Distributed Processing**: Multiple consumers can process messages in parallel
- **Fault Tolerance**: Messages are replicated across brokers

**Key Kafka Concepts:**

#### Topics
- **Topic**: A category/feed name to which messages are published
- **Partition**: Topics are divided into partitions for parallelism
- **Replication Factor**: Number of copies of data across brokers

#### Producers and Consumers
- **Producer**: Publishes messages to topics
- **Consumer**: Subscribes to topics and processes messages
- **Consumer Group**: Multiple consumers working together to process messages

#### Message Structure
```javascript
{
  topic: "request_topic",
  partition: 0,
  offset: 12345,
  value: { /* message data */ },
  key: "correlation-id"
}
```

### 2. Kafka RPC Pattern

**RPC (Remote Procedure Call)** over Kafka enables synchronous-like communication over asynchronous messaging.

**How it works:**
1. Client generates unique **correlation ID**
2. Client sends request with correlation ID to request topic
3. Client sets up consumer for response topic
4. Server processes request and sends response with same correlation ID
5. Client matches correlation ID and invokes callback

**Benefits:**
- Decouples client and server
- Enables horizontal scaling
- Provides fault tolerance
- Supports multiple concurrent requests

### 3. Message Queues vs. Direct Calls

**Direct HTTP/REST Calls:**
```
Client ──HTTP──► Server
         (synchronous, blocking)
```

**Message Queue (Kafka):**
```
Client ──► Queue ──► Server
         (asynchronous, non-blocking)
```

**Advantages of Message Queues:**
- **Decoupling**: Client and server don't need to be available simultaneously
- **Scalability**: Multiple workers can process messages
- **Reliability**: Messages persist if server is down
- **Load Balancing**: Messages distributed across workers

### 4. Multi-Agent Systems

**What are Multi-Agent Systems?**
Systems where multiple autonomous agents work together to solve complex problems. Each agent:
- Has specific capabilities
- Communicates via messages
- Operates independently
- Can process tasks in parallel

**Agent Communication Patterns:**
- **Pipeline**: Agents process in sequence (like our system)
- **Broadcast**: One agent sends to many
- **Request-Response**: One-to-one communication
- **Pub-Sub**: Many-to-many communication

### 5. LangChain and LLM Integration

**LangChain** is a framework for building applications with LLMs:
- **Abstraction**: Simplifies LLM interactions
- **Chaining**: Combines multiple LLM calls
- **Memory**: Maintains conversation context
- **Tools**: Integrates external tools with LLMs

**LLM Agents:**
- **Planning Agent**: Breaks down complex tasks
- **Execution Agent**: Performs specific actions
- **Review Agent**: Validates and improves outputs

---

## Code Walkthrough - Part 1

### File: `consumer.js` - User Management Service

#### Lines 1-19: Imports and Configuration

```javascript
const kafka = require("kafka-node");
const crypto = require("crypto");
```

**Explanation:**
- `kafka-node`: Node.js client library for Kafka
- `crypto`: Node.js built-in module for generating unique IDs

#### Lines 8-19: Kafka Client Setup

```javascript
const client = new kafka.KafkaClient({ kafkaHost: "localhost:9092" });
const consumer = new kafka.Consumer(
  client,
  [{ topic: "request_topic", partition: 0 }],
  { autoCommit: true }
);
const producer = new kafka.Producer(client);
```

**Line-by-Line:**
- **Line 9**: Creates Kafka client connection to broker at localhost:9092
- **Line 12-16**: Creates consumer that:
  - Listens to `request_topic`
  - Reads from partition 0
  - Auto-commits offsets (marks messages as processed)
- **Line 19**: Creates producer for sending responses

**Concepts:**
- **Bootstrap Servers**: Initial Kafka broker addresses
- **Partition**: Logical division of topic for parallelism
- **Auto Commit**: Automatically marks messages as processed

#### Lines 21-35: Event Handlers

```javascript
producer.on("ready", () => {
  console.log("✓ Producer is ready");
});

consumer.on("ready", () => {
  console.log("✓ Consumer is ready and listening on 'request_topic'");
});
```

**Explanation:**
- Event-driven architecture: Kafka clients emit events
- `ready` event: Fired when connection is established
- `error` event: Handles connection/processing errors

#### Lines 40-110: Message Processing

```javascript
consumer.on("message", async function (message) {
  const payload = JSON.parse(message.value);
  const { correlationId, replyTo, data, timestamp } = payload;
  
  const processedResult = processRequest(data);
  
  const responsePayload = [{
    topic: replyTo,
    messages: JSON.stringify({
      correlationId: correlationId,
      data: processedResult,
      error: null
    })
  }];
  
  producer.send(responsePayload, callback);
});
```

**Line-by-Line:**
- **Line 40**: Listens for incoming messages
- **Line 46**: Parses JSON message payload
- **Line 47**: Extracts correlation ID (for matching request/response)
- **Line 59**: Processes business logic
- **Line 62-70**: Prepares response with same correlation ID
- **Line 76**: Sends response to reply topic

**Key Concepts:**
- **Correlation ID**: Unique identifier matching request to response
- **Reply-To Pattern**: Server responds to topic specified in request
- **Error Handling**: Try-catch ensures errors are sent back to client

#### Lines 112-140: User Storage

```javascript
const users = new Map();

function generateUserId() {
  return crypto.randomBytes(16).toString("hex");
}
```

**Explanation:**
- **Map**: JavaScript data structure for O(1) lookups
- **In-Memory Storage**: Fast but not persistent (resets on restart)
- **UUID Generation**: Creates unique 32-character hex ID

#### Lines 142-155: Validation Functions

```javascript
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function validateUserData(data) {
  const errors = [];
  if (data.name && typeof data.name !== "string") {
    errors.push("Name must be a non-empty string");
  }
  // ... more validation
  return errors;
}
```

**Concepts:**
- **Input Validation**: Prevents invalid data from entering system
- **Email Regex**: Pattern matching for email format
- **Error Collection**: Collects all validation errors before returning

#### Lines 157-180: CREATE_USER Operation

```javascript
function createUser(data) {
  const { name, email, age } = data;
  
  // Validate required fields
  if (!name || !email || age === undefined) {
    return { success: false, error: "Missing required fields" };
  }
  
  // Check if email exists
  for (const [userId, user] of users.entries()) {
    if (user.email === email) {
      return { success: false, error: "Email already exists" };
    }
  }
  
  // Create user
  const userId = generateUserId();
  const user = { userId, name, email, age };
  users.set(userId, user);
  
  return { success: true, userId, message: "User created" };
}
```

**Line-by-Line:**
- **Line 159**: Destructures input data
- **Line 162-165**: Validates required fields
- **Line 168-172**: Checks for duplicate email (data integrity)
- **Line 175**: Generates unique ID
- **Line 176**: Creates user object
- **Line 177**: Stores in Map
- **Line 179**: Returns success response

**Concepts:**
- **CRUD Operations**: Create, Read, Update, Delete
- **Data Integrity**: Prevents duplicate emails
- **Idempotency**: Same input produces same output

#### Lines 182-205: GET_USER Operation

```javascript
function getUser(data) {
  const { userId } = data;
  const user = users.get(userId);
  
  if (!user) {
    return { success: false, error: "User not found" };
  }
  
  return { success: true, user };
}
```

**Explanation:**
- **O(1) Lookup**: Map.get() is constant time
- **Error Handling**: Returns error if user doesn't exist
- **Data Sanitization**: Returns only necessary fields

#### Lines 207-250: UPDATE_USER Operation

```javascript
function updateUser(data) {
  const { userId, updates } = data;
  const user = users.get(userId);
  
  if (!user) {
    return { success: false, error: "User not found" };
  }
  
  // Apply updates
  if (updates.name !== undefined) {
    user.name = updates.name.trim();
  }
  if (updates.email !== undefined) {
    user.email = updates.email.trim().toLowerCase();
  }
  if (updates.age !== undefined) {
    user.age = Number(updates.age);
  }
  
  users.set(userId, user);
  return { success: true, user };
}
```

**Concepts:**
- **Partial Updates**: Only updates provided fields
- **Data Normalization**: Trims whitespace, lowercases email
- **Type Coercion**: Converts age to number

#### Lines 252-275: DELETE_USER Operation

```javascript
function deleteUser(data) {
  const { userId } = data;
  const user = users.get(userId);
  
  if (!user) {
    return { success: false, error: "User not found" };
  }
  
  users.delete(userId);
  return { success: true, message: "User deleted" };
}
```

**Explanation:**
- **Soft Delete**: Could mark as deleted instead of removing
- **Hard Delete**: Actually removes from storage (current implementation)

#### Lines 277-295: LIST_USERS Operation

```javascript
function listUsers() {
  const userList = Array.from(users.values()).map(user => ({
    userId: user.userId,
    name: user.name,
    email: user.email,
    age: user.age
  }));
  
  return {
    success: true,
    users: userList,
    count: userList.length
  };
}
```

**Concepts:**
- **Data Transformation**: Maps internal structure to API response
- **Pagination**: Could add limit/offset for large datasets
- **Projection**: Returns only necessary fields

### File: `rpc.js` - RPC Implementation

#### Lines 10-15: RPC Constructor

```javascript
function KafkaRPC() {
  this.connection = connection;
  this.requests = {}; // Store pending requests
  this.responseQueueReady = false;
  this.producer = this.connection.getProducer();
}
```

**Explanation:**
- **Singleton Pattern**: Single producer instance
- **Request Storage**: Maps correlation IDs to callbacks
- **Lazy Initialization**: Response queue set up on first request

#### Lines 23-76: makeRequest Method

```javascript
KafkaRPC.prototype.makeRequest = function (topicName, content, callback) {
  const correlationId = crypto.randomBytes(16).toString("hex");
  
  const timeoutId = setTimeout(() => {
    callback(new Error(`Request timeout: ${correlationId}`), null);
    delete self.requests[corrId];
  }, TIMEOUT);
  
  self.requests[correlationId] = {
    callback: callback,
    timeout: timeoutId
  };
  
  const payload = [{
    topic: topicName,
    messages: JSON.stringify({
      correlationId: correlationId,
      replyTo: "response_topic",
      data: content
    })
  }];
  
  self.producer.send(payload, callback);
};
```

**Line-by-Line:**
- **Line 27**: Generates unique correlation ID
- **Line 30-35**: Sets timeout (prevents hanging requests)
- **Line 41-44**: Stores request with callback
- **Line 50-58**: Creates message with correlation ID
- **Line 65**: Sends to Kafka topic

**Key Concepts:**
- **Correlation ID**: Links request to response
- **Timeout Handling**: Prevents indefinite waiting
- **Callback Pattern**: Async JavaScript pattern

#### Lines 81-131: setupResponseQueue Method

```javascript
KafkaRPC.prototype.setupResponseQueue = function (next) {
  if (this.responseQueueReady) {
    return next();
  }
  
  const consumer = self.connection.getConsumer("response_topic");
  
  consumer.on("message", function (message) {
    const response = JSON.parse(message.value);
    const correlationId = response.correlationId;
    
    if (correlationId in self.requests) {
      const entry = self.requests[correlationId];
      clearTimeout(entry.timeout);
      delete self.requests[correlationId];
      
      if (response.error) {
        entry.callback(new Error(response.error), null);
      } else {
        entry.callback(null, response.data);
      }
    }
  });
  
  self.responseQueueReady = true;
  return next();
};
```

**Explanation:**
- **Lazy Initialization**: Sets up consumer only once
- **Message Matching**: Finds request by correlation ID
- **Cleanup**: Removes timeout and request entry
- **Error Propagation**: Passes errors to original callback

### File: `homework-demo.js` - Demo Script

#### Lines 16-39: CREATE_USER Operations

```javascript
function createUser1() {
  client.makeRequest(
    "request_topic",
    {
      operation: "CREATE_USER",
      name: "Alice Johnson",
      email: "alice.johnson@example.com",
      age: 28
    },
    function (err, response) {
      if (response.success) {
        global.userId1 = response.userId;
        setTimeout(createUser2, 1000);
      }
    }
  );
}
```

**Concepts:**
- **Sequential Execution**: Each operation waits for previous
- **State Management**: Stores user IDs for later operations
- **Error Handling**: Checks for errors before proceeding

---

## Code Walkthrough - Part 2

### File: `planner.py` - Planning Agent

#### Lines 1-12: Imports and Configuration

```python
import json
import os
from kafka import KafkaConsumer, KafkaProducer
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
```

**Explanation:**
- `kafka-python`: Python Kafka client
- `langchain_openai`: LangChain integration with OpenAI
- `langchain_core.messages`: Message types for LLM

#### Lines 14-17: Kafka Configuration

```python
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
INBOX_TOPIC = 'inbox'
TASKS_TOPIC = 'tasks'
```

**Concepts:**
- **Topic Names**: Descriptive names for message categories
- **Bootstrap Servers**: Kafka broker addresses

#### Lines 19-26: LLM Initialization

```python
api_key = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=api_key
)
```

**Line-by-Line:**
- **Line 20**: Gets API key from environment variable
- **Line 21-25**: Initializes LangChain ChatOpenAI:
  - `model`: GPT-4o-mini (cost-effective)
  - `temperature`: 0.7 (balanced creativity/consistency)
  - `api_key`: Authentication

**Concepts:**
- **Temperature**: Controls randomness (0=deterministic, 1=creative)
- **Model Selection**: Trade-off between cost and quality

#### Lines 28-38: Kafka Consumer Setup

```python
consumer = KafkaConsumer(
    INBOX_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='planner-group',
    auto_offset_reset='earliest',
    enable_auto_commit=True
)
```

**Explanation:**
- **value_deserializer**: Converts bytes to JSON
- **group_id**: Consumer group for load balancing
- **auto_offset_reset**: 'earliest' reads from beginning
- **enable_auto_commit**: Automatically marks messages as processed

#### Lines 40-70: create_plan Function

```python
def create_plan(question):
    system_prompt = """You are a Planning Agent..."""
    user_prompt = f"Create a plan for answering this question: {question}"
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    
    response = llm.invoke(messages)
    plan_data = json.loads(response.content)
    return plan_data
```

**Line-by-Line:**
- **Line 41**: System prompt defines agent role
- **Line 42**: User prompt contains the question
- **Line 44-47**: Creates message array (system + user)
- **Line 49**: Invokes LLM (synchronous call)
- **Line 50**: Parses JSON response

**Concepts:**
- **System Prompt**: Sets agent behavior and constraints
- **User Prompt**: Contains actual task/question
- **Message Format**: LangChain message structure
- **JSON Parsing**: Extracts structured data from LLM response

#### Lines 72-110: process_question Function

```python
def process_question(message):
    payload = message.value
    question_id = payload.get('question_id', 'unknown')
    question = payload.get('question', '')
    
    plan = create_plan(question)
    
    task_message = {
        'question_id': question_id,
        'original_question': question,
        'plan': plan,
        'created_by': 'planner',
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    producer.send(TASKS_TOPIC, value=task_message)
    producer.flush()
```

**Explanation:**
- **Line 74**: Extracts message payload
- **Line 75-76**: Gets question ID and text
- **Line 79**: Creates plan using LLM
- **Line 81-87**: Builds task message with metadata
- **Line 90**: Sends to tasks topic
- **Line 91**: Flushes to ensure delivery

**Key Concepts:**
- **Message Enrichment**: Adds metadata (timestamps, IDs)
- **Topic Routing**: Sends to next topic in pipeline
- **Producer Flush**: Ensures message is sent immediately

### File: `writer.py` - Writing Agent

#### Lines 40-70: write_answer Function

```python
def write_answer(question, plan):
    system_prompt = """You are a Writing Agent..."""
    
    plan_text = "Plan:\n"
    for step in plan['steps']:
        plan_text += f"- Step {step['step_number']}: {step['description']}\n"
    
    user_prompt = f"""Question: {question}
{plan_text}
Please write a comprehensive answer following this plan."""
    
    response = llm.invoke(messages)
    return response.content
```

**Concepts:**
- **Context Building**: Formats plan for LLM
- **Prompt Engineering**: Structures input for better output
- **Answer Generation**: LLM creates detailed response

### File: `reviewer.py` - Review Agent

#### Lines 40-85: review_draft Function

```python
def review_draft(question, draft_answer):
    system_prompt = """You are a Review Agent...
    Evaluate the draft answer based on:
    1. Does it answer the question?
    2. Is it clear and well-structured?
    3. Is it accurate?
    
    Return JSON with: status, quality_score, feedback"""
    
    response = llm.invoke(messages)
    review_data = json.loads(response.content)
    
    return review_data
```

**Explanation:**
- **Quality Assessment**: LLM evaluates answer quality
- **Structured Output**: Returns JSON with status and score
- **Approval Logic**: Determines if answer is ready

#### Lines 87-130: process_draft Function

```python
def process_draft(message):
    payload = message.value
    draft_answer = payload.get('draft_answer', '')
    
    review = review_draft(question, draft_answer)
    
    final_message = {
        'question_id': question_id,
        'answer': draft_answer,
        'review': review,
        'status': review.get('status', 'approved'),
        'quality_score': review.get('quality_score', 0)
    }
    
    producer.send(FINAL_TOPIC, value=final_message)
```

**Concepts:**
- **Review Integration**: Combines draft with review
- **Status Propagation**: Carries status through pipeline
- **Final Output**: Sends approved answer to final topic

### File: `send_question.py` - Question Sender

#### Lines 10-40: send_question Function

```python
def send_question(question):
    question_id = f"q_{int(time.time())}"
    
    message = {
        'question_id': question_id,
        'question': question,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'source': 'user'
    }
    
    producer.send(INBOX_TOPIC, value=message)
    producer.flush()
```

**Explanation:**
- **ID Generation**: Creates unique ID from timestamp
- **Message Structure**: Standardized format
- **Topic Publishing**: Sends to inbox to start pipeline

---

## Architecture Diagrams

### Part 1: Kafka RPC Flow

```
┌──────────┐
│  Client  │
│ (Demo)   │
└────┬─────┘
     │ 1. makeRequest()
     │    correlationId: "abc123"
     ▼
┌─────────────────┐
│ request_topic   │
└────┬────────────┘
     │ 2. Message consumed
     ▼
┌─────────────┐
│  Consumer   │
│  (Service)  │
│             │
│ processRequest()│
│ - CREATE_USER  │
│ - GET_USER     │
│ - UPDATE_USER  │
│ - DELETE_USER  │
│ - LIST_USERS   │
└────┬────────┘
     │ 3. Response
     │    correlationId: "abc123"
     ▼
┌─────────────────┐
│ response_topic  │
└────┬────────────┘
     │ 4. Response received
     ▼
┌──────────┐
│  Client  │
│ callback │
└──────────┘
```

### Part 2: Multi-Agent Pipeline

```
┌─────────────┐
│    User     │
└──────┬──────┘
       │ send_question.py
       │ "What is Kafka?"
       ▼
┌─────────────┐
│   inbox     │ ────┐
└─────────────┘     │
                     │ Consumer reads
                     ▼
              ┌──────────────┐
              │   Planner    │
              │    Agent     │
              │              │
              │ create_plan()│
              │ (LLM call)   │
              └──────┬───────┘
                     │ Producer sends
                     ▼
              ┌──────────────┐
              │    tasks     │ ────┐
              └──────────────┘     │
                                    │ Consumer reads
                                    ▼
                             ┌──────────────┐
                             │    Writer    │
                             │    Agent     │
                             │              │
                             │ write_answer()│
                             │ (LLM call)   │
                             └──────┬───────┘
                                    │ Producer sends
                                    ▼
                             ┌──────────────┐
                             │    drafts    │ ────┐
                             └──────────────┘     │
                                                  │ Consumer reads
                                                  ▼
                                           ┌──────────────┐
                                           │   Reviewer   │
                                           │    Agent     │
                                           │              │
                                           │ review_draft()│
                                           │ (LLM call)   │
                                           └──────┬───────┘
                                                  │ Producer sends
                                                  ▼
                                           ┌──────────────┐
                                           │    final     │
                                           │              │
                                           │ {            │
                                           │   "status":  │
                                           │   "approved",│
                                           │   "answer":  │
                                           │   "..."      │
                                           │ }            │
                                           └──────────────┘
```

---

## Key Technologies

### 1. Apache Kafka

**Why Kafka?**
- **High Throughput**: Millions of messages per second
- **Scalability**: Horizontal scaling by adding brokers
- **Durability**: Messages persisted to disk
- **Fault Tolerance**: Replication across brokers

**Kafka vs. Traditional Message Queues:**
- **RabbitMQ**: Better for simple queuing
- **Kafka**: Better for event streaming, high volume
- **Redis Pub/Sub**: In-memory, faster but less durable

### 2. RPC Pattern

**Synchronous RPC (HTTP):**
```javascript
const response = await fetch('/api/users', {
  method: 'POST',
  body: JSON.stringify(userData)
});
```

**Asynchronous RPC (Kafka):**
```javascript
client.makeRequest('request_topic', userData, (err, response) => {
  // Handle response
});
```

**Benefits:**
- Non-blocking: Client doesn't wait
- Decoupling: Services independent
- Scalability: Multiple workers

### 3. Multi-Agent Systems

**Agent Characteristics:**
- **Autonomous**: Operates independently
- **Reactive**: Responds to environment
- **Proactive**: Takes initiative
- **Social**: Communicates with other agents

**Our System:**
- **Planner**: Proactive (creates plans)
- **Writer**: Reactive (responds to plans)
- **Reviewer**: Proactive (validates quality)

### 4. LangChain

**What is LangChain?**
Framework that provides:
- **Abstraction**: Simplifies LLM calls
- **Chains**: Combines multiple operations
- **Memory**: Maintains context
- **Tools**: Integrates external APIs

**Example Chain:**
```
Question → Planner → Writer → Reviewer → Final Answer
```

### 5. LLM Integration

**OpenAI GPT Models:**
- **gpt-4o-mini**: Fast, cost-effective, good quality
- **gpt-4**: Higher quality, more expensive
- **Temperature**: Controls randomness

**Prompt Engineering:**
- **System Prompt**: Defines agent role
- **User Prompt**: Contains task
- **Few-Shot Learning**: Examples in prompt
- **Chain-of-Thought**: Step-by-step reasoning

---

## Running the Homework

### Part 1: User Management Service

1. **Start Kafka:**
```bash
docker-compose up -d
```

2. **Setup Topics:**
```bash
node setup-topics.js
```

3. **Start Consumer:**
```bash
npm run start:consumer
```

4. **Run Demo:**
```bash
node homework-demo.js
```

### Part 2: Multi-Agent System

1. **Create Topics:**
```bash
kafka-topics --create --topic inbox --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
kafka-topics --create --topic tasks --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
kafka-topics --create --topic drafts --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
kafka-topics --create --topic final --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
```

2. **Start Agents (in separate terminals):**
```bash
# Terminal 1
python planner.py

# Terminal 2
python writer.py

# Terminal 3
python reviewer.py
```

3. **Send Question:**
```bash
python send_question.py "What are the benefits of Kafka?"
```

4. **Check Final Topic:**
```bash
kafka-console-consumer --topic final --from-beginning --bootstrap-server localhost:9092
```

---

## Summary

**Part 1** demonstrates:
- Kafka RPC pattern for microservice communication
- CRUD operations via message queues
- Request-response correlation
- Error handling in distributed systems

**Part 2** demonstrates:
- Multi-agent system architecture
- Agent communication via Kafka topics
- LLM integration with LangChain
- Pipeline processing pattern
- Quality assurance through review

**Key Takeaways:**
1. **Message Queues** enable decoupled, scalable systems
2. **RPC over Kafka** provides synchronous-like interface over async messaging
3. **Multi-Agent Systems** break complex tasks into specialized agents
4. **LLMs** can be integrated into distributed systems for intelligent processing
5. **Kafka Topics** provide reliable message routing between components

---

## References

- Apache Kafka Documentation: https://kafka.apache.org/documentation/
- LangChain Documentation: https://python.langchain.com/
- Kafka RPC Pattern: https://kafka.apache.org/documentation/#design
- Multi-Agent Systems: Distributed AI concepts
- Lecture Slides: 07-DS.MQ.Kafka.Multi-Agent Systems.pptx.pdf
