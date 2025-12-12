# 📖 Key Terms Glossary - Homework 4

## React Concepts (Q1)

### **React**
A JavaScript library for building user interfaces by creating reusable components that manage their own state.

### **Component**
A reusable piece of UI code that returns JSX (JavaScript XML) to render on the screen, like a building block for your webpage.

### **JSX (JavaScript XML)**
A syntax extension that lets you write HTML-like code in JavaScript, making it easier to describe what the UI should look like.

### **Functional Component**
A component written as a JavaScript function that returns JSX, the modern way to write React components.

### **Props (Properties)**
Data passed from a parent component to a child component, like passing arguments to a function, allowing components to receive and use data.

### **State**
Data that can change over time in a component, stored using `useState` hook, causing the component to re-render when it updates.

### **useState Hook**
A React hook that lets you add state to functional components, returning the current state value and a function to update it.

### **useEffect Hook**
A React hook that lets you perform side effects (like fetching data, updating the DOM) after the component renders.

### **React Router DOM**
A library that enables client-side routing in React applications, allowing navigation between different pages without full page reloads.

### **BrowserRouter**
A React Router component that enables routing functionality by wrapping your app and managing browser history.

### **Route**
A component that renders a specific component when the URL matches a certain path, like `/create` or `/update/:id`.

### **Link Component**
A React Router component that creates navigation links without causing a full page reload, like an anchor tag but for single-page apps.

### **useNavigate Hook**
A React Router hook that provides a function to programmatically navigate to different routes, like redirecting after form submission.

### **useParams Hook**
A React Router hook that extracts URL parameters (like `:id` in `/update/:id`) from the current route.

### **Controlled Component**
An input element whose value is controlled by React state, ensuring React is the single source of truth for the input's value.

### **Event Handler**
A function that runs when a user interacts with the UI (like clicking a button or typing in an input), handling user actions.

### **Conditional Rendering**
Displaying different UI based on certain conditions, like showing an error message only when there's an error.

### **Array.map()**
A JavaScript method that creates a new array by calling a function on each element, commonly used to render lists of items in React.

### **Array.filter()**
A JavaScript method that creates a new array with elements that pass a test, used to remove items from lists.

### **Spread Operator (...)**
A JavaScript operator that expands arrays or objects, used to create new arrays/objects without mutating the original.

### **Immutability**
The practice of not modifying data directly, instead creating new copies with changes, which React requires for proper re-rendering.

### **Re-render**
When React updates the UI because state or props changed, efficiently updating only the parts of the DOM that changed.

---

## MySQL & Sequelize Concepts (Q2)

### **MySQL**
A popular relational database management system that stores data in tables with rows and columns, using SQL (Structured Query Language).

### **Relational Database**
A database that organizes data into tables (relations) that can be linked together using relationships, ensuring data integrity.

### **ORM (Object-Relational Mapping)**
A technique that lets you interact with databases using object-oriented code instead of writing SQL queries directly.

### **Sequelize**
A Node.js ORM for MySQL, PostgreSQL, SQLite, and other databases that provides an easy way to work with databases using JavaScript.

### **Model**
A Sequelize class that represents a database table, defining the structure (columns) and providing methods to interact with the table.

### **Schema**
The structure of a database table, defining what columns exist, their data types, and constraints (like required fields).

### **DataTypes**
Sequelize types that define what kind of data a column stores (STRING, INTEGER, BOOLEAN, DATE, etc.).

### **Primary Key**
A unique identifier for each row in a table, automatically used to find specific records efficiently.

### **Auto Increment**
A database feature that automatically generates sequential numbers for primary keys (1, 2, 3, ...) when new records are created.

### **Validation**
Rules that ensure data meets certain requirements before being saved (like "title cannot be empty" or "email must be valid").

### **Timestamps**
Automatic fields (createdAt, updatedAt) that track when a record was created and last modified, managed by Sequelize.

### **Sequelize Instance**
A connection object that represents your database connection, used to define models and execute queries.

