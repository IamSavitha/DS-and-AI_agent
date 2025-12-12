import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useNavigate, useParams } from 'react-router-dom';
import './App.css';

/**
 * ============================================
 * Q1: REACT BOOK MANAGEMENT APP
 * ============================================
 * 
 * CONCEPTS COVERED:
 * 1. React Router DOM - Client-side routing
 * 2. useState Hook - Component state management
 * 3. useEffect Hook - Side effects and lifecycle
 * 4. Props - Passing data between components
 * 5. Event Handling - User interactions
 * 6. Conditional Rendering - Dynamic UI
 */

// ============================================
// HOME COMPONENT - Displays all books
// ============================================
const Home = ({ books, onDelete }) => {
  /**
   * CONCEPT: Functional Component with Props
   * - Receives 'books' array and 'onDelete' function as props
   * - Props allow parent component (App) to pass data down
   */
  
  return (
    <div className="container mt-5">
      <h1 className="mb-4">📚 Book Management System</h1>
      
      {/* Navigation Links */}
      <div className="mb-4">
        <Link to="/create" className="btn btn-primary me-2">
          ➕ Add New Book
        </Link>
      </div>

      {/* Books List */}
      {books.length === 0 ? (
        <div className="alert alert-info">
          No books available. Add your first book!
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Author</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {books.map((book) => (
                <tr key={book.id}>
                  <td>{book.id}</td>
                  <td>{book.title}</td>
                  <td>{book.author}</td>
                  <td>
                    <Link 
                      to={`/update/${book.id}`} 
                      className="btn btn-sm btn-warning me-2"
                    >
                      ✏️ Update
                    </Link>
                    <Link 
                      to={`/delete/${book.id}`} 
                      className="btn btn-sm btn-danger"
                    >
                      🗑️ Delete
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

// ============================================
// CREATE BOOK COMPONENT
// ============================================
const CreateBook = ({ onAdd }) => {
  /**
   * CONCEPT: useState Hook
   * - Manages component's local state
   * - Returns [currentValue, setterFunction]
   * - Each state variable is independent
   */
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  
  /**
   * CONCEPT: useNavigate Hook (React Router)
   * - Programmatic navigation
   * - Replaces history.push() from older React Router
   */
  const navigate = useNavigate();

  /**
   * CONCEPT: Event Handler Function
   * - Handles form submission
   * - Prevents default form behavior
   * - Calls parent's onAdd function with new book data
   */
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevents page refresh
    
    if (title.trim() && author.trim()) {
      onAdd({ title: title.trim(), author: author.trim() });
      
      // Reset form
      setTitle('');
      setAuthor('');
      
      // Navigate back to home
      navigate('/');
    }
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-4">➕ Add New Book</h2>
      
      <Link to="/" className="btn btn-secondary mb-3">
        ← Back to Home
      </Link>

      <form onSubmit={handleSubmit} className="card p-4">
        <div className="mb-3">
          <label htmlFor="title" className="form-label">
            Book Title
          </label>
          <input
            type="text"
            className="form-control"
            id="title"
            value={title}
            /**
             * CONCEPT: Controlled Component
             * - Input value is controlled by React state
             * - onChange updates state, which updates input
             * - Single source of truth (React state)
             */
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Enter book title"
            required
          />
        </div>

        <div className="mb-3">
          <label htmlFor="author" className="form-label">
            Author Name
          </label>
          <input
            type="text"
            className="form-control"
            id="author"
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
            placeholder="Enter author name"
            required
          />
        </div>

        <button type="submit" className="btn btn-primary">
          Add Book
        </button>
      </form>
    </div>
  );
};

// ============================================
// UPDATE BOOK COMPONENT
// ============================================
const UpdateBook = ({ books, onUpdate }) => {
  /**
   * CONCEPT: useParams Hook (React Router)
   * - Extracts URL parameters
   * - In this case, gets book ID from URL: /update/:id
   */
  const { id } = useParams();
  const navigate = useNavigate();
  
  /**
   * CONCEPT: Finding data from props
   * - Finds the book to update based on URL parameter
   * - parseInt converts string ID to number
   */
  const book = books.find(b => b.id === parseInt(id));
  
  /**
   * CONCEPT: useState with Initial Value from Props
   * - Initializes state with existing book data
   * - Falls back to empty strings if book not found
   */
  const [title, setTitle] = useState(book ? book.title : '');
  const [author, setAuthor] = useState(book ? book.author : '');

  /**
   * CONCEPT: useEffect Hook
   * - Runs after component renders
   * - Dependency array [book] means it runs when 'book' changes
   * - Updates form fields when book data loads
   */
  useEffect(() => {
    if (book) {
      setTitle(book.title);
      setAuthor(book.author);
    }
  }, [book]);

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (title.trim() && author.trim() && book) {
      onUpdate(parseInt(id), { title: title.trim(), author: author.trim() });
      navigate('/');
    }
  };

  if (!book) {
    return (
      <div className="container mt-5">
        <div className="alert alert-warning">
          Book not found!
        </div>
        <Link to="/" className="btn btn-secondary">
          ← Back to Home
        </Link>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4">✏️ Update Book</h2>
      
      <Link to="/" className="btn btn-secondary mb-3">
        ← Back to Home
      </Link>

      <form onSubmit={handleSubmit} className="card p-4">
        <div className="mb-3">
          <label htmlFor="update-title" className="form-label">
            Book Title
          </label>
          <input
            type="text"
            className="form-control"
            id="update-title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Enter book title"
            required
          />
        </div>

        <div className="mb-3">
          <label htmlFor="update-author" className="form-label">
            Author Name
          </label>
          <input
            type="text"
            className="form-control"
            id="update-author"
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
            placeholder="Enter author name"
            required
          />
        </div>

        <button type="submit" className="btn btn-warning">
          Update Book
        </button>
      </form>
    </div>
  );
};

// ============================================
// DELETE BOOK COMPONENT
// ============================================
const DeleteBook = ({ books, onDelete }) => {
  const { id } = useParams();
  const navigate = useNavigate();
  
  const book = books.find(b => b.id === parseInt(id));

  /**
   * CONCEPT: Event Handler for Delete Action
   * - Confirms deletion with user
   * - Calls parent's onDelete function
   * - Navigates back to home after deletion
   */
  const handleDelete = () => {
    if (book && window.confirm(`Are you sure you want to delete "${book.title}"?`)) {
      onDelete(parseInt(id));
      navigate('/');
    }
  };

  if (!book) {
    return (
      <div className="container mt-5">
        <div className="alert alert-warning">
          Book not found!
        </div>
        <Link to="/" className="btn btn-secondary">
          ← Back to Home
        </Link>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4">🗑️ Delete Book</h2>
      
      <Link to="/" className="btn btn-secondary mb-3">
        ← Back to Home
      </Link>

      <div className="card p-4">
        <div className="alert alert-danger">
          <h5>Are you sure you want to delete this book?</h5>
          <p className="mb-0">
            <strong>Title:</strong> {book.title}<br />
            <strong>Author:</strong> {book.author}
          </p>
        </div>

        <button 
          onClick={handleDelete} 
          className="btn btn-danger me-2"
        >
          Delete Book
        </button>
        <Link to="/" className="btn btn-secondary">
          Cancel
        </Link>
      </div>
    </div>
  );
};

// ============================================
// MAIN APP COMPONENT
// ============================================
const App = () => {
  /**
   * CONCEPT: useState for Array State
   * - Manages list of books
   * - Initial state is empty array
   * - Each book has: id, title, author
   */
  const [books, setBooks] = useState([]);
  
  /**
   * CONCEPT: Auto-increment ID Counter
   * - Tracks next available ID
   * - Increments each time a book is added
   */
  const [nextId, setNextId] = useState(1);

  /**
   * CONCEPT: useEffect for Initialization
   * - Runs once on component mount (empty dependency array [])
   * - Can be used to load data from localStorage or API
   * - In this case, initializes with empty array
   */
  useEffect(() => {
    // Could load from localStorage or API here
    // For now, starting with empty array
    console.log('App component mounted');
  }, []);

  /**
   * CONCEPT: Callback Function - Add Book
   * - Receives new book data (without ID)
   * - Creates new book object with auto-incremented ID
   * - Updates state using functional update pattern
   * - setBooks(prevBooks => [...]) ensures immutability
   */
  const handleAddBook = (newBook) => {
    const book = {
      id: nextId,
      ...newBook
    };
    
    /**
     * CONCEPT: Functional State Update
     * - Uses previous state to calculate new state
     * - Spread operator (...) creates new array
     * - Maintains immutability (doesn't mutate original array)
     */
    setBooks(prevBooks => [...prevBooks, book]);
    setNextId(prevId => prevId + 1);
  };

  /**
   * CONCEPT: Callback Function - Update Book
   * - Finds book by ID and updates it
   * - Uses map() to create new array with updated book
   * - Spread operator creates new book object
   */
  const handleUpdateBook = (id, updatedData) => {
    setBooks(prevBooks =>
      prevBooks.map(book =>
        book.id === id ? { ...book, ...updatedData } : book
      )
    );
  };

  /**
   * CONCEPT: Callback Function - Delete Book
   * - Filters out book with matching ID
   * - Creates new array without deleted book
   * - Maintains immutability
   */
  const handleDeleteBook = (id) => {
    setBooks(prevBooks => prevBooks.filter(book => book.id !== id));
  };

  /**
   * CONCEPT: React Router Setup
   * - BrowserRouter enables client-side routing
   * - Routes define URL paths and components
   * - Link components provide navigation
   * - Props are passed to child components
   */
  return (
    <Router>
      <div className="App">
        <Routes>
          {/* Root route - Home page */}
          <Route 
            path="/" 
            element={
              <Home 
                books={books} 
                onDelete={handleDeleteBook} 
              />
            } 
          />
          
          {/* Create route */}
          <Route 
            path="/create" 
            element={<CreateBook onAdd={handleAddBook} />} 
          />
          
          {/* Update route with dynamic ID parameter */}
          <Route 
            path="/update/:id" 
            element={
              <UpdateBook 
                books={books} 
                onUpdate={handleUpdateBook} 
              />
            } 
          />
          
          {/* Delete route with dynamic ID parameter */}
          <Route 
            path="/delete/:id" 
            element={
              <DeleteBook 
                books={books} 
                onDelete={handleDeleteBook} 
              />
            } 
          />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
