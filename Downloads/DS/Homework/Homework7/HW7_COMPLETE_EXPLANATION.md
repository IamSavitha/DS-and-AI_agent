# Homework 7: JWT Authentication & Authorization - Complete Explanation

## Table of Contents
1. [Overview](#overview)
2. [Core Concepts](#core-concepts)
3. [File Structure](#file-structure)
4. [Line-by-Line Code Explanations](#line-by-line-code-explanations)
5. [Authentication Flow](#authentication-flow)
6. [Security Concepts](#security-concepts)
7. [Testing](#testing)

---

## Overview

This homework implements a **complete JWT (JSON Web Token) authentication and authorization system** using:
- **Express.js** - Web framework for Node.js
- **MongoDB with Mongoose** - NoSQL database and ODM
- **JWT** - Stateless authentication tokens
- **bcrypt** - Password hashing
- **Role-Based Access Control (RBAC)** - Admin vs User permissions

---

## Core Concepts

### 1. Authentication vs Authorization

**Authentication (Who are you?):**
- Verifies user identity (username/password)
- Answers: "Is this person who they claim to be?"
- Example: Login process

**Authorization (What can you do?):**
- Determines what resources a user can access
- Answers: "Does this authenticated user have permission?"
- Example: Admin-only routes

### 2. JWT (JSON Web Token)

**What is JWT?**
- A compact, URL-safe token format for securely transmitting information
- Contains three parts separated by dots: `header.payload.signature`
- Example: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG4iLCJyb2xlIjoiYWRtaW4ifQ.signature`

**JWT Structure:**
```
Header.Payload.Signature
```

1. **Header**: Algorithm and token type
   ```json
   {
     "alg": "HS256",
     "typ": "JWT"
   }
   ```

2. **Payload (Claims)**: User data (id, username, role)
   ```json
   {
     "id": "507f1f77bcf86cd799439011",
     "username": "john",
     "role": "admin",
     "iat": 1234567890,
     "exp": 1234571490
   }
   ```

3. **Signature**: Verifies token integrity
   ```
   HMACSHA256(
     base64UrlEncode(header) + "." + base64UrlEncode(payload),
     secret
   )
   ```

**Why JWT?**
- **Stateless**: Server doesn't need to store session data
- **Scalable**: Works across multiple servers
- **Self-contained**: All user info is in the token
- **Secure**: Cryptographically signed, can't be tampered with

### 3. Password Hashing with bcrypt

**Why Hash Passwords?**
- Never store plain text passwords
- Even if database is compromised, passwords remain secure
- One-way function: can't reverse hash to get original password

**How bcrypt Works:**
1. Generates a random salt (unique per password)
2. Combines salt with password
3. Hashes multiple times (10 rounds = 2^10 iterations)
4. Stores: `$2b$10$salt22charactershashedpassword31characters`

**Example:**
```javascript
// Plain password: "mypassword123"
// Hashed: "$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy"
// Can never reverse this to get "mypassword123"
```

### 4. Middleware Pattern

**Express Middleware:**
- Functions that execute during request-response cycle
- Can modify request/response objects
- Can end request-response cycle
- Can call next middleware

**Middleware Chain:**
```
Request → Middleware 1 → Middleware 2 → Route Handler → Response
```

**Our Authentication Middleware:**
```javascript
verifyToken(req, res, next) {
  // 1. Extract token from header
  // 2. Verify token
  // 3. Attach user data to req.user
  // 4. Call next() to continue
}
```

### 5. Role-Based Access Control (RBAC)

**Concept:**
- Different users have different roles
- Roles determine permissions
- Example: Admin can access admin routes, regular users cannot

**Implementation:**
```javascript
if (req.user.role !== 'admin') {
  return res.status(403).json({ message: "Access Denied" });
}
```

---

## File Structure

```
Homework7/
├── server.js              # Main Express server
├── authRoutes.js          # Authentication routes (register, login, protected)
├── middleware/
│   └── auth.js           # JWT verification middleware
├── models/
│   └── User.js           # Mongoose User model
├── auth.test.js          # Test suite
├── package.json           # Dependencies
└── env.example           # Environment variables template
```

---

## Line-by-Line Code Explanations

### File: `server.js`

```javascript
require('dotenv').config();
```
**Concept**: Environment Variables
- Loads variables from `.env` file into `process.env`
- Keeps secrets (JWT_SECRET, DB passwords) out of code
- **Security Best Practice**: Never commit `.env` to git

```javascript
const express = require('express');
```
**Concept**: Express Framework
- Web application framework for Node.js
- Simplifies HTTP server creation
- Provides routing, middleware, templating

```javascript
const mongoose = require('mongoose');
```
**Concept**: Mongoose ODM
- Object Document Mapper for MongoDB
- Provides schema validation, models, queries
- Converts JavaScript objects ↔ MongoDB documents

```javascript
const app = express();
```
**Concept**: Express Application Instance
- Creates Express application
- `app` object handles HTTP requests/responses
- Can attach middleware and routes

```javascript
app.use(cors());
```
**Concept**: CORS (Cross-Origin Resource Sharing)
- Allows frontend (different origin) to call backend API
- Without CORS, browsers block cross-origin requests
- **Example**: Frontend at `localhost:3000` calling API at `localhost:5000`

```javascript
app.use(express.json());
```
**Concept**: JSON Body Parser
- Parses incoming JSON request bodies
- Makes `req.body` available as JavaScript object
- **Example**: `POST /api/auth/login` with `{"username": "user"}` → `req.body.username = "user"`

```javascript
mongoose.connect(process.env.MONGODB_URI)
```
**Concept**: MongoDB Connection
- Connects to MongoDB database
- `MONGODB_URI`: Connection string (from .env)
- Returns a Promise (use `.then()` or `async/await`)

```javascript
app.use('/api/auth', require('./authRoutes'));
```
**Concept**: Route Mounting
- All routes in `authRoutes.js` are prefixed with `/api/auth`
- **Example**: Route `/login` in authRoutes.js becomes `/api/auth/login`

```javascript
module.exports = app;
```
**Concept**: Module Export for Testing
- Exports app (not server) for testing
- `supertest` needs the Express app, not the listening server
- Allows testing without starting actual server

---

### File: `models/User.js`

```javascript
const mongoose = require('mongoose');
```
**Concept**: Mongoose Import
- Required to create schemas and models

```javascript
const userSchema = new mongoose.Schema({...});
```
**Concept**: Schema Definition
- Defines structure, validation, and defaults for documents
- **MongoDB vs SQL**: MongoDB is schema-less, but Mongoose adds structure
- Schema acts as a contract for data shape

```javascript
username: {
    type: String,
    required: [true, 'Username is required'],
    unique: true,
    trim: true,
    minlength: [3, 'Username must be at least 3 characters'],
    maxlength: [30, 'Username cannot exceed 30 characters']
}
```
**Concept**: Schema Field Definition
- `type: String` - Field must be a string
- `required: [true, 'message']` - Field is mandatory
- `unique: true` - No duplicate usernames (creates index)
- `trim: true` - Removes whitespace
- `minlength/maxlength` - Length validation

```javascript
password: {
    type: String,
    required: [true, 'Password is required'],
    minlength: [6, 'Password must be at least 6 characters']
}
```
**Concept**: Password Storage
- Store hashed password, never plain text
- Validation ensures minimum security requirements
- Actual hashing happens in route handler (not schema)

```javascript
role: {
    type: String,
    enum: ['user', 'admin'],
    default: 'user'
}
```
**Concept**: Enum Validation
- Restricts values to predefined list
- `default: 'user'` - If role not provided, defaults to 'user'
- **RBAC**: Role determines permissions

```javascript
}, {
    timestamps: true
});
```
**Concept**: Schema Options
- `timestamps: true` automatically adds:
  - `createdAt` - When document was created
  - `updatedAt` - When document was last updated
- No need to manually track these fields

```javascript
module.exports = mongoose.model('User', userSchema);
```
**Concept**: Model Creation
- `mongoose.model()` creates a model from schema
- Model name 'User' → collection name 'users' (pluralized, lowercased)
- Model provides methods: `User.create()`, `User.findOne()`, etc.

---

### File: `authRoutes.js`

#### Registration Endpoint

```javascript
router.post('/register', async (req, res) => {
```
**Concept**: Express Router
- `router.post()` handles POST requests
- `async` - Allows `await` for asynchronous operations
- Route: `POST /api/auth/register`

```javascript
const { username, password, role } = req.body;
```
**Concept**: Destructuring Assignment
- Extracts `username`, `password`, `role` from request body
- Equivalent to: `const username = req.body.username;`

```javascript
if (!username || !password) {
    return res.status(400).json({ message: "Username and password are required." });
}
```
**Concept**: Input Validation
- Checks required fields before processing
- `400 Bad Request` - Client error (missing data)
- `return` stops execution (prevents further processing)

```javascript
let user = await User.findOne({ username });
```
**Concept**: MongoDB Query
- `User.findOne()` - Finds first document matching criteria
- `await` - Waits for database operation to complete
- Checks if username already exists

```javascript
if (user) {
    return res.status(409).json({ message: "User already exists." });
}
```
**Concept**: HTTP Status Codes
- `409 Conflict` - Resource already exists
- Prevents duplicate usernames

```javascript
const salt = await bcrypt.genSalt(10);
```
**Concept**: bcrypt Salt Generation
- `genSalt(10)` - Generates random salt with 10 rounds
- Salt ensures same password hashes differently
- **Security**: Prevents rainbow table attacks

```javascript
const hashedPassword = await bcrypt.hash(password, salt);
```
**Concept**: Password Hashing
- `bcrypt.hash()` - Hashes password with salt
- One-way function: cannot reverse
- Takes ~100ms (intentionally slow to prevent brute force)

```javascript
user = new User({ username, password: hashedPassword, role: role || 'user' });
```
**Concept**: Mongoose Document Creation
- `new User()` - Creates new document instance
- `role: role || 'user'` - Defaults to 'user' if role not provided
- Document not saved yet (in memory only)

```javascript
await user.save();
```
**Concept**: Database Persistence
- Saves document to MongoDB
- `await` - Waits for save operation
- Throws error if validation fails

```javascript
res.status(201).json({ message: "User registered successfully.", ... });
```
**Concept**: HTTP Response
- `201 Created` - Resource successfully created
- `.json()` - Sends JSON response
- Never return password in response (security)

#### Login Endpoint

```javascript
router.post('/login', async (req, res) => {
```
**Concept**: Login Route
- Route: `POST /api/auth/login`
- Authenticates user and returns JWT token

```javascript
const user = await User.findOne({ username });
```
**Concept**: User Lookup
- Finds user by username in database
- Returns `null` if user doesn't exist

```javascript
if (!user) {
    return res.status(401).json({ message: "Authentication failed: Invalid credentials." });
}
```
**Concept**: Authentication Failure
- `401 Unauthorized` - Authentication failed
- Generic message (don't reveal if username exists - security)

```javascript
const isMatch = await bcrypt.compare(password, user.password);
```
**Concept**: Password Verification
- `bcrypt.compare()` - Compares plain password with hash
- Returns `true` if match, `false` otherwise
- Handles salt automatically

```javascript
if (!isMatch) {
    return res.status(401).json({ message: "Authentication failed: Invalid credentials." });
}
```
**Concept**: Password Mismatch
- Same error message as user not found
- Prevents username enumeration attacks

```javascript
const payload = {
    id: user._id,
    username: user.username,
    role: user.role
};
```
**Concept**: JWT Payload (Claims)
- Data to embed in token
- `_id` - MongoDB document ID
- `username` - User identifier
- `role` - For authorization checks

```javascript
jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: process.env.TOKEN_EXPIRY }, (err, token) => {
```
**Concept**: JWT Token Generation
- `jwt.sign()` - Creates signed JWT token
- `payload` - Data to encode
- `JWT_SECRET` - Secret key for signing (must match verification)
- `expiresIn` - Token expiration time (e.g., "24h")
- Callback function receives token or error

```javascript
res.json({ message: "Login successful.", token: token, expiresIn: process.env.TOKEN_EXPIRY });
```
**Concept**: Token Response
- Returns JWT token to client
- Client stores token (localStorage, cookie, memory)
- Client sends token in subsequent requests

#### Protected Route

```javascript
router.get('/protected/admin-data', verifyToken, (req, res) => {
```
**Concept**: Protected Route with Middleware
- Route: `GET /api/auth/protected/admin-data`
- `verifyToken` - Middleware runs before route handler
- Middleware authenticates user, route handler authorizes

```javascript
if (req.user.role !== 'admin') {
    return res.status(403).json({ message: "Access Denied: Requires 'admin' role.", userRole: req.user.role });
}
```
**Concept**: Authorization Check
- `req.user` - Set by `verifyToken` middleware (contains decoded JWT payload)
- `403 Forbidden` - Authenticated but not authorized
- **Difference**: 401 = not authenticated, 403 = authenticated but no permission

```javascript
res.json({ message: "SUCCESS! You accessed the highly protected admin resource.", ... });
```
**Concept**: Authorized Access
- User has admin role, access granted
- Returns protected data

---

### File: `middleware/auth.js`

```javascript
const verifyToken = (req, res, next) => {
```
**Concept**: Express Middleware Function
- `req` - Request object
- `res` - Response object
- `next` - Function to call next middleware
- Middleware signature: `(req, res, next) => {}`

```javascript
const bearerHeader = req.headers['authorization'];
```
**Concept**: HTTP Authorization Header
- Standard header for authentication
- Format: `Authorization: Bearer <token>`
- `req.headers` - Object containing all HTTP headers

```javascript
if (typeof bearerHeader === 'undefined' || !bearerHeader.startsWith('Bearer ')) {
    return res.status(401).json({ message: "Unauthorized: Bearer token format required." });
}
```
**Concept**: Token Validation
- Checks if Authorization header exists
- Checks if it starts with "Bearer " (standard format)
- `401 Unauthorized` - Missing or malformed token

```javascript
const token = bearerHeader.split(' ')[1];
```
**Concept**: Token Extraction
- Splits "Bearer <token>" by space
- Takes second element (index 1) = token
- **Example**: "Bearer abc123" → "abc123"

```javascript
jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
```
**Concept**: JWT Verification
- `jwt.verify()` - Verifies token signature and expiration
- `JWT_SECRET` - Must match secret used to sign token
- Callback receives error or decoded payload

```javascript
if (err) {
    return res.status(403).json({ message: "Forbidden: Invalid or expired token.", errorName: err.name });
}
```
**Concept**: Token Verification Failure
- `403 Forbidden` - Token invalid, tampered, or expired
- `err.name` - Error type (e.g., "TokenExpiredError", "JsonWebTokenError")
- Different from 401: 401 = no token, 403 = bad token

```javascript
req.user = decoded;
```
**Concept**: Attaching User Data to Request
- `decoded` - JWT payload (id, username, role)
- Attaches to `req.user` for use in route handlers
- Available to all subsequent middleware and route handlers

```javascript
next();
```
**Concept**: Middleware Chain Continuation
- Calls next middleware/route handler
- Without `next()`, request hangs (never gets response)

---

## Authentication Flow

### 1. Registration Flow

```
Client                    Server                    Database
  |                         |                          |
  |--POST /register-------->|                          |
  |  {username, password}   |                          |
  |                         |--Check if exists-------->|
  |                         |<--User not found---------|
  |                         |                          |
  |                         |--Hash password           |
  |                         |                          |
  |                         |--Save user-------------->|
  |                         |<--User saved------------|
  |<--201 Created-----------|                          |
  |  {username, role}       |                          |
```

### 2. Login Flow

```
Client                    Server                    Database
  |                         |                          |
  |--POST /login----------->|                          |
  |  {username, password}   |                          |
  |                         |--Find user-------------->|
  |                         |<--User found------------|
  |                         |                          |
  |                         |--Compare password       |
  |                         |  (bcrypt.compare)        |
  |                         |                          |
  |                         |--Generate JWT token     |
  |                         |  (jwt.sign)             |
  |<--200 OK----------------|                          |
  |  {token, expiresIn}     |                          |
```

### 3. Protected Route Flow

```
Client                    Server
  |                         |
  |--GET /admin-data------->|
  |  Authorization:         |
  |  Bearer <token>         |
  |                         |--verifyToken middleware |
  |                         |  (extract & verify)     |
  |                         |                         |
  |                         |--Check role === 'admin' |
  |                         |                         |
  |<--200 OK----------------|
  |  {admin data}           |
```

---

## Security Concepts

### 1. Password Security

**Never Store Plain Passwords:**
```javascript
// ❌ BAD
password: "mypassword123"

// ✅ GOOD
password: "$2b$10$N9qo8uLOickgx2ZMRZoMye..."
```

**Why bcrypt?**
- Adaptive hashing (can increase rounds over time)
- Slow by design (prevents brute force)
- Includes salt automatically

### 2. JWT Security

**Secret Key:**
- Must be strong and random
- Never commit to git
- Different for each environment (dev, prod)

**Token Expiration:**
- Tokens should expire (e.g., 24 hours)
- Reduces risk if token is stolen
- User must re-authenticate

**HTTPS:**
- Always use HTTPS in production
- Prevents token interception
- Encrypts data in transit

### 3. Error Messages

**Generic Error Messages:**
```javascript
// ❌ BAD - Reveals if username exists
"Username not found" or "Password incorrect"

// ✅ GOOD - Generic message
"Authentication failed: Invalid credentials."
```

**Why?**
- Prevents username enumeration
- Attacker can't determine valid usernames
- Security through obscurity (not primary defense, but helps)

### 4. HTTP Status Codes

- **200 OK** - Request successful
- **201 Created** - Resource created
- **400 Bad Request** - Invalid input
- **401 Unauthorized** - Not authenticated (no token/invalid credentials)
- **403 Forbidden** - Authenticated but not authorized (wrong role)
- **409 Conflict** - Resource already exists
- **500 Internal Server Error** - Server error

---

## Testing

### Running Tests

```bash
npm test
```

### Test Structure

1. **Setup**: Creates admin and standard users
2. **Login Tests**: Verify token generation
3. **Authorization Tests**: Verify role-based access
4. **Security Tests**: Verify token validation

### Test Cases Covered

- ✅ Admin login returns token
- ✅ Standard user login returns token
- ✅ Invalid credentials return 401
- ✅ Admin can access admin route
- ✅ Standard user cannot access admin route (403)
- ✅ Missing token returns 401
- ✅ Invalid/tampered token returns 403

---

## Key Takeaways

1. **JWT enables stateless authentication** - No server-side sessions
2. **bcrypt secures passwords** - One-way hashing with salt
3. **Middleware pattern** - Reusable authentication logic
4. **RBAC** - Role-based permissions for authorization
5. **Security best practices** - Hash passwords, expire tokens, use HTTPS
6. **HTTP status codes** - Proper error responses
7. **MongoDB + Mongoose** - NoSQL database with schema validation

---

## References

- [JWT.io](https://jwt.io/) - JWT debugger and documentation
- [bcrypt Documentation](https://www.npmjs.com/package/bcrypt)
- [Express Middleware](https://expressjs.com/en/guide/using-middleware.html)
- [Mongoose Documentation](https://mongoosejs.com/docs/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

## Next Steps

1. Add refresh tokens for longer sessions
2. Implement password reset functionality
3. Add rate limiting to prevent brute force
4. Implement token blacklisting for logout
5. Add email verification
6. Implement 2FA (Two-Factor Authentication)
