// routes/auth.js - Authentication Routes
// Handles user login, logout, and authentication logic

// ============================================================================
// 1. IMPORT DEPENDENCIES
// ============================================================================
const express = require('express');
const router = express.Router(); // Create a new router instance
const bcrypt = require('bcryptjs'); // Library for hashing passwords

// ============================================================================
// 2. USER DATA STORAGE (In-Memory - For Demo Only)
// ============================================================================
// In production, this would be stored in a database (MongoDB, PostgreSQL, etc.)
// For this homework, we use an in-memory array

const users = [
    {
        id: 1,
        username: 'admin',
        // Password is hashed using bcrypt with salt rounds of 8
        // bcrypt.hashSync() synchronously hashes the password
        // Salt rounds determine the computational cost (higher = more secure but slower)
        password: bcrypt.hashSync('password', 8) // Hashed version of 'password'
    },
    {
        id: 2,
        username: 'user',
        password: bcrypt.hashSync('user123', 8) // Hashed version of 'user123'
    }
];

// ============================================================================
// 3. GET LOGIN PAGE ROUTE
// ============================================================================
// Displays the login form to the user
router.get('/login', (req, res) => {
    // Check if user is already logged in
    if (req.session.user) {
        // If already authenticated, redirect to dashboard
        return res.redirect('/dashboard');
    }
    // Render the login page template
    res.render('login', { error: null });
});

// ============================================================================
// 4. POST LOGIN ROUTE - HANDLE LOGIN FORM SUBMISSION
// ============================================================================
// Processes the login form data and authenticates the user
router.post('/login', (req, res) => {
    // Extract username and password from request body
    // These come from the HTML form submission
    const { username, password } = req.body;

    // Validate input - check if username and password are provided
    if (!username || !password) {
        return res.render('login', { 
            error: 'Username and password are required' 
        });
    }

    // Find user in the users array by username
    // Array.find() returns the first element that matches the condition
    const user = users.find(u => u.username === username);

    // Check if user exists and password matches
    if (user) {
        // bcrypt.compareSync() compares the plain text password with the hashed password
        // It returns true if they match, false otherwise
        // This is secure because:
        // 1. We never store plain text passwords
        // 2. bcrypt handles salt extraction and comparison automatically
        const passwordMatch = bcrypt.compareSync(password, user.password);

        if (passwordMatch) {
            // Authentication successful!
            // Store user information in the session
            // This creates a server-side session and sends a session cookie to the client
            req.session.user = {
                id: user.id,
                username: user.username
                // Note: We NEVER store the password in the session
            };

            // Redirect to dashboard after successful login
            res.redirect('/dashboard');
        } else {
            // Password doesn't match
            res.render('login', { 
                error: 'Invalid username or password' 
            });
        }
    } else {
        // User not found
        // For security, we don't reveal whether username exists or not
        res.render('login', { 
            error: 'Invalid username or password' 
        });
    }
});

// ============================================================================
// 5. LOGOUT ROUTE
// ============================================================================
// Destroys the user's session and logs them out
router.get('/logout', (req, res) => {
    // req.session.destroy() removes the session from the server
    // It takes a callback function that runs after destruction
    req.session.destroy((err) => {
        if (err) {
            // If there's an error destroying the session
            console.error('Error destroying session:', err);
            // Redirect back to dashboard (user is still logged in)
            return res.redirect('/dashboard');
        }
        // Successfully logged out
        // Clear the session cookie by setting it to expire
        res.clearCookie('connect.sid'); // 'connect.sid' is the default session cookie name
        // Redirect to home page
        res.redirect('/');
    });
});

// ============================================================================
// 6. EXPORT ROUTER
// ============================================================================
// Export the router so it can be used in app.js
module.exports = router;