### **Connection Pool**
A cache of database connections that are reused, improving performance by avoiding the overhead of creating new connections.

### **Model.define()**
A Sequelize method that creates a model (table definition) with specified columns, data types, and validation rules.

### **Model.create()**
A Sequelize method that creates a new record in the database, inserting a new row into the table.

### **Model.findAll()**
A Sequelize method that retrieves all records from a table, returning an array of model instances.

### **Model.findByPk()**
A Sequelize method that finds a single record by its primary key (id), more efficient than searching all records.

### **Model.update()**
A Sequelize method that updates existing records matching certain conditions, modifying data in the database.

### **Model.destroy()**
A Sequelize method that deletes records from the database, removing rows from the table.

### **Where Clause**
A condition that filters which records are affected by a query (like "where id = 5" to find a specific book).

### **Async/Await**
JavaScript syntax for handling asynchronous operations, making code that waits for database operations easier to read and write.

### **Promise**
An object representing the eventual result of an asynchronous operation, like a database query that will complete in the future.

---

## Express.js & API Concepts (Q2)

### **Express.js**
A minimal web framework for Node.js that simplifies building web servers and APIs, handling HTTP requests and responses.

### **RESTful API**
An API that follows REST principles, using standard HTTP methods (GET, POST, PUT, DELETE) to perform operations on resources.

### **Endpoint**
A specific URL path that performs a particular action, like `/api/books` for book operations.

### **HTTP Methods**
Verbs that indicate what action to perform: GET (read), POST (create), PUT (update), DELETE (remove).

### **Route Parameter**
A dynamic part of a URL (like `:id` in `/api/books/:id`) that captures values from the URL path.

### **Request Body (req.body)**
Data sent in the request (usually JSON), containing information like book title and author when creating a new book.

### **Response (res)**
An object used to send data back to the client, including status codes, JSON data, or error messages.

### **HTTP Status Codes**
Numbers that indicate the result of a request: 200 (success), 201 (created), 400 (bad request), 404 (not found), 500 (server error).

### **Middleware**
Functions that execute during the request-response cycle, processing requests before they reach route handlers (like parsing JSON).

### **CORS (Cross-Origin Resource Sharing)**
A security feature that allows web pages to make requests to a different domain, enabled by cors middleware.

### **express.json()**
Middleware that parses JSON request bodies, making the data available in `req.body` as a JavaScript object.

### **Router**
A mini Express application that handles routes for a specific resource, keeping code organized and modular.

### **Controller**
Functions that contain the business logic for handling requests, processing data, and sending responses.

### **MVC Pattern (Model-View-Controller)**
An architectural pattern that separates code into Models (data), Views (presentation), and Controllers (logic).

### **Environment Variables**
Configuration values stored outside the code (in `.env` file), keeping sensitive data like database passwords secure.

### **dotenv**
A package that loads environment variables from a `.env` file into `process.env`, making configuration management easier.

---

## MCP Server Concepts (Q3)

### **MCP (Model Context Protocol)**
A protocol that allows AI assistants (like Claude) to interact with external tools and services, extending their capabilities.

### **MCP Server**
A server application that implements the MCP protocol, providing tools that AI assistants can call to perform actions.

### **Tool**
A function exposed by an MCP server that an AI assistant can call, like searching for recipes or fetching data from an API.

### **TheMealDB API**
A free, open API that provides recipe data, meal information, and cooking instructions without requiring authentication.

### **API Endpoint**
A specific URL on an API server that returns data or performs an action, like `https://www.themealdb.com/api/json/v1/1/search.php`.

### **API Key**
A unique identifier used to authenticate API requests, though TheMealDB uses a test key "1" for development.

### **JSON (JavaScript Object Notation)**
A lightweight data format for exchanging information, commonly used by APIs to send and receive data.

### **HTTP Request**
A message sent to a server asking for data or to perform an action, like fetching recipe information.

### **HTTP Response**
A message sent back from a server containing the requested data or confirmation of an action.

### **Async Function**
A function that can perform operations that take time (like API calls) without blocking other code from running.

