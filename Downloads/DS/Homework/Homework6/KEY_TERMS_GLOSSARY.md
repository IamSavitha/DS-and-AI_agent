# 📖 Key Terms Glossary - Simple One-Line Definitions

## Core Web Development Terms

### **Full-Stack Application**
An application that has both a frontend (what users see) and a backend (server that processes data), working together to create a complete system.

### **MERN Stack**
A technology stack using **M**ongoDB (database), **E**xpress.js (backend), **R**eact (frontend), and **N**ode.js (runtime) to build web applications.

### **Framework**
A pre-built structure that provides tools and rules to build applications faster, so you don't have to write everything from scratch.

### **Express.js**
A Node.js framework that makes it easy to create web servers and handle HTTP requests/responses.

### **React**
A JavaScript library for building user interfaces, especially for creating interactive web pages with components.

### **Node.js**
A JavaScript runtime environment that lets you run JavaScript on the server (outside the browser).

---

## Database & NoSQL Terms

### **MongoDB**
A NoSQL document database that stores data as flexible JSON-like documents instead of rigid tables.

### **NoSQL**
A type of database that doesn't use tables and rows like traditional SQL databases, offering more flexibility in data structure.

### **Document**
A record in MongoDB, stored as a JSON-like object (like `{ name: "Laptop", price: 999.99 }`).

### **Collection**
A group of documents in MongoDB (similar to a table in SQL databases).

### **Schema**
A blueprint that defines the structure, validation rules, and data types for documents in a collection.

### **Mongoose**
An Object Document Mapper (ODM) library that provides structure and validation for MongoDB, making it easier to work with.

### **ODM (Object Document Mapper)**
A tool that translates between objects in your code and documents in the database, like a translator between JavaScript and MongoDB.

### **Model**
A Mongoose class that represents a collection and provides methods to interact with documents (like `Product.find()`, `Product.save()`).

### **ObjectId**
A unique identifier automatically created by MongoDB for each document (like `_id: "507f1f77bcf86cd799439011"`).

---

## Express.js & Backend Terms

### **Middleware**
Functions that run between receiving a request and sending a response, like a checkpoint that processes data before it reaches your route handler.

### **Route**
A URL path (like `/api/products`) that tells the server what to do when someone visits that address.

### **Route Handler**
The function that runs when a specific route is accessed, containing the code that processes the request and sends a response.

### **Router**
A mini Express app that groups related routes together, helping organize code into separate files.

### **app.use()**
An Express method that applies middleware to all incoming requests or mounts routers at specific paths.

### **req.body**
An object containing data sent in the request body (form data or JSON), made available by express.json() middleware.

### **req.params**
An object containing route parameters (like `:id` in `/api/products/:id` becomes `req.params.id`).

### **res.json()**
An Express method that sends a JSON response to the client (converts JavaScript objects to JSON format).

### **res.status()**
An Express method that sets the HTTP status code (like 200 for success, 404 for not found, 201 for created).

### **CORS (Cross-Origin Resource Sharing)**
A security feature that allows web pages from one origin (like localhost:3000) to request resources from another origin (like localhost:5000).

---

## React & Frontend Terms

### **Component**
A reusable piece of UI code that represents a part of the webpage (like a form or product card).

### **Functional Component**
A React component written as a JavaScript function (modern way, preferred over class components).

### **JSX (JavaScript XML)**
A syntax extension that lets you write HTML-like code in JavaScript (like `<div>Hello</div>` instead of `React.createElement('div', null, 'Hello')`).

### **State**
Data that can change over time in a React component, causing the component to re-render when updated.

### **useState Hook**
A React hook that lets you add state to functional components (returns current value and a function to update it).

### **useEffect Hook**
A React hook that lets you perform side effects (like API calls) in functional components, similar to lifecycle methods in class components.

### **Hook**
A special function in React that lets you "hook into" React features like state and lifecycle methods.

