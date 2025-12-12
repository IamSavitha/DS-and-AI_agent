// app.js - Main Express Application Entry Point
// This file sets up the Express server, middleware, and routes

// ============================================================================
// 1. IMPORT DEPENDENCIES
// ============================================================================
const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const path = require('path');

// Import authentication routes
const authRoutes = require('./routes/auth');

// ============================================================================
// 2. CREATE EXPRESS APPLICATION INSTANCE
// ============================================================================
const app = express();
const PORT = process.env.PORT || 3000;

// ============================================================================
// 3. CONFIGURE MIDDLEWARE
// ============================================================================

// Body Parser Middleware
// Parses incoming request bodies in URL-encoded format (from HTML forms)
// extended: true allows parsing of rich objects and arrays
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json()); // Also parse JSON bodies for API endpoints

// Session Middleware Configuration
// express-session creates and manages session data on the server
app.use(session({
    secret: 'your-secret-key-change-in-production', // Secret key for signing session cookie
    resave: false, // Don't save session if unmodified (prevents unnecessary writes)
    saveUninitialized: false, // Don't create session until something is stored (security)
    cookie: { 
        secure: false, // Set to true in production with HTTPS
        httpOnly: true, // Prevents client-side JavaScript from accessing cookie
        maxAge: 24 * 60 * 60 * 1000 // Session expires after 24 hours (in milliseconds)
    }
}));

// ============================================================================
// 4. CONFIGURE VIEW ENGINE (EJS - Embedded JavaScript)
// ============================================================================
// EJS allows embedding JavaScript in HTML templates
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Serve static files (CSS, JS, images) from public directory
app.use(express.static(path.join(__dirname, 'public')));

// ============================================================================
// 5. MIDDLEWARE FOR SESSION LOGGING (Development Only)
// ============================================================================
// This middleware logs session data for debugging purposes
app.use((req, res, next) => {
    console.log('Session ID:', req.sessionID);
    console.log('Session Data:', req.session);
    next(); // Pass control to next middleware/route handler
});

// ============================================================================
// 6. ROUTES
// ============================================================================

// Root Route - Home Page
// Displays different content based on whether user is logged in
app.get('/', (req, res) => {
    // Pass user session data to the view template
    res.render('index', { user: req.session.user });
});

// Mount authentication routes
// All routes in authRoutes will be prefixed with '/auth'
app.use('/auth', authRoutes);

// Protected Dashboard Route
// Only accessible to authenticated users
app.get('/dashboard', (req, res) => {
    // Check if user session exists (authentication check)
    if (!req.session.user) {
        // If not authenticated, redirect to login page
        return res.redirect('/auth/login');
    }
    // If authenticated, render dashboard with user data
    res.render('dashboard', { user: req.session.user });
});

// ============================================================================
// 7. ERROR HANDLING MIDDLEWARE
// ============================================================================
// Catches any errors that occur in route handlers
app.use((err, req, res, next) => {
    console.error('Error:', err);
    res.status(500).send('Internal Server Error');
});

// ============================================================================
// 8. START SERVER
// ============================================================================
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
    console.log(`Environment: ${process.env.NODE_ENV || 'development'}`);
});
