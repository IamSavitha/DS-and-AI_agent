# Homework 3: Session-Based Authentication - Complete Explanation

## Table of Contents
1. [Overview](#overview)
2. [Key Concepts](#key-concepts)
3. [Architecture & Flow](#architecture--flow)
4. [Line-by-Line Code Analysis](#line-by-line-code-analysis)
5. [Security Considerations](#security-considerations)
6. [How to Run](#how-to-run)

---

## Overview

This homework implements **session-based authentication** using Express.js. Session-based authentication is a server-side authentication mechanism where the server maintains session state and identifies clients using session cookies.

### What is Session-Based Authentication?

Session-based authentication works as follows:
1. User submits credentials (username/password)
2. Server validates credentials
3. Server creates a session and stores it server-side
4. Server sends a session ID cookie to the client
5. Client includes this cookie in subsequent requests
6. Server uses the cookie to identify the session and authenticate the user

---

## Key Concepts

### 1. **HTTP Sessions**

**Definition:** A session is a way to store information about a user across multiple HTTP requests. Unlike cookies stored on the client, session data is stored on the server.

**Why Sessions?**
- HTTP is stateless - each request is independent
- Sessions allow us to maintain user state (logged in, user data, etc.)
- More secure than storing sensitive data in client-side cookies

**How it Works:**
```
Client                    Server
  |                         |
  |-- Login Request ------->|
  |                         | (Validate credentials)
  |                         | (Create session)
  |<-- Set-Cookie ---------| (Session ID: abc123)
  |                         |
  |-- Request + Cookie ---->|
  |                         | (Lookup session abc123)
  |                         | (Retrieve user data)
  |<-- Response ------------|
```

### 2. **express-session Middleware**

**Purpose:** Manages session creation, storage, and cookie handling in Express.js applications.

**Key Configuration Options:**
- `secret`: Used to sign the session cookie (prevents tampering)
- `resave`: Whether to save session even if unmodified
- `saveUninitialized`: Whether to create session before storing data
- `cookie`: Cookie configuration (secure, httpOnly, maxAge)

### 3. **Password Hashing with bcrypt**

**Why Hash Passwords?**
- Never store plain text passwords
- If database is compromised, attackers can't see actual passwords
- Hashing is one-way (can't reverse to get original password)

**How bcrypt Works:**
1. Takes plain text password
2. Adds random "salt" (prevents rainbow table attacks)
3. Hashes password + salt multiple times (salt rounds)
4. Stores hash in database

**Verification:**
- When user logs in, compare entered password with stored hash
- bcrypt handles salt extraction automatically

### 4. **EJS (Embedded JavaScript) Templates**

**Purpose:** Server-side templating engine that allows embedding JavaScript in HTML.

**Syntax:**
- `<% code %>` - Execute JavaScript (no output)
- `<%= expression %>` - Output expression value (HTML escaped)
- `<%- html %>` - Output raw HTML (not escaped)

### 5. **Express Router**

**Purpose:** Modular route handlers. Allows organizing routes into separate files.

**Benefits:**
- Code organization
- Reusability
- Separation of concerns

### 6. **Middleware**

**Definition:** Functions that execute during the request-response cycle.

**Types in this project:**
- **Body Parser:** Parses request bodies
- **Session:** Manages sessions
- **Authentication:** Protects routes
- **Error Handling:** Catches errors

---

## Architecture & Flow

### Request Flow Diagram

```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │
       │ HTTP Request
       ▼
┌─────────────────────────────────────┐
│         Express App (app.js)        │
│  ┌───────────────────────────────┐  │
│  │      Middleware Stack         │  │
│  │  1. Body Parser               │  │
│  │  2. Session Manager           │  │
│  │  3. Static Files              │  │
│  └───────────────────────────────┘  │
│                                      │
│  ┌───────────────────────────────┐  │
│  │         Routes                │  │
│  │  / → index.ejs                │  │
│  │  /auth/login → auth.js        │  │
│  │  /dashboard → Protected       │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
       │
       │ Session Lookup
       ▼
┌─────────────────────────────────────┐
│      Session Store (Memory)          │
│  Session ID: abc123                  │
│  Data: { user: { id: 1, ... } }     │
└─────────────────────────────────────┘
```

### Authentication Flow

```
1. User visits /auth/login
   ↓
2. Server renders login.ejs
   ↓
3. User submits form (POST /auth/login)
   ↓
4. Server receives username/password
   ↓
5. Server finds user in database
   ↓
6. Server compares password with hash (bcrypt)
   ↓
7. If match:
   - Create session
   - Store user data in session
   - Send session cookie to client
   - Redirect to /dashboard
   ↓
8. User makes request to /dashboard
   ↓
9. Server checks req.session.user
   ↓
10. If exists: Render dashboard
    If not: Redirect to /auth/login
```

---

## Line-by-Line Code Analysis

### File: `app.js`

```javascript
// Line 1-5: Import Dependencies
const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const path = require('path');
```

**Explanation:**
- `express`: Web framework for Node.js
- `express-session`: Session management middleware
- `body-parser`: Parses HTTP request bodies
- `path`: Node.js module for file path operations

```javascript
// Line 7-8: Create Express App
const app = express();
const PORT = process.env.PORT || 3000;
```

**Explanation:**
- Creates Express application instance
- Sets port (uses environment variable or defaults to 3000)

```javascript
// Line 11: Body Parser Middleware
app.use(bodyParser.urlencoded({ extended: true }));
```

**Explanation:**
- `app.use()`: Mounts middleware for all routes
- `urlencoded`: Parses form data (application/x-www-form-urlencoded)
- `extended: true`: Allows parsing of rich objects and arrays

**What it does:**
- Parses POST request bodies from HTML forms
- Makes data available in `req.body`

```javascript
// Line 12-18: Session Middleware Configuration
app.use(session({
    secret: 'your-secret-key-change-in-production',
    resave: false,
    saveUninitialized: false,
    cookie: { 
        secure: false,
        httpOnly: true,
        maxAge: 24 * 60 * 60 * 1000
    }
}));
```

**Line-by-Line Breakdown:**

**`secret`**: 
- Used to sign the session cookie
- Prevents tampering with the cookie
- **IMPORTANT:** Change in production!

**`resave: false`**:
- Don't save session if it hasn't been modified
- Prevents unnecessary writes to session store
- Improves performance

**`saveUninitialized: false`**:
- Don't create session until something is stored
- Security best practice (prevents session fixation attacks)
- Only creates session after successful login

**`cookie.secure: false`**:
- Set to `true` in production with HTTPS
- Ensures cookie only sent over encrypted connection

**`cookie.httpOnly: true`**:
- Prevents JavaScript from accessing cookie
- Protects against XSS attacks

**`cookie.maxAge`**:
- Session expiration time (24 hours)
- After this time, session expires and user must login again

```javascript
// Line 20-21: Configure View Engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
```

**Explanation:**
- Sets EJS as the templating engine
- Specifies views directory location
- `__dirname`: Current directory path

```javascript
// Line 24: Static Files Middleware
app.use(express.static(path.join(__dirname, 'public')));
```

**Explanation:**
- Serves static files (CSS, JS, images) from `public` directory
- Files accessible at root path (e.g., `/css/styles.css`)

```javascript
// Line 27-30: Session Logging Middleware
app.use((req, res, next) => {
    console.log('Session ID:', req.sessionID);
    console.log('Session Data:', req.session);
    next();
});
```

**Explanation:**
- Custom middleware function
- Logs session information for debugging
- `next()`: Passes control to next middleware/route

```javascript
// Line 33-36: Root Route
app.get('/', (req, res) => {
    res.render('index', { user: req.session.user });
});
```

**Explanation:**
- Handles GET requests to root path
- `res.render()`: Renders EJS template
- Passes `user` object to template (null if not logged in)

```javascript
// Line 39: Mount Auth Routes
app.use('/auth', authRoutes);
```

**Explanation:**
- Mounts authentication routes
- All routes in `authRoutes` prefixed with `/auth`
- Example: `/auth/login`, `/auth/logout`

```javascript
// Line 42-48: Protected Dashboard Route
app.get('/dashboard', (req, res) => {
    if (!req.session.user) {
        return res.redirect('/auth/login');
    }
    res.render('dashboard', { user: req.session.user });
});
```

**Explanation:**
- **Authentication Check**: `if (!req.session.user)`
  - Checks if user is logged in
  - If not, redirects to login page
- **Protected Content**: Only renders if authenticated
- This is a simple form of route protection

```javascript
// Line 51-55: Error Handling Middleware
app.use((err, req, res, next) => {
    console.error('Error:', err);
    res.status(500).send('Internal Server Error');
});
```

**Explanation:**
- Catches errors from route handlers
- Must have 4 parameters (err, req, res, next)
- Sends 500 status code on error

```javascript
// Line 58-61: Start Server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

**Explanation:**
- Starts HTTP server
- Listens on specified port
- Callback executes when server starts

---

### File: `routes/auth.js`

```javascript
// Line 1-4: Import Dependencies
const express = require('express');
const router = express.Router();
const bcrypt = require('bcryptjs');
```

**Explanation:**
- `express.Router()`: Creates a router instance
- `bcryptjs`: Password hashing library (pure JavaScript implementation)

```javascript
// Line 6-15: User Data Storage
const users = [
    {
        id: 1,
        username: 'admin',
        password: bcrypt.hashSync('password', 8)
    }
];
```

**Explanation:**
- In-memory user storage (demo only)
- `bcrypt.hashSync()`: Synchronously hashes password
- **Salt Rounds (8)**: Number of hashing iterations
  - Higher = more secure but slower
  - 8-10 is typical for production

**How Hashing Works:**
```javascript
// Original: 'password'
// After bcrypt.hashSync('password', 8):
// '$2a$08$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy'
// This includes: algorithm, salt rounds, salt, and hash
```

```javascript
// Line 17-23: GET Login Route
router.get('/login', (req, res) => {
    if (req.session.user) {
        return res.redirect('/dashboard');
    }
    res.render('login', { error: null });
});
```

**Explanation:**
- Handles GET requests to `/auth/login`
- **Already Logged In Check**: Prevents logged-in users from seeing login page
- Renders login template with no error initially

```javascript
// Line 25-54: POST Login Route
router.post('/login', (req, res) => {
    const { username, password } = req.body;
```

**Explanation:**
- Handles POST requests (form submission)
- **Destructuring**: Extracts `username` and `password` from `req.body`
- `req.body` populated by body-parser middleware

```javascript
    // Line 28-32: Input Validation
    if (!username || !password) {
        return res.render('login', { 
            error: 'Username and password are required' 
        });
    }
```

**Explanation:**
- Validates that both fields are provided
- Returns early if validation fails
- Shows error message to user

```javascript
    // Line 34-35: Find User
    const user = users.find(u => u.username === username);
```

**Explanation:**
- `Array.find()`: Returns first element matching condition
- Searches users array for matching username
- Returns `undefined` if not found

```javascript
    // Line 37-52: Authentication Logic
    if (user) {
        const passwordMatch = bcrypt.compareSync(password, user.password);
```

**Explanation:**
- `bcrypt.compareSync()`: Compares plain text with hash
- Returns `true` if match, `false` otherwise
- Automatically extracts salt from hash

**How Password Comparison Works:**
```
1. User enters: "password"
2. Stored hash: "$2a$08$N9qo8uLOickgx2ZMRZoMye..."
3. bcrypt extracts salt from hash
4. Hashes "password" with extracted salt
5. Compares result with stored hash
6. Returns true if match
```

```javascript
        if (passwordMatch) {
            req.session.user = {
                id: user.id,
                username: user.username
            };
            res.redirect('/dashboard');
```

**Explanation:**
- **Create Session**: Stores user data in session
- **Security**: Only stores non-sensitive data (no password!)
- **Redirect**: Sends user to dashboard after login

**What Happens Behind the Scenes:**
1. Session created in session store
2. Session ID generated (e.g., "abc123")
3. Cookie sent to client: `Set-Cookie: connect.sid=abc123`
4. Client stores cookie
5. Future requests include cookie automatically

```javascript
        } else {
            res.render('login', { 
                error: 'Invalid username or password' 
            });
        }
    } else {
        res.render('login', { 
            error: 'Invalid username or password' 
        });
    }
```

**Explanation:**
- Same error message for both cases (security best practice)
- Prevents username enumeration attacks
- User can't tell if username exists or password is wrong

```javascript
// Line 56-67: Logout Route
router.get('/logout', (req, res) => {
    req.session.destroy((err) => {
        if (err) {
            console.error('Error destroying session:', err);
            return res.redirect('/dashboard');
        }
        res.clearCookie('connect.sid');
        res.redirect('/');
    });
});
```

**Explanation:**
- **`req.session.destroy()`**: Removes session from store
- **Callback**: Executes after destruction
- **`res.clearCookie()`**: Removes cookie from client
- **Redirect**: Sends user to home page

**Why Clear Cookie?**
- Even after session destroyed, cookie may still exist
- Clearing ensures complete logout

---

### File: `middleware/auth.js`

```javascript
// Line 1-12: Authentication Middleware
const requireAuth = (req, res, next) => {
    if (req.session && req.session.user) {
        return next();
    } else {
        req.session.returnTo = req.originalUrl;
        res.redirect('/auth/login');
    }
};
```

**Explanation:**
- **Middleware Function**: Takes req, res, next parameters
- **Check Session**: Verifies user is authenticated
- **`next()`**: Allows request to proceed
- **Redirect**: Sends to login if not authenticated
- **`returnTo`**: Stores original URL for redirect after login

**Usage Example:**
```javascript
app.get('/dashboard', requireAuth, (req, res) => {
    res.render('dashboard', { user: req.session.user });
});
```

---

### File: `views/login.ejs`

```html
<!-- Line 17: Form Action -->
<form action="/auth/login" method="POST">
```

**Explanation:**
- `action`: URL where form submits
- `method="POST"`: HTTP method (not GET, which would expose password in URL)

```html
<!-- Line 20: Username Input -->
<input type="text" class="form-control" id="username" name="username" required>
```

**Explanation:**
- `name="username"`: Key in `req.body` object
- `required`: HTML5 validation (browser checks before submit)

```html
<!-- Line 24: Password Input -->
<input type="password" class="form-control" id="password" name="password" required>
```

**Explanation:**
- `type="password"`: Hides input (shows dots/asterisks)
- Prevents shoulder surfing

```html
<!-- Line 30-34: Error Display -->
<% if (typeof error !== 'undefined' && error) { %>
    <div class="alert alert-danger" role="alert">
        <%= error %>
    </div>
<% } %>
```

**Explanation:**
- **EJS Conditional**: `<% %>` executes JavaScript
- **Check Error**: Verifies error exists
- **Output Error**: `<%= %>` outputs value (HTML escaped)

---

### File: `views/dashboard.ejs`

```html
<!-- Line 26: Display Username -->
<p class="text-center">Welcome, <strong><%= user.username %></strong>!</p>
```

**Explanation:**
- **EJS Output**: `<%= %>` outputs value
- **HTML Escaping**: Automatically escapes HTML (prevents XSS)
- Accesses `user` object passed from route handler

---

### File: `views/index.ejs`

```html
<!-- Line 19-30: Conditional Rendering -->
<% if (user) { %>
    <!-- Authenticated User View -->
<% } else { %>
    <!-- Guest User View -->
<% } %>
```

**Explanation:**
- **Conditional Logic**: Shows different content based on auth status
- **EJS Syntax**: `<% %>` for logic, `<%= %>` for output

---

## Security Considerations

### 1. **Password Security**

✅ **What We Do:**
- Hash passwords with bcrypt
- Never store plain text passwords
- Use salt rounds (8+)

❌ **What NOT to Do:**
- Store passwords in plain text
- Use weak hashing (MD5, SHA1)
- Send passwords in URLs (use POST, not GET)

### 2. **Session Security**

✅ **Best Practices:**
- Use strong secret key
- Set `httpOnly: true` (prevents XSS)
- Set `secure: true` in production (HTTPS only)
- Set appropriate `maxAge`
- Use `saveUninitialized: false`

❌ **Common Mistakes:**
- Weak secret key
- Storing sensitive data in session
- Not setting expiration
- Allowing session fixation

### 3. **Input Validation**

✅ **What We Do:**
- Validate required fields
- Use generic error messages
- Sanitize user input (EJS auto-escapes)

❌ **What NOT to Do:**
- Reveal which field is wrong (username vs password)
- Allow SQL injection (use parameterized queries)
- Trust client-side validation only

### 4. **Session Fixation Prevention**

**What is Session Fixation?**
- Attacker forces victim to use attacker's session ID
- After victim logs in, attacker has access

**How We Prevent:**
- `saveUninitialized: false` - Don't create session until login
- Regenerate session ID after login (can be added)

### 5. **XSS (Cross-Site Scripting) Prevention**

**How EJS Protects:**
- `<%= %>` automatically escapes HTML
- Prevents script injection

**Example:**
```javascript
// User input: <script>alert('XSS')</script>
// EJS output: &lt;script&gt;alert('XSS')&lt;/script&gt;
// Browser displays as text, doesn't execute
```

---

## How to Run

### 1. Install Dependencies

```bash
cd Homework/Homework3
npm install
```

This installs:
- `express`: Web framework
- `express-session`: Session management
- `body-parser`: Request body parsing
- `bcryptjs`: Password hashing
- `ejs`: Templating engine

### 2. Start the Server

```bash
npm start
# or
node app.js
```

### 3. Access the Application

- Open browser: `http://localhost:3000`
- Click "Login"
- Use credentials:
  - Username: `admin`, Password: `password`
  - Username: `user`, Password: `user123`

### 4. Test the Flow

1. Visit home page (not logged in)
2. Click "Login"
3. Enter credentials
4. Redirected to dashboard
5. Session persists across page refreshes
6. Click "Logout"
7. Session destroyed, redirected to home

---

## Key Takeaways

### 1. **Session vs Token Authentication**

| Feature | Session-Based (HW3) | Token-Based (JWT - HW7) |
|---------|---------------------|------------------------|
| Storage | Server-side | Client-side |
| Scalability | Requires shared store | Stateless |
| Security | Server controls | Token can be stolen |
| Use Case | Traditional web apps | APIs, SPAs |

### 2. **Middleware Order Matters**

```javascript
app.use(bodyParser);      // 1. Parse body first
app.use(session);         // 2. Then create session
app.use(routes);          // 3. Finally handle routes
```

### 3. **Password Hashing is One-Way**

- Can't reverse hash to get password
- Must compare hashes, not decrypt
- Salt prevents rainbow table attacks

### 4. **Sessions Require Server-Side Storage**

- In production, use Redis or database
- Memory store (default) lost on server restart
- Not suitable for multiple servers (need shared store)

---

## Additional Resources

### Related Lecture Topics
- **Lecture 02**: Session and Prompt Management
- **Lecture 06**: Authentication and Authorization
- **Lecture 08**: Caching with Redis (can store sessions)

### Next Steps
- **HW7**: JWT Token-Based Authentication
- **HW8**: Message Queues (Kafka)
- **HW9**: Multi-Agent Systems

---

## Summary

This homework demonstrates:
1. ✅ Server-side session management
2. ✅ Password hashing with bcrypt
3. ✅ Protected routes
4. ✅ EJS templating
5. ✅ Express routing
6. ✅ Middleware usage
7. ✅ Security best practices

**Core Concept:** Sessions allow maintaining user state across stateless HTTP requests by storing data server-side and identifying clients with cookies.
