/**
 * ============================================
 * BOOK CONTROLLER
 * ============================================
 * 
 * CONCEPTS:
 * 1. Controller Pattern - Business logic separation
 * 2. Async/Await - Asynchronous operations
 * 3. Error Handling - Try-catch blocks
 * 4. HTTP Status Codes - Response codes
 * 5. Sequelize Methods - Database operations
 */

const { Book } = require('../models');

/**
 * CONCEPT: Controller Function - Create Book
 * - Handles POST /api/books
 * - Creates new book record in database
 * - Returns created book with 201 status
 */
exports.createBook = async (req, res) => {
  try {
    /**
     * CONCEPT: Request Body
     * - req.body contains JSON data from client
     * - Extracted using express.json() middleware
     */
    const { title, author } = req.body;

    /**
     * CONCEPT: Input Validation
     * - Checks if required fields are present
     * - Returns 400 (Bad Request) if validation fails
     */
    if (!title || !author) {
      return res.status(400).json({
        error: 'Title and author are required fields'
      });
    }

    /**
     * CONCEPT: Sequelize Create Method
     * - Book.create() inserts new record
     * - Returns created book object
     * - Automatically sets id, createdAt, updatedAt
     */
    const book = await Book.create({
      title: title.trim(),
      author: author.trim()
    });

    /**
     * CONCEPT: HTTP Status Code 201
     * - 201 Created: Resource successfully created
     * - Returns created resource in response body
     */
    res.status(201).json({
      message: 'Book created successfully',
      book: book
    });
  } catch (error) {
    /**
     * CONCEPT: Error Handling
     * - Catches database errors
     * - Returns 500 (Internal Server Error)
     * - Includes error message for debugging
     */
    console.error('Error creating book:', error);
    res.status(500).json({
      error: 'Failed to create book',
      message: error.message
    });
  }
};

/**
 * CONCEPT: Controller Function - Get All Books
 * - Handles GET /api/books
 * - Retrieves all books from database
 * - Returns array of books
 */
exports.getAllBooks = async (req, res) => {
  try {
    /**
     * CONCEPT: Sequelize FindAll Method
     * - Book.findAll() retrieves all records
     * - Returns array of book objects
     * - Empty array if no books exist
     */
    const books = await Book.findAll({
      order: [['id', 'ASC']]  // Order by ID ascending
    });

    /**
     * CONCEPT: HTTP Status Code 200
     * - 200 OK: Request successful
     * - Returns data in response body
     */
    res.status(200).json({
      message: 'Books retrieved successfully',
      count: books.length,
      books: books
    });
  } catch (error) {
    console.error('Error fetching books:', error);
    res.status(500).json({
      error: 'Failed to fetch books',
      message: error.message
    });
  }
};

/**
 * CONCEPT: Controller Function - Get Book by ID
 * - Handles GET /api/books/:id
 * - Retrieves single book by primary key
 * - Returns 404 if book not found
 */
exports.getBookById = async (req, res) => {
  try {
    /**
     * CONCEPT: URL Parameters
     * - req.params contains route parameters
     * - :id in route becomes req.params.id
     * - parseInt converts string to number
     */
    const bookId = parseInt(req.params.id);

    if (isNaN(bookId)) {
      return res.status(400).json({
        error: 'Invalid book ID'
      });
    }

    /**
     * CONCEPT: Sequelize FindByPk Method
     * - findByPk = "find by primary key"
     * - Returns single book or null
     * - More efficient than findAll with where clause
     */
    const book = await Book.findByPk(bookId);

    /**
     * CONCEPT: Conditional Response
     * - Checks if book exists
     * - 404 Not Found if book doesn't exist
     * - 200 OK with book data if found
     */
    if (!book) {
      return res.status(404).json({
        error: 'Book not found'
      });
    }

    res.status(200).json({
      message: 'Book retrieved successfully',
      book: book
    });
  } catch (error) {
    console.error('Error fetching book:', error);
    res.status(500).json({
      error: 'Failed to fetch book',
      message: error.message
    });
  }
};

/**
 * CONCEPT: Controller Function - Update Book
 * - Handles PUT /api/books/:id
 * - Updates existing book record
 * - Returns updated book
 */
exports.updateBook = async (req, res) => {
  try {
    const bookId = parseInt(req.params.id);
    const { title, author } = req.body;

    if (isNaN(bookId)) {
      return res.status(400).json({
        error: 'Invalid book ID'
      });
    }

    /**
     * CONCEPT: Input Validation
     * - Checks if at least one field is provided
     * - Allows partial updates
     */
    if (!title && !author) {
      return res.status(400).json({
        error: 'At least one field (title or author) must be provided'
      });
    }

    /**
     * CONCEPT: Sequelize Update Method
     * - Book.update() updates matching records
     * - Returns [numberOfAffectedRows, affectedRows]
     * - First element is count of updated rows
     */
    const [updated] = await Book.update(
      {
        // Only update fields that are provided
        ...(title && { title: title.trim() }),
        ...(author && { author: author.trim() })
      },
      {
        where: { id: bookId }
      }
    );

    /**
     * CONCEPT: Check Update Result
     * - updated is number of rows affected
     * - 0 means no book found with that ID
     * - 1 means book was successfully updated
     */
    if (updated === 0) {
      return res.status(404).json({
        error: 'Book not found'
      });
    }

    /**
     * CONCEPT: Fetch Updated Record
     * - Retrieves updated book to return to client
     * - Ensures response contains latest data
     */
    const updatedBook = await Book.findByPk(bookId);

    res.status(200).json({
      message: 'Book updated successfully',
      book: updatedBook
    });
  } catch (error) {
    console.error('Error updating book:', error);
    res.status(500).json({
      error: 'Failed to update book',
      message: error.message
    });
  }
};

/**
 * CONCEPT: Controller Function - Delete Book
 * - Handles DELETE /api/books/:id
 * - Removes book from database
 * - Returns 204 No Content on success
 */
exports.deleteBook = async (req, res) => {
  try {
    const bookId = parseInt(req.params.id);

    if (isNaN(bookId)) {
      return res.status(400).json({
        error: 'Invalid book ID'
      });
    }

    /**
     * CONCEPT: Sequelize Destroy Method
     * - Book.destroy() deletes matching records
     * - Returns number of deleted rows
     * - 0 means no book found
     * - 1 means book was deleted
     */
    const deleted = await Book.destroy({
      where: { id: bookId }
    });

    if (deleted === 0) {
      return res.status(404).json({
        error: 'Book not found'
      });
    }

    /**
     * CONCEPT: HTTP Status Code 204
     * - 204 No Content: Success with no response body
     * - Standard for DELETE operations
     * - Indicates successful deletion
     */
    res.status(204).send();
  } catch (error) {
    console.error('Error deleting book:', error);
    res.status(500).json({
      error: 'Failed to delete book',
      message: error.message
    });
  }
};
