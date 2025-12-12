/**
 * ============================================
 * Q2: MYSQL/SEQUELIZE CRUD API
 * ============================================
 * 
 * CONCEPTS COVERED:
 * 1. Express.js - Web application framework
 * 2. Sequelize ORM - Object-Relational Mapping
 * 3. MySQL Database - Relational database
 * 4. RESTful API - Resource-based endpoints
 * 5. Middleware - Request processing
 * 6. MVC Pattern - Model-View-Controller
 */

require('dotenv').config();
const express = require('express');
const cors = require('cors');
const sequelize = require('./config/database');
const bookRoutes = require('./routes/book.routes');

/**
 * CONCEPT: Express Application
 * - Creates Express app instance
 * - App handles HTTP requests and responses
 */
const app = express();
const PORT = process.env.PORT || 3001;

/**
 * CONCEPT: Middleware
 * - Functions that execute during request-response cycle
 * - cors() enables Cross-Origin Resource Sharing
 * - express.json() parses JSON request bodies
 */
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

/**
 * CONCEPT: Route Mounting
 * - Mounts book routes at /api/books
 * - All routes in book.routes.js will be prefixed with /api/books
 */
app.use('/api/books', bookRoutes);

/**
 * CONCEPT: Root Route
 * - Handles GET requests to root path
 * - Returns API information
 */
app.get('/', (req, res) => {
  res.json({
    message: 'Book Management API',
    version: '1.0.0',
    endpoints: {
      'GET /api/books': 'Get all books',
      'GET /api/books/:id': 'Get book by ID',
      'POST /api/books': 'Create new book',
      'PUT /api/books/:id': 'Update book',
      'DELETE /api/books/:id': 'Delete book'
    }
  });
});

/**
 * CONCEPT: Database Connection
 * - Tests database connection before starting server
 * - sequelize.authenticate() verifies credentials
 * - sequelize.sync() creates tables if they don't exist
 */
const startServer = async () => {
  try {
    // Test database connection
    await sequelize.authenticate();
    console.log('✅ Database connection established successfully.');

    // Sync models with database (creates tables)
    await sequelize.sync({ alter: true });
    console.log('✅ Database models synchronized.');

    // Start Express server
    app.listen(PORT, () => {
      console.log(`🚀 Server running on http://localhost:${PORT}`);
      console.log(`📚 Book Management API is ready!`);
    });
  } catch (error) {
    console.error('❌ Unable to connect to database:', error);
    process.exit(1);
  }
};

startServer();

module.exports = app;
