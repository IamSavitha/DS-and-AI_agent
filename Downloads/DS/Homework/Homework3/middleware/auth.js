// middleware/auth.js - Authentication Middleware
// Protects routes by checking if user is authenticated

// ============================================================================
// AUTHENTICATION MIDDLEWARE
// ============================================================================
// This middleware function checks if a user is logged in
// If not authenticated, it redirects to login page
// If authenticated, it allows the request to proceed

const requireAuth = (req, res, next) => {
    // Check if user session exists
    // req.session.user is set during login (see routes/auth.js)
    if (req.session && req.session.user) {
        // User is authenticated, proceed to the next middleware/route handler
        return next();
    } else {
        // User is not authenticated
        // Store the original URL they tried to access
        // This allows us to redirect them back after login
        req.session.returnTo = req.originalUrl;
        // Redirect to login page
        res.redirect('/auth/login');
    }
};

// ============================================================================
// OPTIONAL: GUEST MIDDLEWARE
// ============================================================================
// Redirects authenticated users away from login/register pages
const requireGuest = (req, res, next) => {
    if (req.session && req.session.user) {
        // User is already logged in, redirect to dashboard
        return res.redirect('/dashboard');
    }
    // User is not logged in, allow access to login/register pages
    next();
};

// Export middleware functions
module.exports = {
    requireAuth,
    requireGuest
};
