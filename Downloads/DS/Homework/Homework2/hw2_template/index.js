/**
 * ============================================================================
 * HOMEWORK 2: BOOK STORE APPLICATION
 * ============================================================================
 * 
 * CONCEPTS COVERED:
 * 1. REST API (Representational State Transfer)
 * 2. Express.js Framework
 * 3. HTTP Methods (GET, POST)
 * 4. Middleware (body-parser, static files)
 * 5. EJS Templating Engine (Server-Side Rendering)
 * 6. CRUD Operations (Create, Read, Update, Delete)
 * 7. Request/Response Cycle
 * 8. URL Routing
 * 9. Form Handling
 * 
 * ============================================================================
 */

// ============================================================================
// STEP 1: IMPORT REQUIRED MODULES
// ============================================================================
// Express.js is a minimal and flexible Node.js web application framework
// that provides a robust set of features for web and mobile applications.
// It simplifies server creation and routing.
const express = require('express');

// Create an Express application instance
// This app object has methods for routing HTTP requests, configuring middleware,
// rendering HTML views, and registering a template engine.
const app = express();

// Body-parser is middleware that extracts the entire body portion of an incoming
// request stream and makes it available on req.body. It's essential for
// processing form data and JSON payloads.
const bodyParser = require('body-parser');

// ============================================================================
// STEP 2: CONFIGURE VIEW ENGINE (EJS - Embedded JavaScript)
// ============================================================================
// EJS (Embedded JavaScript) is a templating engine that lets you generate
// HTML markup with plain JavaScript. It allows server-side rendering where
// the server generates HTML before sending it to the client.

// Set EJS as the view engine for rendering templates
// When you call res.render(), Express will look for .ejs files
app.set('view engine', 'ejs');

// Specify the directory where EJS templates are stored
// Express will look in './views' folder for template files
app.set('views', './views');

// ============================================================================
// STEP 3: CONFIGURE STATIC FILES MIDDLEWARE
// ============================================================================
// Static files (CSS, JavaScript, images) are served directly without processing.
// The express.static middleware serves static files from the specified directory.
// __dirname is a Node.js global that contains the absolute path of the
// directory containing the currently executing file.
app.use(express.static(__dirname + '/public'));

// ============================================================================
// STEP 4: CONFIGURE BODY PARSER MIDDLEWARE
// ============================================================================
// Middleware functions are functions that have access to the request object (req),
// the response object (res), and the next middleware function in the application's
// request-response cycle.

// Parse JSON payloads in request bodies
// When a client sends JSON data (Content-Type: application/json),
// this middleware parses it and makes it available in req.body
app.use(bodyParser.json());

// Parse URL-encoded payloads (form data)
// When a client submits a form (Content-Type: application/x-www-form-urlencoded),
// this middleware parses it and makes it available in req.body
// extended: true allows parsing of rich objects and arrays
app.use(bodyParser.urlencoded({ extended: true }));

// ============================================================================
// STEP 5: IN-MEMORY DATA STORAGE
// ============================================================================
// In a real application, data would be stored in a database (MongoDB, PostgreSQL, etc.)
// For this homework, we use an in-memory array to simulate a database.
// Note: This data is lost when the server restarts (not persistent).

// Initialize books array with default data
// Each book object has three properties: BookID, Title, and Author
var books = [
    { "BookID": "1", "Title": "Book 1", "Author": "Author 1" },
    { "BookID": "2", "Title": "Book 2", "Author": "Author 2" },
    { "BookID": "3", "Title": "Book 3", "Author": "Author 3" }
];

// ============================================================================
// STEP 6: ROUTING - DEFINE API ENDPOINTS
// ============================================================================
// Routes define how the application responds to client requests to a particular
// endpoint, which is a URI (or path) and a specific HTTP request method (GET, POST, etc.)

// ----------------------------------------------------------------------------
// ROUTE 1: GET / (Root Route - Home Page)
// ----------------------------------------------------------------------------
// HTTP GET method is used to retrieve data. It's idempotent (safe to call multiple times).
// This route renders the home page showing all books.

// app.get() defines a route handler for GET requests
// First parameter: URL path ('/' means root/home page)
// Second parameter: Callback function that handles the request
//   - req: Request object (contains data about the HTTP request)
//   - res: Response object (used to send response back to client)
app.get('/', function (req, res) {
    // res.render() renders an EJS template
    // First parameter: name of the template file (without .ejs extension)
    // Second parameter: object containing data to pass to the template
    // The template can access 'books' variable in the EJS file
    res.render('home', {
        books: books
    });
});

// ----------------------------------------------------------------------------
// ROUTE 2: GET /add-book (Display Create Book Form)
// ----------------------------------------------------------------------------
// This route renders the form page where users can input new book information.
// GET is used here because we're just displaying a form (not submitting data yet).
app.get('/add-book', function (req, res) {
    // Render the create.ejs template
    // No data needs to be passed since it's just an empty form
    res.render('create');
});

// ----------------------------------------------------------------------------
// ROUTE 3: POST /add-book (Create New Book)
// ----------------------------------------------------------------------------
// HTTP POST method is used to submit data to be processed (create new resource).
// This route handles the form submission from the create page.

