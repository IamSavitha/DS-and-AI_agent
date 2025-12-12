# 📖 Key Terms Glossary - Simple One-Line Definitions

## Authentication & Authorization Terms

### **Authentication**
The process of verifying who a user is (proving identity), typically done through username and password.

### **Authorization**
The process of determining what resources or actions an authenticated user is allowed to access based on their permissions or role.

### **JWT (JSON Web Token)**
A compact, URL-safe token format that securely transmits information between parties, containing user identity and permissions encoded in a signed token.

### **Token**
A credential that represents a user's authenticated session, allowing them to access protected resources without re-entering credentials.

### **Bearer Token**
A type of authentication token sent in the HTTP Authorization header with the format "Bearer <token>", indicating the client should present this token to access resources.

### **Claims**
The data embedded inside a JWT token (like user ID, username, role) that represent information about the authenticated user.

### **Payload**
The data portion of a JWT token that contains the claims (user information) encoded in the token.

### **Signature**
A cryptographic hash in a JWT that verifies the token hasn't been tampered with and was issued by a trusted server.

### **Stateless Authentication**
An authentication method where the server doesn't store session information; all user data is contained in the token itself.

---

## Security & Password Terms

### **Password Hashing**
The process of converting a plain text password into a scrambled, irreversible string using a one-way mathematical function.

### **bcrypt**
A password hashing algorithm that automatically handles salting and is designed to be slow, making brute-force attacks difficult.

### **Salt**
A random string added to a password before hashing to ensure the same password produces different hashes, preventing rainbow table attacks.

### **Hash**
The output of a one-way function that converts input data (like a password) into a fixed-length string that cannot be reversed to get the original data.

### **Rainbow Table Attack**
A method where attackers use pre-computed hash tables to quickly look up passwords from their hashes, prevented by using salts.

### **Brute Force Attack**
An attack method where an attacker tries many password combinations to guess the correct one, made difficult by slow hashing algorithms like bcrypt.

### **Plain Text Password**
An unencrypted password stored as readable text, which is a security vulnerability and should never be stored in databases.

---

## Database Terms

### **MongoDB**
A NoSQL document database that stores data as flexible JSON-like documents instead of rigid tables.

### **Mongoose**
An Object Document Mapper (ODM) for MongoDB in Node.js that provides schema validation, models, and an easy way to interact with MongoDB.

### **ODM (Object Document Mapper)**
A tool that maps JavaScript objects to database documents, similar to how ORMs map objects to database tables in SQL databases.

### **Schema**
A structure definition that describes the shape, validation rules, and default values for documents in a MongoDB collection.

### **Model**
A Mongoose class that represents a collection in MongoDB and provides methods to create, read, update, and delete documents.

### **Document**
A single record in a MongoDB collection, similar to a row in a SQL table but stored as a JSON-like object.

### **Collection**
A group of documents in MongoDB, similar to a table in SQL databases.

### **Query**
A request to find, retrieve, or manipulate data in a database.

### **findOne()**
A Mongoose method that finds and returns the first document matching specified criteria, or null if none found.

### **save()**
A Mongoose method that persists a document (new or modified) to the MongoDB database.

---

## Middleware Terms

### **Middleware**
Functions that execute during the request-response cycle, processing requests before they reach route handlers or responses before they're sent.

### **Authentication Middleware**
Middleware that verifies a user's identity by checking and validating their authentication token before allowing access to protected routes.

### **next()**
A function in Express middleware that passes control to the next middleware function or route handler in the chain.

### **req.user**
A property attached to the request object by authentication middleware, containing the decoded user information from the JWT token.

---

## HTTP & Status Code Terms

### **401 Unauthorized**
An HTTP status code indicating the request lacks valid authentication credentials (no token or invalid credentials).

### **403 Forbidden**
An HTTP status code indicating the request is authenticated but the user doesn't have permission to access the requested resource.

### **400 Bad Request**
An HTTP status code indicating the server cannot process the request due to invalid or missing data in the request.

### **409 Conflict**
An HTTP status code indicating the request conflicts with the current state of the resource (like trying to create a duplicate username).

### **201 Created**
An HTTP status code indicating a new resource was successfully created on the server.

### **500 Internal Server Error**
An HTTP status code indicating the server encountered an unexpected error while processing the request.

### **Authorization Header**
An HTTP header used to send authentication credentials, typically in the format "Authorization: Bearer <token>".

---

## Express.js Terms

### **Router**
An Express component that groups related routes together and can be mounted to a specific path in the main application.

### **router.post()**
An Express Router method that defines what happens when a POST request is made to a specific route path.

### **router.get()**
An Express Router method that defines what happens when a GET request is made to a specific route path.

### **app.use()**
An Express method that mounts middleware or routers to a specific path, applying them to all requests matching that path.

### **res.status()**
An Express method that sets the HTTP status code for the response (like 200, 401, 403).

### **res.json()**
An Express method that sends a JSON response to the client with the appropriate Content-Type header.

### **req.body**
An object containing data sent in the request body (form data or JSON), made available by body-parser middleware.

### **req.headers**
An object containing all HTTP headers sent with the request, including the Authorization header.

---

## Role-Based Access Control (RBAC) Terms

### **Role-Based Access Control (RBAC)**
A security model where access permissions are assigned to users based on their role (like 'admin' or 'user') rather than individual permissions.

### **Role**
A category or label assigned to users that determines what resources and actions they can access in the system.

### **Admin Role**
A privileged role that grants access to administrative functions and protected resources that regular users cannot access.

### **User Role**
A standard role with limited permissions, typically the default role assigned to new users.

### **Permission**
The specific right or ability to perform an action or access a resource, often determined by a user's role.