### **Fetch API**
A browser/Node.js API for making HTTP requests to fetch resources from a server, commonly used to call external APIs.

### **Error Handling**
Code that catches and handles errors gracefully, preventing crashes and providing useful error messages.

### **Rate Limiting**
Restrictions on how many API requests can be made in a certain time period, preventing abuse of the API.

### **Data Transformation**
Converting data from one format to another, like extracting specific fields from an API response to return only needed information.

---

## General Programming Concepts

### **CRUD Operations**
The four basic database operations: **C**reate (add new), **R**ead (retrieve), **U**pdate (modify), **D**elete (remove).

### **Single Page Application (SPA)**
A web application that loads once and dynamically updates content without full page reloads, providing a smoother user experience.

### **Client-Side Routing**
Navigation between different views in a single-page application without requesting new HTML pages from the server.

### **Server-Side Rendering (SSR)**
When the server generates complete HTML pages before sending them to the browser, as opposed to client-side rendering.

### **Client-Side Rendering (CSR)**
When the browser builds the HTML using JavaScript after receiving the page, as React does.

### **API Integration**
Connecting your application to external services (like TheMealDB) to fetch or send data, extending functionality.

### **Modular Code**
Code organized into separate files and functions, making it easier to maintain, test, and reuse.

### **Separation of Concerns**
Organizing code so each part has a single responsibility (models handle data, controllers handle logic, routes handle routing).

### **Error Handling**
Code that anticipates and gracefully handles errors, preventing crashes and providing helpful feedback to users.

### **Input Validation**
Checking that user input meets requirements (not empty, correct format, within limits) before processing it.

### **Environment Configuration**
Storing settings (like database credentials) in environment variables instead of hardcoding them in the source code.

---

## Database Concepts

### **Database**
A structured collection of data stored electronically, organized for easy access, management, and updating.

### **Table**
A collection of related data organized in rows and columns, like a spreadsheet, where each row is a record and each column is a field.

### **Row (Record)**
A single entry in a table, representing one complete item (like one book with id, title, and author).

### **Column (Field)**
A specific piece of information in a table (like "title" or "author"), defining what type of data is stored.

### **Query**
A request to retrieve or manipulate data in a database, like "get all books" or "find book with id 5".

### **SQL (Structured Query Language)**
A programming language designed for managing data in relational databases, though ORMs like Sequelize write it for you.

### **Transaction**
A sequence of database operations that must all succeed or all fail together, ensuring data consistency.

### **Migration**
Scripts that modify the database schema (structure) in a controlled way, tracking changes over time.

### **Seed Data**
Initial data inserted into a database for testing or to provide starting content for an application.

---

## HTTP & Network Concepts

### **HTTP (HyperText Transfer Protocol)**
The protocol used for communication between web browsers and servers, defining how requests and responses work.

### **GET Request**
An HTTP method used to retrieve data from a server, like fetching a list of books (should not modify data).

### **POST Request**
An HTTP method used to send data to a server to create a new resource, like adding a new book.

### **PUT Request**
An HTTP method used to update an existing resource, like modifying a book's information.

### **DELETE Request**
An HTTP method used to remove a resource, like deleting a book from the database.

### **Status Code**
A three-digit number in an HTTP response indicating the result: 200 (OK), 201 (Created), 400 (Bad Request), 404 (Not Found), 500 (Server Error).

### **JSON Response**
Data sent back from a server in JSON format, easily parseable by JavaScript applications.

### **Request Headers**
Metadata sent with HTTP requests, containing information like content type, authentication tokens, etc.

### **Response Headers**
Metadata sent with HTTP responses, containing information like content type, cache control, etc.

---

## Development Tools & Practices

### **npm (Node Package Manager)**
A tool for installing and managing JavaScript packages (libraries) used in Node.js projects.

### **package.json**
A file that lists project dependencies (packages needed), scripts, and project metadata.

### **node_modules**
A folder containing all installed packages and their dependencies, created when you run `npm install`.

