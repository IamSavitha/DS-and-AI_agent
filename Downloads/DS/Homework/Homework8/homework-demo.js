const KafkaClient = require("./client");

/**
 * Homework 8 - Part 1 Demo
 * Demonstrates all 5 User Management CRUD operations via Kafka RPC
 */

const client = new KafkaClient();

console.log("🚀 Homework 8 - Part 1: User Management Microservice Demo");
console.log("=".repeat(70) + "\n");

// Give producer time to connect
setTimeout(() => {
  runDemo();
}, 2000);

/**
 * Main demo function - runs all operations in sequence
 */
function runDemo() {
  console.log("\n" + "=".repeat(70));
  console.log("PART 1: CREATE USERS");
  console.log("=".repeat(70) + "\n");
  
  // Create 3 users sequentially
  createUser1();
}

/**
 * CREATE USER 1
 */
function createUser1() {
  console.log("📝 Creating User 1: Alice");
  
  client.makeRequest(
    "request_topic",
    {
      operation: "CREATE_USER",
      name: "Alice Johnson",
      email: "alice.johnson@example.com",
      age: 28
    },
    function (err, response) {
      if (err) {
        console.error("❌ Error:", err.message);
        return;
      }
      
      if (response.success) {
        console.log(`✅ User created successfully!`);
        console.log(`   User ID: ${response.userId}`);
        console.log(`   Name: ${response.user.name}`);
        console.log(`   Email: ${response.user.email}`);
        console.log(`   Age: ${response.user.age}\n`);
        
        // Store userId for later operations
        global.userId1 = response.userId;
        
        // Continue to create user 2
        setTimeout(createUser2, 1000);
      } else {
        console.error("❌ Failed:", response.error);
      }
    }
  );
}

/**
 * CREATE USER 2
 */
function createUser2() {
  console.log("📝 Creating User 2: Bob");
  
  client.makeRequest(
    "request_topic",
    {
      operation: "CREATE_USER",
      name: "Bob Smith",
      email: "bob.smith@example.com",
      age: 35
    },
    function (err, response) {
      if (err) {
        console.error("❌ Error:", err.message);
        return;
      }
      
      if (response.success) {
        console.log(`✅ User created successfully!`);
        console.log(`   User ID: ${response.userId}`);
        console.log(`   Name: ${response.user.name}`);
        console.log(`   Email: ${response.user.email}`);
        console.log(`   Age: ${response.user.age}\n`);
        
        global.userId2 = response.userId;
        setTimeout(createUser3, 1000);
      } else {
        console.error("❌ Failed:", response.error);
      }
    }
  );
}

/**
 * CREATE USER 3
 */
function createUser3() {
  console.log("📝 Creating User 3: Charlie");
  
  client.makeRequest(
    "request_topic",
    {
      operation: "CREATE_USER",
      name: "Charlie Brown",
      email: "charlie.brown@example.com",
      age: 42
    },
    function (err, response) {
      if (err) {
        console.error("❌ Error:", err.message);
        return;
      }
      
      if (response.success) {
        console.log(`✅ User created successfully!`);
        console.log(`   User ID: ${response.userId}`);
        console.log(`   Name: ${response.user.name}`);
        console.log(`   Email: ${response.user.email}`);
        console.log(`   Age: ${response.user.age}\n`);
        
        global.userId3 = response.userId;
        
        // After creating all users, list them
        setTimeout(() => {
          console.log("\n" + "=".repeat(70));
          console.log("PART 2: LIST ALL USERS (Initial State)");
          console.log("=".repeat(70) + "\n");
          listUsers1();
        }, 1000);
      } else {
        console.error("❌ Failed:", response.error);
      }
    }
  );
}

/**
 * LIST USERS - First time
 */
function listUsers1() {
  console.log("📋 Listing all users...");
  
  client.makeRequest(
    "request_topic",
    {
      operation: "LIST_USERS"
    },
    function (err, response) {
      if (err) {
        console.error("❌ Error:", err.message);
        return;
      }
      
      if (response.success) {
        console.log(`✅ Found ${response.count} users:\n`);
        response.users.forEach((user, index) => {
          console.log(`   ${index + 1}. ${user.name} (${user.userId})`);
          console.log(`      Email: ${user.email}, Age: ${user.age}\n`);
        });
        
        // Continue to GET operation
        setTimeout(() => {
          console.log("\n" + "=".repeat(70));
          console.log("PART 3: GET USER BY ID");
          console.log("=".repeat(70) + "\n");
          getUser();
        }, 1000);
      } else {
        console.error("❌ Failed:", response.error);
      }
    }
  );
}

/**
 * GET USER
 */
function getUser() {
  console.log(`🔍 Retrieving user with ID: ${global.userId1}`);
  
  client.makeRequest(
    "request_topic",
    {
      operation: "GET_USER",
      userId: global.userId1
    },
    function (err, response) {
      if (err) {
        console.error("❌ Error:", err.message);
        return;
      }
      
      if (response.success) {
        console.log(`✅ User retrieved successfully!`);
        console.log(`   User ID: ${response.user.userId}`);
        console.log(`   Name: ${response.user.name}`);
        console.log(`   Email: ${response.user.email}`);
        console.log(`   Age: ${response.user.age}\n`);
        
        // Continue to UPDATE operation
        setTimeout(() => {
          console.log("\n" + "=".repeat(70));
          console.log("PART 4: UPDATE USER");
          console.log("=".repeat(70) + "\n");
          updateUser();
        }, 1000);
      } else {
        console.error("❌ Failed:", response.error);
      }
    }
  );
}