// app.post() defines a route handler for POST requests
app.post('/add-book', function (req, res) {
    // Extract form data from request body
    // req.body contains the parsed form data thanks to body-parser middleware
    // The field names (BookID, Title, Author) match the 'name' attributes in the form
    const { BookID, Title, Author } = req.body;
    
    // Input validation: Check if required fields are provided
    // trim() removes whitespace from both ends of a string
    if (!BookID || !Title || !Author) {
        // Return error response with status code 400 (Bad Request)
        return res.status(400).send('All fields (BookID, Title, Author) are required');
    }
    
    // Check if BookID already exists (prevent duplicates)
    const existingBook = books.find(book => book.BookID === BookID);
    if (existingBook) {
        return res.status(400).send('Book with this ID already exists');
    }
    
    // Create new book object
    // The object structure matches our books array format
    const newBook = {
        "BookID": BookID.trim(),
        "Title": Title.trim(),
        "Author": Author.trim()
    };
    
    // Add the new book to the books array
    books.push(newBook);
    
    // Redirect to home page after successful creation
    // res.redirect() sends an HTTP redirect response (status 302)
    // The client's browser will automatically make a GET request to '/'
    // This shows the updated list of books including the newly added one
    res.redirect('/');
});

// ----------------------------------------------------------------------------
// ROUTE 4: GET /update-book (Display Update Book Form)
// ----------------------------------------------------------------------------
// This route renders the form page where users can update existing book information.
app.get('/update-book', function (req, res) {
    // Render the update.ejs template
    // We could optionally pass the books array to show a dropdown of existing books
    res.render('update', {
        books: books  // Pass books so user can see which books exist
    });
});

// ----------------------------------------------------------------------------
// ROUTE 5: POST /update-book (Update Existing Book)
// ----------------------------------------------------------------------------
// This route handles the form submission to update an existing book.
app.post('/update-book', function (req, res) {
    // Extract form data from request body
    const { BookID, Title, Author } = req.body;
    
    // Input validation
    if (!BookID || !Title || !Author) {
        return res.status(400).send('All fields (BookID, Title, Author) are required');
    }
    
    // Find the book to update
    // Array.find() returns the first element that satisfies the condition
    // If no book is found, it returns undefined
    const book = books.find(book => book.BookID === BookID.trim());
    
    // Check if book exists
    if (!book) {
        // Return 404 (Not Found) status code if book doesn't exist
        return res.status(404).send('Book not found');
    }
    
    // Update the book's properties
    // We modify the existing object in the array (mutation)
    book.Title = Title.trim();
    book.Author = Author.trim();
    
    // Redirect to home page to show updated list
    res.redirect('/');
});

// ----------------------------------------------------------------------------
// ROUTE 6: GET /delete-book (Display Delete Book Form)
// ----------------------------------------------------------------------------
// This route renders the form page where users can delete a book.
app.get('/delete-book', function (req, res) {
    // Render the delete.ejs template
    res.render('delete', {
        books: books  // Pass books so user can see which books can be deleted
    });
});

// ----------------------------------------------------------------------------
// ROUTE 7: POST /delete-book (Delete Existing Book)
// ----------------------------------------------------------------------------
// This route handles the deletion of a book.
app.post('/delete-book', function (req, res) {
    // Extract BookID from request body
    const { BookID } = req.body;
    
    // Input validation
    if (!BookID) {
        return res.status(400).send('BookID is required');
    }
    
    // Find the index of the book to delete
    // Array.findIndex() returns the index of the first element that satisfies the condition
    // Returns -1 if no element is found
    const bookIndex = books.findIndex(book => book.BookID === BookID.trim());
    
    // Check if book exists
    if (bookIndex === -1) {
        return res.status(404).send('Book not found');
    }
    
    // Remove the book from the array
    // Array.splice() changes the contents of an array by removing or replacing elements
    // First parameter: index to start at
    // Second parameter: number of elements to remove
    books.splice(bookIndex, 1);
    
    // Redirect to home page to show updated list
    res.redirect('/');
});

// ============================================================================
// STEP 7: START THE SERVER
// ============================================================================
// app.listen() binds and listens for connections on the specified host and port.
// When the server starts, it will listen for incoming HTTP requests on port 5000.

// Port 5000 is where our server will be accessible
// You can access the application at http://localhost:5000
// If port 5000 is in use, the server will try port 3000 as fallback
const PORT = process.env.PORT || 5000;

const server = app.listen(PORT, function () {
    console.log("Server listening on port " + PORT);
    console.log("Open http://localhost:" + PORT + " in your browser");
});

// Error handling for port conflicts
server.on('error', function(err) {
    if (err.code === 'EADDRINUSE') {
        console.log(`Port ${PORT} is already in use. Trying port 3000...`);
        const fallbackPort = 3000;
        app.listen(fallbackPort, function() {
            console.log("Server listening on port " + fallbackPort);
            console.log("Open http://localhost:" + fallbackPort + " in your browser");
        });
    } else {
        console.error('Server error:', err);
    }
});
