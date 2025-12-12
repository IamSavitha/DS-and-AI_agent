/**
 * ============================================
 * BOOK ROUTES
 * ============================================
 * 
 * CONCEPTS:
 * 1. Express Router - Route organization
 * 2. RESTful Routes - Resource-based URLs
 * 3. HTTP Methods - GET, POST, PUT, DELETE
 * 4. Route Parameters - Dynamic URL segments
 */

const express = require('express');
const router = express.Router();
const bookController = require('../controllers/book.controller');

/**
 * CONCEPT: Express Router
 * - router is a mini Express app
 * - Handles routes for specific resource
 * - Mounted in main app.js file
 */

/**
 * CONCEPT: RESTful Route - Create
 * - POST /api/books
 * - Creates new book resource
 * - Maps to createBook controller function
 */
router.post('/', bookController.createBook);

/**
 * CONCEPT: RESTful Route - Read All
 * - GET /api/books
 * - Retrieves all books
 * - Maps to getAllBooks controller function
 */
router.get('/', bookController.getAllBooks);

/**
 * CONCEPT: RESTful Route - Read One
 * - GET /api/books/:id
 * - :id is route parameter (dynamic)
 * - Retrieves single book by ID
 * - Maps to getBookById controller function
 */
router.get('/:id', bookController.getBookById);

/**
 * CONCEPT: RESTful Route - Update
 * - PUT /api/books/:id
 * - Updates existing book
 * - Maps to updateBook controller function
 */
router.put('/:id', bookController.updateBook);

/**
 * CONCEPT: RESTful Route - Delete
 * - DELETE /api/books/:id
 * - Removes book from database
 * - Maps to deleteBook controller function
 */
router.delete('/:id', bookController.deleteBook);

module.exports = router;
