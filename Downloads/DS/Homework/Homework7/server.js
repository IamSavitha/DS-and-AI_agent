/**
 * Express Server for JWT Authentication System
 * 
 * This server implements a complete authentication system using:
 * - JWT (JSON Web Tokens) for stateless authentication
 * - bcrypt for password hashing
 * - MongoDB with Mongoose for user storage
 * - Express middleware for route protection
 */

require('dotenv').config(); // Load environment variables from .env file
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

// Create Express application instance
const app = express();

// =======================================================
// MIDDLEWARE CONFIGURATION
// =======================================================

/**
 * CORS (Cross-Origin Resource Sharing) Middleware
 * 
 * Concept: CORS allows web pages to make requests to a different domain
 * than the one serving the web page. This is essential for frontend-backend
 * separation in modern web applications.
 * 
 * Without CORS, browsers block requests from different origins for security.
 */
app.use(cors());

/**
 * Express JSON Parser Middleware
 * 
 * Concept: This middleware parses incoming requests with JSON payloads.
 * It makes req.body available as a JavaScript object.
 * 
 * Example: POST /api/auth/login with body {"username": "user", "password": "pass"}
 *          becomes accessible as req.body.username and req.body.password
 */
app.use(express.json());

// =======================================================
// MONGODB CONNECTION
// =======================================================

/**
 * MongoDB Connection using Mongoose
 * 
 * Concepts:
 * 1. MongoDB: NoSQL document database that stores data as BSON (Binary JSON)
 * 2. Mongoose: ODM (Object Document Mapper) for MongoDB in Node.js
 *    - Provides schema validation
 *    - Converts JavaScript objects to MongoDB documents
 *    - Handles relationships and data modeling
 * 
 * Connection String Format: mongodb://[username:password@]host[:port][/database]
 * 
 * process.env.MONGODB_URI: Retrieved from .env file for security
 */
mongoose.connect(process.env.MONGODB_URI)
    .then(() => {
        console.log('✅ MongoDB connected successfully');
        console.log(`   Database: ${mongoose.connection.name}`);
    })
    .catch((err) => {
        console.error('❌ MongoDB connection error:', err);
        process.exit(1); // Exit process if database connection fails
    });

// =======================================================
// ROUTES
// =======================================================

/**
 * Authentication Routes
 * 
 * All routes under /api/auth are handled by authRoutes.js
 * This includes:
 * - POST /api/auth/register - User registration
 * - POST /api/auth/login - User login (returns JWT token)
 * - GET /api/auth/protected/admin-data - Protected route requiring admin role
 */
app.use('/api/auth', require('./authRoutes'));

// =======================================================
// ROOT ENDPOINT
// =======================================================

/**
 * Health Check / Root Endpoint
 * 
 * Simple endpoint to verify the server is running.
 * Useful for monitoring and testing.
 */
app.get('/', (req, res) => {
    res.json({ 
        message: 'JWT Authentication API is running',
        endpoints: {
            register: 'POST /api/auth/register',
            login: 'POST /api/auth/login',
            protected: 'GET /api/auth/protected/admin-data (requires Bearer token)'
        }
    });
});

// =======================================================
// ERROR HANDLING MIDDLEWARE
// =======================================================

/**
 * Global Error Handler
 * 
 * This middleware catches any errors that occur in route handlers
 * and sends a standardized error response.
 * 
 * Concept: Express error handling middleware has 4 parameters (err, req, res, next)
 */
app.use((err, req, res, next) => {
    console.error('Error:', err);
    res.status(err.status || 500).json({
        message: err.message || 'Internal server error',
        ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
    });
});

// =======================================================
// SERVER STARTUP
// =======================================================

/**
 * Start the Express Server
 * 
 * The server listens on the port specified in environment variables
 * or defaults to port 3000.
 * 
 * Concept: process.env.PORT allows deployment platforms (like Heroku, AWS)
 * to dynamically assign ports.
 */
const PORT = process.env.PORT || 3000;

// Only start server if this file is run directly (not when imported for testing)
if (require.main === module) {
    app.listen(PORT, () => {
        console.log(`🚀 Server running on port ${PORT}`);
        console.log(`   Environment: ${process.env.NODE_ENV || 'development'}`);
    });
}

// Export app for testing (supertest requires the app, not the server)
module.exports = app;