/**
 * UPDATE USER
 */
function updateUser() {
  console.log(`✏️  Updating user ${global.userId2}...`);
  console.log("   Changes: age from 35 to 36, email update");
  
  client.makeRequest(
    "request_topic",
    {
      operation: "UPDATE_USER",
      userId: global.userId2,
      updates: {
        age: 36,
        email: "bob.smith.updated@example.com"
      }
    },
    function (err, response) {
      if (err) {
        console.error("❌ Error:", err.message);
        return;
      }
      
      if (response.success) {
        console.log(`✅ User updated successfully!`);
        console.log(`   User ID: ${response.user.userId}`);
        console.log(`   Name: ${response.user.name}`);
        console.log(`   Email: ${response.user.email} (updated)`);
        console.log(`   Age: ${response.user.age} (updated)\n`);
        
        // Continue to DELETE operation
        setTimeout(() => {
          console.log("\n" + "=".repeat(70));
          console.log("PART 5: DELETE USER");
          console.log("=".repeat(70) + "\n");
          deleteUser();
        }, 1000);
      } else {
        console.error("❌ Failed:", response.error);
      }
    }
  );
}

/**
 * DELETE USER
 */
function deleteUser() {
  console.log(`🗑️  Deleting user ${global.userId3}...`);
  
  client.makeRequest(
    "request_topic",
    {
      operation: "DELETE_USER",
      userId: global.userId3
    },
    function (err, response) {
      if (err) {
        console.error("❌ Error:", err.message);
        return;
      }
      
      if (response.success) {
        console.log(`✅ User deleted successfully!`);
        console.log(`   Deleted User ID: ${response.deletedUser.userId}`);
        console.log(`   Deleted User Name: ${response.deletedUser.name}\n`);
        
        // List users again to show deletion
        setTimeout(() => {
          console.log("\n" + "=".repeat(70));
          console.log("PART 6: LIST USERS (After Deletion)");
          console.log("=".repeat(70) + "\n");
          listUsers2();
        }, 1000);
      } else {
        console.error("❌ Failed:", response.error);
      }
    }
  );
}

/**
 * LIST USERS - After deletion
 */
function listUsers2() {
  console.log("📋 Listing all users after deletion...");
  
  client.makeRequest(
    "request_topic",
    {
      operation: "LIST_USERS"
    },
    function (err, response) {
      if (err) {
        console.error("❌ Error:", err.message);
        return;
      }
      
      if (response.success) {
        console.log(`✅ Found ${response.count} users (1 deleted):\n`);
        response.users.forEach((user, index) => {
          console.log(`   ${index + 1}. ${user.name} (${user.userId})`);
          console.log(`      Email: ${user.email}, Age: ${user.age}\n`);
        });
        
        // Demonstrate error handling
        setTimeout(() => {
          console.log("\n" + "=".repeat(70));
          console.log("PART 7: ERROR HANDLING DEMONSTRATIONS");
          console.log("=".repeat(70) + "\n");
          demonstrateErrors();
        }, 1000);
      } else {
        console.error("❌ Failed:", response.error);
      }
    }
  );
}

/**
 * Demonstrate error handling
 */
function demonstrateErrors() {
  // Error 1: Get non-existent user
  console.log("❌ Error Demo 1: Getting non-existent user");
  client.makeRequest(
    "request_topic",
    {
      operation: "GET_USER",
      userId: "non-existent-id"
    },
    function (err, response) {
      if (err) {
        console.error("   Request error:", err.message);
      } else if (!response.success) {
        console.log(`   ✅ Error handled correctly: ${response.error}\n`);
      }
      
      // Error 2: Create user with invalid email
      setTimeout(() => {
        console.log("❌ Error Demo 2: Creating user with invalid email");
        client.makeRequest(
          "request_topic",
          {
            operation: "CREATE_USER",
            name: "Invalid User",
            email: "not-an-email",
            age: 25
          },
          function (err, response) {
            if (err) {
              console.error("   Request error:", err.message);
            } else if (!response.success) {
              console.log(`   ✅ Error handled correctly: ${response.error}\n`);
            }
            
            // Error 3: Invalid operation
            setTimeout(() => {
              console.log("❌ Error Demo 3: Invalid operation");
              client.makeRequest(
                "request_topic",
                {
                  operation: "INVALID_OPERATION"
                },
                function (err, response) {
                  if (err) {
                    console.error("   Request error:", err.message);
                  } else if (!response.success) {
                    console.log(`   ✅ Error handled correctly: ${response.error}\n`);
                  }
                  
                  // Complete
                  setTimeout(() => {
                    console.log("\n" + "=".repeat(70));
                    console.log("🎉 ALL DEMOS COMPLETED SUCCESSFULLY!");
                    console.log("=".repeat(70));
                    console.log("\n✅ Summary:");
                    console.log("   - Created 3 users");
                    console.log("   - Listed users (2 times)");
                    console.log("   - Retrieved user by ID");
                    console.log("   - Updated user information");
                    console.log("   - Deleted user");
                    console.log("   - Demonstrated error handling");
                    console.log("\n👋 Exiting demo...\n");
                    
                    setTimeout(() => {
                      process.exit(0);
                    }, 2000);
                  }, 1000);
                }
              );
            }, 1000);
          }
        );
      }, 1000);
    }
  );
}

// Handle errors
process.on("uncaughtException", (err) => {
  console.error("Uncaught Exception:", err);
  process.exit(1);
});

process.on("SIGINT", () => {
  console.log("\n\n👋 Demo interrupted by user");
  process.exit(0);
});