### **Development Server**
A local server running on your computer for testing applications during development, typically on localhost.

### **Production Build**
An optimized version of your application with minified code, ready for deployment to users.

### **Hot Reload**
A development feature that automatically refreshes the browser when code changes, speeding up development.

### **Debugging**
The process of finding and fixing errors in code, using tools like console.log, breakpoints, and error messages.

### **Version Control**
Tracking changes to code over time using tools like Git, allowing you to revert changes and collaborate.

---

## Real-World Analogies

### **React Components = Building Blocks**
Think of React components like LEGO blocks - each block (component) is a reusable piece that you combine to build a complete structure (application).

### **State = Memory**
State is like a component's memory - it remembers information that can change, and when it changes, the component updates to reflect the new information.

### **Props = Instructions**
Props are like instructions passed from a parent to a child - "Here's the data you need to display" or "Here's the function to call when clicked."

### **React Router = GPS Navigation**
React Router is like GPS navigation - it knows where you are (current route) and can take you to different places (routes) without starting over.

### **Database = Filing Cabinet**
A database is like a well-organized filing cabinet - tables are drawers, rows are folders, and columns are labels on the folders.

### **ORM = Translator**
An ORM is like a translator - you speak JavaScript, and it translates your commands into SQL that the database understands.

### **API = Waiter**
An API is like a waiter in a restaurant - you make a request (order), and it brings back what you asked for (data) from the kitchen (server).

### **Middleware = Assembly Line**
Middleware is like stations on an assembly line - each station (middleware) processes the request before it reaches the final destination (route handler).

### **MCP Server = Toolbox**
An MCP server is like a toolbox for AI assistants - it provides tools (functions) that the assistant can use to accomplish tasks it couldn't do alone.

---

## Quick Reference: Most Important Terms

### React (Q1)
1. **Component** = Reusable UI building block
2. **Props** = Data passed to components
3. **State** = Changeable data in components
4. **useState** = Hook to manage state
5. **useEffect** = Hook for side effects
6. **React Router** = Client-side navigation
7. **Route** = URL path to component mapping
8. **Link** = Navigation without page reload

### MySQL/Sequelize (Q2)
1. **ORM** = Object-Relational Mapping tool
2. **Model** = Database table representation
3. **Sequelize** = Node.js ORM for databases
4. **create()** = Insert new record
5. **findAll()** = Get all records
6. **findByPk()** = Find by primary key
7. **update()** = Modify existing record
8. **destroy()** = Delete record

### Express.js (Q2)
1. **Route** = URL path handler
2. **Controller** = Business logic function
3. **Middleware** = Request processor
4. **req.body** = Request data
5. **res.json()** = Send JSON response
6. **Status Code** = Request result indicator

### MCP Server (Q3)
1. **MCP** = Model Context Protocol
2. **Tool** = Function AI can call
3. **API** = External service interface
4. **Endpoint** = Specific API URL
5. **JSON** = Data format
6. **Async** = Non-blocking operations

### General
1. **CRUD** = Create, Read, Update, Delete
2. **SPA** = Single Page Application
3. **API** = Application Programming Interface
4. **HTTP** = Web communication protocol
5. **JSON** = JavaScript Object Notation
6. **Async/Await** = Asynchronous code handling

---

## Study Tips

1. **Start with React basics** - Understand components, props, and state before diving into routing
2. **Practice with small examples** - Build simple components before complex applications
3. **Understand the data flow** - Know how data moves from parent to child (props) and how state updates trigger re-renders
4. **Learn Sequelize methods** - Memorize the basic CRUD operations (create, findAll, findByPk, update, destroy)
5. **Practice API calls** - Understand how to make HTTP requests and handle responses
6. **Read error messages** - They often tell you exactly what's wrong
7. **Use console.log()** - Print values to understand what your code is doing
8. **Break problems into steps** - Don't try to build everything at once

---

*This glossary covers all major concepts in Homework 4. Refer to it when you encounter unfamiliar terms while reading the code or documentation.*
