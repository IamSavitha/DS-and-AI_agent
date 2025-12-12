const kafka = require("kafka-node");

/**
 * Kafka Consumer - Backend Service
 * Listens for requests, processes them, and sends responses
 */

// Kafka configuration
const client = new kafka.KafkaClient({ kafkaHost: "localhost:9092" });

// Consumer listens to incoming requests
const consumer = new kafka.Consumer(
  client,
  [{ topic: "request_topic", partition: 0 }],
  { autoCommit: true }
);

// Producer for sending responses
const producer = new kafka.Producer(client);

producer.on("ready", () => {
  console.log("✓ Producer is ready");
});

producer.on("error", (err) => {
  console.error("✗ Producer error:", err);
});

consumer.on("ready", () => {
  console.log("✓ Consumer is ready and listening on 'request_topic'");
});

consumer.on("error", (err) => {
  console.error("✗ Consumer error:", err);
});

/**
 * Process incoming messages
 */
consumer.on("message", async function (message) {
  console.log("\n" + "=".repeat(50));
  console.log("📨 Received message:");
  console.log("Raw value:", message.value);
  
  try {
    const payload = JSON.parse(message.value);
    const { correlationId, replyTo, data, timestamp } = payload;
    
    console.log("Correlation ID:", correlationId);
    console.log("Reply To:", replyTo);
    console.log("Request Data:", data);
    console.log("Request Time:", timestamp);
    
    // ============================================
    // TODO: PROCESS YOUR BUSINESS LOGIC HERE
    // ============================================
    
    // Example processing: Simulate some work
    const processedResult = processRequest(data);
    
    // Prepare response
    const responsePayload = [
      {
        topic: replyTo,
        messages: JSON.stringify({
          correlationId: correlationId,
          data: processedResult,
          error: null,
          processedAt: new Date().toISOString()
        }),
        partition: 0
      }
    ];
    
    // Send response back
    producer.send(responsePayload, (err, result) => {
      if (err) {
        console.error("✗ Error sending response:", err);
      } else {
        console.log("✓ Response sent successfully");
        console.log("=".repeat(50) + "\n");
      }
    });
    
  } catch (err) {
    console.error("✗ Error processing message:", err);
    
    // Try to send error response if possible
    try {
      const errorPayload = JSON.parse(message.value);
      const errorResponse = [
        {
          topic: errorPayload.replyTo || "response_topic",
          messages: JSON.stringify({
            correlationId: errorPayload.correlationId,
            data: null,
            error: err.message
          }),
          partition: 0
        }
      ];
      
      producer.send(errorResponse, (err) => {
        if (err) console.error("✗ Error sending error response:", err);
      });
    } catch (e) {
      console.error("✗ Could not send error response:", e);
    }
  }
});

// ============================================
// USER MANAGEMENT SERVICE - In-Memory Storage
// ============================================
const crypto = require("crypto");

// In-memory user storage (Map for O(1) lookups)
const users = new Map();

/**
 * Generate unique user ID
 */
function generateUserId() {
  return crypto.randomBytes(16).toString("hex");
}

/**
 * Validate email format
 */
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Validate user data
 */
function validateUserData(data) {
  const errors = [];
  
  if (data.name && typeof data.name !== "string" || data.name?.trim().length === 0) {
    errors.push("Name must be a non-empty string");
  }
  
  if (data.email && !isValidEmail(data.email)) {
    errors.push("Email must be a valid email address");
  }
  
  if (data.age !== undefined) {
    const age = Number(data.age);
    if (isNaN(age) || age <= 0 || !Number.isInteger(age)) {
      errors.push("Age must be a positive integer");
    }
  }
  
  return errors;
}

/**
 * User Management Service - Process CRUD operations
 */
function processRequest(data) {
  console.log("🔧 Processing request...");
  console.log("Operation:", data.operation);
  
  const { operation } = data;
  
  try {
    switch (operation) {
      case "CREATE_USER":
        return createUser(data);
      
      case "GET_USER":
        return getUser(data);
      
      case "UPDATE_USER":
        return updateUser(data);
      
      case "DELETE_USER":
        return deleteUser(data);
      
      case "LIST_USERS":
        return listUsers();
      
      default:
        return {
          success: false,
          error: `Unknown operation: ${operation}. Supported operations: CREATE_USER, GET_USER, UPDATE_USER, DELETE_USER, LIST_USERS`
        };
    }
  } catch (error) {
    return {
      success: false,
      error: error.message
    };
  }
}

/**
 * CREATE_USER - Create a new user
 * Input: { operation: "CREATE_USER", name: string, email: string, age: number }
 * Output: { success: true, userId: string, message: "User created" }
 */