---

## Environment & Configuration Terms

### **Environment Variables**
Configuration values stored outside the code (in .env files) that can change between different environments (development, production) without modifying code.

### **dotenv**
A Node.js package that loads environment variables from a .env file into process.env, keeping secrets out of source code.

### **process.env**
A Node.js global object that contains environment variables, accessible throughout the application.

### **JWT_SECRET**
A secret key used to sign and verify JWT tokens, which must be kept secure and never exposed in code or version control.

### **TOKEN_EXPIRY**
The duration for which a JWT token remains valid before it expires and requires the user to re-authenticate.

---

## JavaScript & Node.js Terms

### **async/await**
JavaScript syntax that allows writing asynchronous code in a synchronous-looking style, making it easier to handle promises.

### **Promise**
A JavaScript object representing the eventual completion (or failure) of an asynchronous operation, allowing you to handle results when they're ready.

### **await**
A JavaScript keyword that pauses execution until a Promise resolves, allowing you to work with asynchronous operations synchronously.

### **try/catch**
JavaScript error handling syntax that attempts to execute code in the try block and catches any errors that occur in the catch block.

### **Destructuring**
Extracting values from objects or arrays into variables: `const { username, password } = req.body`.

### **Module.exports**
A Node.js mechanism for exporting functions, objects, or values from a module so they can be imported in other files.

### **require()**
A Node.js function that imports/loads a module from another file or from node_modules.

---

## Testing Terms

### **Unit Test**
A test that verifies a single function or component works correctly in isolation.

### **Integration Test**
A test that verifies multiple components work together correctly, like testing the full authentication flow.

### **Test Suite**
A collection of related tests that verify different aspects of the application's functionality.

### **supertest**
A Node.js library that provides a high-level abstraction for testing HTTP endpoints, making it easy to test Express routes.

### **Mocha**
A JavaScript test framework that provides the structure and utilities for writing and running tests.

### **Chai**
A JavaScript assertion library that provides readable assertions for writing test expectations.

### **expect()**
A Chai assertion method used to write readable test expectations, like `expect(res.status).to.equal(200)`.

---

## API Terms

### **REST API**
An API that follows REST (Representational State Transfer) principles, using standard HTTP methods (GET, POST, PUT, DELETE) to perform operations.

### **Endpoint**
A specific URL path in an API that performs a particular action when accessed with a specific HTTP method.

### **Protected Route**
An API endpoint that requires authentication (and sometimes authorization) before allowing access to the resource.

### **Public Route**
An API endpoint that can be accessed without authentication, like registration or login endpoints.

### **Route Handler**
The function that executes when a specific route is accessed, containing the logic to process the request and send a response.

---

## CORS Terms

### **CORS (Cross-Origin Resource Sharing)**
A security mechanism that allows web pages to make requests to a different domain than the one serving the web page, controlled by HTTP headers.

### **Origin**
The combination of protocol (http/https), domain, and port that identifies where a web page is being served from.

### **Cross-Origin Request**
An HTTP request made from one origin (domain) to a different origin, which browsers restrict by default for security.

---

## Real-World Analogy

Think of JWT authentication like a secure building access system:

- **Authentication** = Proving your identity at the front desk (login with username/password)
- **JWT Token** = A temporary access badge with your photo and clearance level encoded on it
- **Authorization** = The security guard checking if your badge has the right clearance to enter a restricted area
- **Password Hashing** = Like storing your fingerprint instead of your actual password - can verify it's you, but can't reverse it to get your password
- **Salt** = A unique identifier added to your fingerprint scan, so even identical passwords look different in the database
- **Middleware (verifyToken)** = The security checkpoint that scans your badge before you can proceed
- **Role (admin/user)** = The clearance level on your badge (admin = all access, user = limited access)
- **Protected Route** = A restricted floor that requires badge scanning and proper clearance
- **Token Expiration** = Your badge expires after 24 hours, requiring you to get a new one
- **MongoDB** = The building's database of all employees and their information
- **Mongoose Schema** = The form template that defines what information must be on each employee record

---

## Quick Reference: Most Important Terms

1. **Authentication** = Verifying who you are (login)
2. **Authorization** = Checking what you're allowed to do (permissions)
3. **JWT** = A token containing your identity and permissions
4. **Password Hashing** = Converting passwords to irreversible scrambled strings
5. **bcrypt** = A secure password hashing algorithm
6. **Middleware** = Functions that process requests before routes
7. **Mongoose** = Tool for working with MongoDB in Node.js
8. **Schema** = Structure definition for database documents
9. **Role-Based Access Control** = Permissions based on user roles
10. **Bearer Token** = Token format sent in Authorization header
11. **401 Unauthorized** = Not authenticated (no/invalid token)
12. **403 Forbidden** = Authenticated but not authorized (wrong role)
13. **Salt** = Random data added to passwords before hashing
14. **Stateless** = Server doesn't store session data (all in token)
15. **Claims/Payload** = Data embedded in JWT token

---

## Security Best Practices Covered

### **Never Store Plain Text Passwords**
Always hash passwords using bcrypt before storing in the database.

### **Use Strong JWT Secrets**
Generate random, strong secrets for signing tokens and keep them in environment variables.

### **Set Token Expiration**
Always set expiration times on tokens to limit the damage if a token is stolen.

### **Generic Error Messages**
Don't reveal whether a username exists or if password is wrong - use generic "Invalid credentials" messages.

### **HTTPS in Production**
Always use HTTPS to encrypt data in transit, preventing token interception.

### **Validate Input**
Always validate and sanitize user input before processing to prevent attacks.

### **Environment Variables**
Keep secrets (JWT_SECRET, database passwords) in .env files, never in code.
