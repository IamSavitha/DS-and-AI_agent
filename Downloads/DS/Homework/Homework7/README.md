# Homework 7: JWT Authentication & Authorization - Setup & Run Guide

## 📋 Prerequisites

Before running this application, ensure you have the following installed:

1. **Node.js** (version 14 or higher)
   - Check version: `node --version`
   - Download: [nodejs.org](https://nodejs.org/)

2. **MongoDB** (local installation or MongoDB Atlas account)
   - Local MongoDB: [mongodb.com/download](https://www.mongodb.com/try/download/community)
   - MongoDB Atlas (cloud): [mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
   - Check if running: `mongod --version` (for local)

3. **npm** (comes with Node.js)
   - Check version: `npm --version`

---

## 🚀 Quick Start Guide

### Step 1: Navigate to Project Directory

```bash
cd /Users/savithavijayarangan/Downloads/DS/Homework/Homework7
```

### Step 2: Install Dependencies

```bash
npm install
```

This will install all required packages:
- `express` - Web framework
- `mongoose` - MongoDB ODM
- `jsonwebtoken` - JWT token handling
- `bcrypt` - Password hashing
- `dotenv` - Environment variables
- `cors` - Cross-origin resource sharing
- `supertest`, `chai`, `mocha` - Testing libraries

### Step 3: Set Up Environment Variables

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` file with your configuration:
   ```bash
   nano .env
   # or use any text editor
   ```

3. Update the following values:

   **For Local MongoDB:**
   ```env
   MONGODB_URI=mongodb://localhost:27017/hw7_auth_db
   ```

   **For MongoDB Atlas (Cloud):**
   ```env
   MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/hw7_auth_db
   ```

   **Generate a Strong JWT Secret:**
   ```bash
   node -e "console.log(require('crypto').randomBytes(64).toString('hex'))"
   ```
   Copy the output and paste it as your `JWT_SECRET`:
   ```env
   JWT_SECRET=your_generated_secret_key_here
   ```

   **Complete .env file example:**
   ```env
   MONGODB_URI=mongodb://localhost:27017/hw7_auth_db
   JWT_SECRET=your_super_secret_jwt_key_change_this_in_production
   TOKEN_EXPIRY=24h
   PORT=3000
   NODE_ENV=development
   ```

### Step 4: Start MongoDB (Local Installation Only)

If you're using local MongoDB, make sure it's running:

**macOS (using Homebrew):**
```bash
brew services start mongodb-community
```

**Linux:**
```bash
sudo systemctl start mongod
```

**Windows:**
```bash
net start MongoDB
```

**Or run manually:**
```bash
mongod
```

**Verify MongoDB is running:**
```bash
mongosh
# or
mongo
```

If you see the MongoDB shell, you're good! Type `exit` to leave.

---

## 🏃 Running the Application

### Option 1: Standard Run

```bash
npm start
```

This runs: `node server.js`

You should see:
```
✅ MongoDB connected successfully
   Database: hw7_auth_db
🚀 Server running on port 3000
   Environment: development
```

### Option 2: Development Mode (with auto-reload)

First install nodemon globally (if not already installed):
```bash
npm install -g nodemon
```

Then run:
```bash
npm run dev
```

This runs: `nodemon server.js` - automatically restarts server when you make changes.

---

## 🧪 Testing the Application

### Run Automated Tests

```bash
npm test
```

This will:
1. Create test users (admin and standard user)
2. Test login functionality
3. Test protected routes
4. Test authorization (admin vs user)
5. Test security (invalid tokens, missing tokens)

### Manual Testing with cURL

#### 1. Register a New User

```bash
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123",
    "role": "user"
  }'
```

**Expected Response:**
```json
{
  "message": "User registered successfully.",
  "username": "testuser",
  "role": "user"
}
```

#### 2. Register an Admin User

```bash
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "adminpass123",
    "role": "admin"
  }'
```

#### 3. Login (Get JWT Token)

```bash
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'
```

**Expected Response:**
```json
{
  "message": "Login successful.",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expiresIn": "24h"
}
```

**Save the token** from the response for the next steps!

#### 4. Access Protected Admin Route (with Admin Token)

Replace `YOUR_ADMIN_TOKEN` with the token from admin login:

```bash
curl -X GET http://localhost:3000/api/auth/protected/admin-data \
  -H "Authorization: Bearer YOUR_ADMIN_TOKEN"
```

**Expected Response:**
```json
{
  "message": "SUCCESS! You accessed the highly protected admin resource.",
  "data": {
    "sensitiveInfo": "Welcome, admin. You are authorized as 'admin'.",
    "verifiedClaims": {
      "id": "...",
      "username": "admin",
      "role": "admin"
    }
  }
}
```

#### 5. Try Accessing Admin Route with User Token (Should Fail)

Replace `YOUR_USER_TOKEN` with a token from a regular user login:

```bash
curl -X GET http://localhost:3000/api/auth/protected/admin-data \
  -H "Authorization: Bearer YOUR_USER_TOKEN"
```

**Expected Response (403 Forbidden):**
```json
{
  "message": "Access Denied: Requires 'admin' role.",
  "userRole": "user"
}
```

#### 6. Try Accessing Without Token (Should Fail)

```bash
curl -X GET http://localhost:3000/api/auth/protected/admin-data
```

**Expected Response (401 Unauthorized):**
```json
{
  "message": "Unauthorized: Bearer token format required."
}
```

---

## 🌐 Testing with Postman or Thunder Client

### Setup

1. **Base URL:** `http://localhost:3000`

### Endpoints

#### 1. Register User
- **Method:** POST
- **URL:** `http://localhost:3000/api/auth/register`
- **Headers:** `Content-Type: application/json`
- **Body (JSON):**
  ```json
  {
    "username": "newuser",
    "password": "password123",
    "role": "user"
  }
  ```

#### 2. Login
- **Method:** POST
- **URL:** `http://localhost:3000/api/auth/login`
- **Headers:** `Content-Type: application/json`
- **Body (JSON):**
  ```json
  {
    "username": "newuser",
    "password": "password123"
  }
  ```
- **Response:** Copy the `token` from the response

#### 3. Access Protected Route
- **Method:** GET
- **URL:** `http://localhost:3000/api/auth/protected/admin-data`
- **Headers:** 
  - `Authorization: Bearer YOUR_TOKEN_HERE`
  - Replace `YOUR_TOKEN_HERE` with the token from login

---

## 📁 Project Structure

```
Homework7/
├── server.js              # Main Express server
├── authRoutes.js          # Authentication routes
├── middleware/
│   └── auth.js           # JWT verification middleware
├── models/
│   └── User.js           # Mongoose User model
├── auth.test.js          # Test suite
├── package.json          # Dependencies
├── env.example           # Environment variables template
├── .env                  # Your environment variables (create this)
└── README.md            # This file
```

---

## 🔧 Troubleshooting

### Issue: "MongoDB connection error"

**Solutions:**
1. Make sure MongoDB is running:
   ```bash
   # Check if MongoDB is running
   mongosh
   ```

2. Check your `MONGODB_URI` in `.env` file

3. For MongoDB Atlas, ensure:
   - Your IP is whitelisted in Network Access
   - Your database user has proper permissions
   - Connection string is correct

### Issue: "JWT_SECRET is not defined"

**Solution:**
- Make sure you created `.env` file from `env.example`
- Check that `JWT_SECRET` is set in `.env`
- Restart the server after creating/editing `.env`

### Issue: "Port 3000 already in use"

**Solutions:**
1. Change PORT in `.env` file to a different port (e.g., 3001)
2. Or kill the process using port 3000:
   ```bash
   # Find process
   lsof -ti:3000
   
   # Kill process
   kill -9 $(lsof -ti:3000)
   ```

### Issue: "Cannot find module" errors

**Solution:**
```bash
# Delete node_modules and reinstall
rm -rf node_modules
npm install
```

### Issue: Tests failing

**Solutions:**
1. Make sure MongoDB is running
2. Check that `.env` file exists and has correct values
3. Tests create users automatically, but if they already exist, tests should still pass
4. Check test timeout - increase in `auth.test.js` if needed:
   ```javascript
   this.timeout(10000); // Increase if needed
   ```

---

## 📊 API Endpoints Summary

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register` | Register new user | No |
| POST | `/api/auth/login` | Login and get JWT token | No |
| GET | `/api/auth/protected/admin-data` | Access admin resource | Yes (Admin role) |
| GET | `/` | Health check | No |

---

## 🔐 Security Notes

1. **Never commit `.env` file to git** - It contains secrets
2. **Use strong JWT_SECRET** - Generate with crypto.randomBytes
3. **Use HTTPS in production** - Never send tokens over HTTP
4. **Set appropriate token expiration** - Don't make tokens last forever
5. **Validate all input** - Always validate user input
6. **Use environment variables** - Never hardcode secrets

---

## 📚 Additional Resources

- **JWT Debugger:** [jwt.io](https://jwt.io/)
- **MongoDB Documentation:** [docs.mongodb.com](https://docs.mongodb.com/)
- **Express.js Guide:** [expressjs.com](https://expressjs.com/)
- **Mongoose Documentation:** [mongoosejs.com](https://mongoosejs.com/docs/)

---

## ✅ Verification Checklist

Before submitting, verify:

- [ ] Server starts without errors
- [ ] MongoDB connection successful
- [ ] Can register a new user
- [ ] Can login and receive JWT token
- [ ] Can access protected route with valid admin token
- [ ] Cannot access admin route with user token (403)
- [ ] Cannot access protected route without token (401)
- [ ] All tests pass: `npm test`
- [ ] `.env` file is not committed to git

---

## 🎯 Next Steps

1. Test all endpoints manually
2. Run the test suite: `npm test`
3. Review the code explanations in `HW7_COMPLETE_EXPLANATION.md`
4. Study the glossary in `KEY_TERMS_GLOSSARY.md`
5. Experiment with different roles and permissions

---

## 💡 Tips

- Use **Postman** or **Thunder Client** (VS Code extension) for easier API testing
- Keep the server running in one terminal and test in another
- Check server console logs for debugging information
- Use `console.log()` to debug JWT tokens (in development only!)

---

Happy coding! 🚀