function createUser(data) {
  const { name, email, age } = data;
  
  // Validate required fields
  if (!name || !email || age === undefined) {
    return {
      success: false,
      error: "Missing required fields: name, email, and age are required"
    };
  }
  
  // Validate data format
  const validationErrors = validateUserData({ name, email, age });
  if (validationErrors.length > 0) {
    return {
      success: false,
      error: validationErrors.join("; ")
    };
  }
  
  // Check if email already exists
  for (const [userId, user] of users.entries()) {
    if (user.email === email) {
      return {
        success: false,
        error: `User with email ${email} already exists (userId: ${userId})`
      };
    }
  }
  
  // Create new user
  const userId = generateUserId();
  const user = {
    userId,
    name: name.trim(),
    email: email.trim().toLowerCase(),
    age: Number(age),
    createdAt: new Date().toISOString()
  };
  
  users.set(userId, user);
  
  console.log(`✓ User created: ${userId} - ${name}`);
  
  return {
    success: true,
    userId: userId,
    message: "User created",
    user: user
  };
}

/**
 * GET_USER - Retrieve user by ID
 * Input: { operation: "GET_USER", userId: string }
 * Output: { success: true, user: {userId, name, email, age} }
 */
function getUser(data) {
  const { userId } = data;
  
  if (!userId) {
    return {
      success: false,
      error: "userId is required"
    };
  }
  
  const user = users.get(userId);
  
  if (!user) {
    return {
      success: false,
      error: `User with userId ${userId} not found`
    };
  }
  
  console.log(`✓ User retrieved: ${userId}`);
  
  return {
    success: true,
    user: {
      userId: user.userId,
      name: user.name,
      email: user.email,
      age: user.age
    }
  };
}

/**
 * UPDATE_USER - Update user information
 * Input: { operation: "UPDATE_USER", userId: string, updates: {name?, email?, age?} }
 * Output: { success: true, user: {updated user data} }
 */
function updateUser(data) {
  const { userId, updates } = data;
  
  if (!userId) {
    return {
      success: false,
      error: "userId is required"
    };
  }
  
  if (!updates || typeof updates !== "object") {
    return {
      success: false,
      error: "updates object is required"
    };
  }
  
  const user = users.get(userId);
  
  if (!user) {
    return {
      success: false,
      error: `User with userId ${userId} not found`
    };
  }
  
  // Validate updates
  const validationErrors = validateUserData(updates);
  if (validationErrors.length > 0) {
    return {
      success: false,
      error: validationErrors.join("; ")
    };
  }
  
  // Check if email is being updated and doesn't conflict
  if (updates.email && updates.email !== user.email) {
    for (const [otherUserId, otherUser] of users.entries()) {
      if (otherUserId !== userId && otherUser.email === updates.email.toLowerCase()) {
        return {
          success: false,
          error: `Email ${updates.email} is already in use by another user`
        };
      }
    }
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
  user.updatedAt = new Date().toISOString();
  
  users.set(userId, user);
  
  console.log(`✓ User updated: ${userId}`);
  
  return {
    success: true,
    user: {
      userId: user.userId,
      name: user.name,
      email: user.email,
      age: user.age
    }
  };
}

/**
 * DELETE_USER - Remove a user
 * Input: { operation: "DELETE_USER", userId: string }
 * Output: { success: true, message: "User deleted" }
 */
function deleteUser(data) {
  const { userId } = data;
  
  if (!userId) {
    return {
      success: false,
      error: "userId is required"
    };
  }
  
  const user = users.get(userId);
  
  if (!user) {
    return {
      success: false,
      error: `User with userId ${userId} not found`
    };
  }
  
  users.delete(userId);
  
  console.log(`✓ User deleted: ${userId} - ${user.name}`);
  
  return {
    success: true,
    message: "User deleted",
    deletedUser: {
      userId: user.userId,
      name: user.name
    }
  };
}

/**
 * LIST_USERS - Get all users
 * Input: { operation: "LIST_USERS" }
 * Output: { success: true, users: [...], count: number }
 */
function listUsers() {
  const userList = Array.from(users.values()).map(user => ({
    userId: user.userId,
    name: user.name,
    email: user.email,
    age: user.age
  }));
  
  console.log(`✓ Listed ${userList.length} users`);
  
  return {
    success: true,
    users: userList,
    count: userList.length
  };
}

// Graceful shutdown
process.on("SIGINT", () => {
  console.log("\n🛑 Shutting down consumer...");
  consumer.close(true, () => {
    process.exit(0);
  });
});

console.log("🚀 Kafka Consumer Service Started");
console.log("📡 Waiting for messages on 'request_topic'...");
console.log("Press Ctrl+C to stop\n");