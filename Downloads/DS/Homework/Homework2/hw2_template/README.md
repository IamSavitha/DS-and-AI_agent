# 📚 Homework 2: Book Store Application

A complete CRUD (Create, Read, Update, Delete) web application built with Node.js, Express.js, and EJS templating.

## 🚀 Quick Start

### Prerequisites
- Node.js installed (v12 or higher)
- npm (comes with Node.js)

### Installation

1. Navigate to the project directory:
```bash
cd hw2_template
```

2. Install dependencies:
```bash
npm install
```

3. Start the server:
```bash
node index.js
```

4. Open your browser and visit:
```
http://localhost:5000
```

## 📁 Project Structure

```
hw2_template/
├── index.js                    # Main server file with all routes
├── package.json                # Project dependencies
├── views/                      # EJS templates
│   ├── home.ejs               # Home page (list all books)
│   ├── create.ejs             # Add new book form
│   ├── update.ejs             # Update book form
│   └── delete.ejs             # Delete book form
├── public/                     # Static files
│   └── css/
│       └── styles.css         # Application styles
└── README.md                   # This file
```

## ✨ Features

- ✅ **View All Books**: Display list of all books in a table
- ✅ **Add New Book**: Create new book entries
- ✅ **Update Book**: Modify existing book information
- ✅ **Delete Book**: Remove books from the collection

## 🎯 Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Home page - displays all books |
| GET | `/add-book` | Display form to add new book |
| POST | `/add-book` | Create a new book |
| GET | `/update-book` | Display form to update book |
| POST | `/update-book` | Update an existing book |
| GET | `/delete-book` | Display form to delete book |
| POST | `/delete-book` | Delete a book |

## 📖 Concepts Covered

This homework demonstrates:

1. **REST API Principles** - Resource-based routing
2. **Express.js Framework** - Web application structure
3. **HTTP Methods** - GET and POST requests
4. **Middleware** - Body-parser, static files
5. **EJS Templating** - Server-side rendering
6. **CRUD Operations** - Complete data management
7. **Form Handling** - User input processing
8. **Request/Response Cycle** - Web request flow

## 📚 Detailed Documentation

For comprehensive explanations of all concepts, see:
- **[HW2_CONCEPTS_EXPLANATION.md](./HW2_CONCEPTS_EXPLANATION.md)** - Complete concept breakdown with line-by-line code explanations

## 🔧 Technologies Used

- **Node.js** - JavaScript runtime
- **Express.js** - Web framework
- **EJS** - Templating engine
- **Body-parser** - Request body parsing middleware
- **HTML/CSS** - Frontend markup and styling

## 📝 Default Data

The application starts with 3 default books:
- Book 1 by Author 1
- Book 2 by Author 2
- Book 3 by Author 3

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is already in use, change it in `index.js`:
```javascript
app.listen(3000, function () {  // Change 5000 to 3000 or another port
    console.log("Server listening on port 3000");
});
```

### Module Not Found
Run `npm install` to install all dependencies.

### CSS Not Loading
Ensure the `public` directory path is correct in `index.js`.

## 📄 License

This is a homework assignment for educational purposes.