### **Controlled Component**
An input element whose value is controlled by React state, ensuring React is the single source of truth.

### **Event Handler**
A function that runs when a user interaction occurs (like clicking a button or typing in an input).

### **Props**
Data passed from a parent component to a child component (short for "properties").

### **Re-render**
The process of React updating the UI when state or props change, efficiently updating only what changed.

### **Key**
A special attribute in React lists that helps React identify which items have changed, been added, or removed.

---

## HTTP & API Terms

### **HTTP (HyperText Transfer Protocol)**
The language computers use to communicate over the internet, defining how requests and responses work.

### **REST (Representational State Transfer)**
An architectural style for building web services that uses standard HTTP methods to perform operations on resources.

### **RESTful API**
An API that follows REST principles, using HTTP methods (GET, POST, PUT, DELETE) in a standard way.

### **GET Request**
An HTTP method used to retrieve/read data from the server (like fetching a list of products).

### **POST Request**
An HTTP method used to send data to the server to create something new (like adding a product).

### **PUT Request**
An HTTP method used to update existing data on the server (like modifying a product's price).

### **DELETE Request**
An HTTP method used to remove data from the server (like deleting a product).

### **Endpoint**
A specific URL path that performs a particular action (like `/api/products` for product operations).

### **API (Application Programming Interface)**
A set of rules and endpoints that allow different applications to communicate with each other.

### **JSON (JavaScript Object Notation)**
A lightweight data format for exchanging data, written as key-value pairs (like `{"name": "Laptop", "price": 999.99}`).

### **Request**
An HTTP message sent from the client (browser) to the server asking for data or to perform an action.

### **Response**
An HTTP message sent from the server back to the client containing data or status information.

### **Request Body**
The data sent with a POST or PUT request (like form fields or JSON data).

### **Idempotent**
An operation that produces the same result no matter how many times you run it (GET, PUT, DELETE are idempotent).

---

## HTTP Status Codes

### **200 OK**
HTTP status code meaning the request was successful.

### **201 Created**
HTTP status code meaning a new resource was successfully created.

### **400 Bad Request**
HTTP status code meaning the request was invalid (missing or incorrect data).

### **404 Not Found**
HTTP status code meaning the requested resource doesn't exist.

### **500 Internal Server Error**
HTTP status code meaning something went wrong on the server.

---

## Asynchronous Programming Terms

### **Asynchronous (Async)**
Operations that don't block other code from running while waiting for results (like API calls or database queries).

### **Promise**
An object representing the eventual completion (or failure) of an asynchronous operation.

### **async/await**
Modern JavaScript syntax that makes asynchronous code look and behave more like synchronous code.

### **async Function**
A function declared with the `async` keyword, allowing you to use `await` inside it.

### **await**
A keyword that pauses execution until a Promise resolves, making async code easier to read.

### **Try-Catch Block**
A way to handle errors in JavaScript: code in `try` runs, and if an error occurs, `catch` handles it.

---

## Data Operations Terms

### **CRUD**
The four basic operations: **C**reate, **R**ead, **U**pdate, **D**elete - everything you can do with data.

### **Query**
A request to retrieve data from a database (like `Product.find()` gets all products).

### **Validation**
Checking that data meets certain rules before saving it (like ensuring price is a positive number).

### **Error Handling**
The process of catching and managing errors gracefully, providing useful feedback to users.

---

## Mongoose Methods

### **find()**
A Mongoose method that retrieves all documents matching criteria (or all documents if no criteria).

### **findById()**
A Mongoose method that finds a single document by its unique ID.

### **findByIdAndUpdate()**
A Mongoose method that finds a document by ID and updates it in one operation.

### **findByIdAndDelete()**
A Mongoose method that finds a document by ID and removes it from the collection.

### **save()**
A Mongoose method that saves a new or modified document to the database.

### **new Model()**
Creating a new document instance from a Mongoose model (like `new Product(req.body)`).

---

## Environment & Configuration Terms

### **Environment Variable**
A configuration value stored outside your code (like database connection strings), accessed via `process.env`.

### **.env File**
A file that stores environment variables (like `MONGODB_URI`), kept secret and not committed to version control.

### **dotenv**
A package that loads environment variables from a `.env` file into `process.env`.

### **process.env**
A Node.js object containing environment variables (like `process.env.PORT` or `process.env.MONGODB_URI`).

---

## HTTP Client Terms

### **Axios**
A JavaScript library that makes it easy to send HTTP requests from the browser or Node.js.

### **HTTP Client**
A tool or library used to send HTTP requests (like Axios or the built-in `fetch` API).

### **API Call**
Sending a request to an API endpoint to get or send data (like `axios.get('/api/products')`).

---

## JavaScript Terms Used

### **require()**
A Node.js function that imports/loads a module (like `require('express')` loads the Express framework).

### **import/export**
Modern JavaScript syntax for importing and exporting modules (used in React with ES6 modules).

### **const / let**
Ways to declare variables in JavaScript (const = constant, let = can be reassigned).

### **Arrow Function**
A shorter way to write functions: `() => {}` instead of `function() {}`.

### **Destructuring**
Extracting values from objects/arrays into variables: `const { name, price } = product`.

### **Spread Operator (...)**
Expands an array or object into individual elements: `{...formData, price: 99}` creates a new object with updated price.

### **Template Literal**
A string that can include variables: `` `${API_URL}/${id}` `` instead of `API_URL + '/' + id`.

### **Array.map()**
A method that creates a new array by transforming each element (like converting products to JSX elements).

### **Conditional Rendering**
Displaying different content based on conditions (like `{error && <div>{error}</div>}`).

---

## Form & Input Terms

### **Controlled Input**
An input field whose value is controlled by React state, ensuring React manages the input value.

### **onChange Event**
An event that fires when an input's value changes, used to update React state.

### **onSubmit Event**
An event that fires when a form is submitted, used to handle form submission.

### **preventDefault()**
A method that stops the default browser behavior (like preventing page reload on form submit).

---

## Server Terms

### **Server**
A computer program that listens for requests and sends back responses.

### **Port**
A number (like 5000) that identifies which program on a computer should receive network requests.

### **localhost**
A special address (127.0.0.1) that refers to your own computer, used for testing applications locally.

### **app.listen()**
An Express method that starts the server and makes it wait for incoming requests on a specific port.

---

## Data Structure Terms

### **Array**
A JavaScript data structure that holds a list of items in order, like `[product1, product2, product3]`.

### **Object**
A JavaScript data structure that stores data as key-value pairs, like `{ name: "Laptop", price: 999.99 }`.

### **Key-Value Pair**
A way of storing data where each piece of data has a name (key) and a value (like `name: "Laptop"`).

---

## Real-World Analogy

Think of building a full-stack application like running a restaurant with a kitchen and dining area:

- **Frontend (React)** = The dining area where customers see the menu and place orders
- **Backend (Express)** = The kitchen that receives orders and prepares food
- **Database (MongoDB)** = The pantry where ingredients (data) are stored
- **API Endpoints** = The order window where requests are placed and responses are received
- **Routes** = Different menu sections (appetizers, main course, desserts)
- **Route Handler** = The chef who prepares that specific dish
- **Middleware** = The prep station where ingredients are cleaned before cooking
- **State (React)** = The current order being prepared
- **Component** = A menu item or section
- **Props** = Instructions passed from the menu to the kitchen
- **useEffect** = The process of checking inventory when the restaurant opens
- **Axios** = The waiter who carries orders between dining area and kitchen
- **CORS** = The security system that ensures only authorized waiters can enter the kitchen
- **Schema (Mongoose)** = The recipe card that defines how each dish should be prepared
- **Model** = The standardized way to prepare a specific type of dish
- **Document** = A single prepared dish ready to serve
- **Collection** = All dishes of the same type (all pizzas, all pastas)
- **Query** = Asking the pantry "do we have tomatoes?"
- **async/await** = Waiting for the oven to finish cooking before serving

---

## Quick Reference: Most Important Terms

1. **MERN Stack** = MongoDB + Express + React + Node.js
2. **Component** = Reusable piece of UI
3. **State** = Data that can change in React
4. **useState** = Hook to manage state
5. **useEffect** = Hook for side effects (API calls)
6. **Route** = URL path that triggers code
7. **Middleware** = Functions that process requests
8. **Schema** = Blueprint for database structure
9. **Model** = Mongoose class representing a collection
10. **API** = Set of endpoints for communication
11. **RESTful** = Using HTTP methods in standard way
12. **async/await** = Modern way to handle asynchronous code
13. **CORS** = Allows cross-origin requests
14. **JSON** = Data format for exchanging data
15. **CRUD** = Create, Read, Update, Delete operations
16. **GET** = Retrieve, **POST** = Create, **PUT** = Update, **DELETE** = Remove
17. **Axios** = Library for making HTTP requests
18. **Controlled Component** = Input controlled by React state
19. **Environment Variable** = Configuration stored outside code
20. **Mongoose** = ODM for MongoDB

---

## Comparison: SQL vs NoSQL

| SQL (Traditional) | NoSQL (MongoDB) |
|------------------|-----------------|
| Tables | Collections |
| Rows | Documents |
| Columns | Fields |
| Fixed Schema | Flexible Schema |
| Relationships | Embedded Documents |
| SQL Queries | JavaScript Queries |

---

## Comparison: Class Components vs Functional Components

| Class Components (Old) | Functional Components (Modern) |
|----------------------|-------------------------------|
| `class Component extends React.Component` | `function Component()` |
| `this.state` | `useState()` hook |
| `componentDidMount()` | `useEffect()` hook |
| More verbose | Simpler syntax |
| Harder to understand | Easier to read |

---

## Common Patterns in This Homework

### **Pattern 1: Fetching Data**
```javascript
useEffect(() => {
  fetchProducts();
}, []);
```
- Runs once when component mounts
- Fetches data from API
- Updates state with results

### **Pattern 2: Controlled Input**
```javascript
<input 
  value={formData.name} 
  onChange={(e) => setFormData({...formData, name: e.target.value})}
/>
```
- Input value comes from state
- onChange updates state
- React controls the input

### **Pattern 3: API Call with Error Handling**
```javascript
try {
  const response = await axios.get(API_URL);
  setProducts(response.data);
} catch (error) {
  setError('Failed to fetch');
}
```
- Try to make API call
- On success, update state
- On error, show error message

### **Pattern 4: CRUD Route**
```javascript
router.post('/', async (req, res) => {
  const product = new Product(req.body);
  await product.save();
  res.status(201).json(product);
});
```
- Create new model instance
- Save to database
- Return created document

---

## Study Tips

1. **Understand the flow**: Frontend → API → Backend → Database → Response
2. **Learn async/await**: Essential for API calls and database operations
3. **Practice state management**: Know when and how to update React state
4. **Master Mongoose methods**: find(), save(), findByIdAndUpdate(), etc.
5. **Understand HTTP methods**: When to use GET, POST, PUT, DELETE
6. **Know React hooks**: useState and useEffect are fundamental
7. **Understand CORS**: Why it's needed and how it works
8. **Practice error handling**: Always handle errors gracefully

---

## Additional Resources

- **MongoDB**: Document-based NoSQL database
- **Mongoose**: ODM for MongoDB
- **Express.js**: Web framework for Node.js
- **React**: UI library for building interfaces
- **Axios**: HTTP client library
- **REST API**: Architectural style for web services

---

*This glossary covers all key terms used in Homework 6. Refer to this document when studying or reviewing concepts!*
