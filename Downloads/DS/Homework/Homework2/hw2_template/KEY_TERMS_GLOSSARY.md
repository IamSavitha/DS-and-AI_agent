# 📖 Key Terms Glossary - Simple One-Line Definitions

## Core Web Development Terms

### **Framework**
A pre-built structure that provides tools and rules to build applications faster, so you don't have to write everything from scratch.

### **Express.js**
A Node.js framework that makes it easy to create web servers and handle HTTP requests/responses.

### **Middleware**
Functions that run between receiving a request and sending a response, like a checkpoint that processes data before it reaches your route handler.

### **Route**
A URL path (like `/add-book`) that tells the server what to do when someone visits that address.

### **Route Handler**
The function that runs when a specific route is accessed, containing the code that processes the request and sends a response.

---

## Template & Rendering Terms

### **Template**
An HTML file with placeholders that get filled with actual data before being sent to the browser.

### **Templating Engine**
A tool that takes a template file and data, then generates the final HTML by replacing placeholders with actual values.

### **EJS (Embedded JavaScript)**
A templating engine that lets you write JavaScript code inside HTML files to create dynamic web pages.

### **Render**
The process of taking a template file, filling it with data, and converting it into complete HTML that gets sent to the browser.

### **Server-Side Rendering (SSR)**
When the server creates the complete HTML page before sending it to the browser, rather than the browser building it.

---

## HTTP & Request/Response Terms

### **HTTP (HyperText Transfer Protocol)**
The language computers use to communicate over the internet, defining how requests and responses work.

### **GET Request**
An HTTP method used to retrieve/read data from the server (like viewing a webpage).

### **POST Request**
An HTTP method used to send data to the server to create or modify something (like submitting a form).

### **Request (req)**
An object containing all information about the incoming HTTP request (data, headers, parameters, etc.).

### **Response (res)**
An object used to send data back to the client (HTML, JSON, redirects, status codes, etc.).

### **Request Body**
The data sent with a POST request (like form fields or JSON data).

---

## Data & Storage Terms

### **CRUD**
The four basic operations: **C**reate, **R**ead, **U**pdate, **D**elete - everything you can do with data.

### **In-Memory Storage**
Data stored in the computer's RAM (temporary memory) that disappears when the server restarts.

### **Database**
A permanent storage system for data that persists even after the server restarts (like MongoDB, PostgreSQL).

### **Array**
A JavaScript data structure that holds a list of items in order, like a shopping list.

### **Object**
A JavaScript data structure that stores data as key-value pairs, like a dictionary entry.

---

## Express.js Specific Terms

### **app.get()**
An Express method that defines what happens when someone visits a URL using a GET request.

### **app.post()**
An Express method that defines what happens when someone submits data to a URL using a POST request.

### **app.use()**
An Express method that applies middleware to all incoming requests.

### **res.render()**
An Express method that takes a template file, fills it with data, and sends the resulting HTML to the browser.

### **res.redirect()**
An Express method that sends the browser to a different URL (like going to the home page after submitting a form).

### **res.status()**
An Express method that sets the HTTP status code (like 200 for success, 404 for not found, 400 for bad request).

### **req.body**
An object containing data sent in the request body (form data or JSON), made available by body-parser middleware.

---

## Middleware Terms

### **body-parser**
A middleware that extracts and parses data from request bodies, making it available in `req.body`.

### **express.static()**
A middleware that serves static files (CSS, images, JavaScript) directly without processing them.

### **Static Files**
Files that don't change (like CSS stylesheets, images) that are served as-is to the browser.

---

## JavaScript Terms Used

### **require()**
A Node.js function that imports/loads a module (like `require('express')` loads the Express framework).

### **const / var / let**
Ways to declare variables in JavaScript (const = constant, var = old way, let = modern way).

### **Arrow Function**
A shorter way to write functions: `() => {}` instead of `function() {}`.

### **Destructuring**
Extracting values from objects/arrays into variables: `const { BookID, Title } = req.body`.

### **Array.find()**
A method that searches an array and returns the first item that matches a condition.

### **Array.findIndex()**
A method that searches an array and returns the index (position) of the first item that matches.

### **Array.splice()**
A method that removes or replaces elements in an array at a specific position.

### **Array.push()**
A method that adds a new item to the end of an array.

### **trim()**
A string method that removes whitespace (spaces) from the beginning and end of text.

---

## Form & HTML Terms

### **HTML Form**
A section of a webpage with input fields that collects user data and sends it to the server.

### **Form Action**
The URL where form data gets sent when the form is submitted.

### **Form Method**
The HTTP method (GET or POST) used when submitting the form.

### **Input Field**
An HTML element where users can type or enter data (like text boxes).

### **Form Submission**
The process of sending form data to the server when the user clicks the submit button.

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

## REST API Terms

### **REST (Representational State Transfer)**
An architectural style for building web services that uses standard HTTP methods to perform operations.

### **RESTful**
Following REST principles - using HTTP methods (GET, POST, PUT, DELETE) in a standard way.

### **Endpoint**
A specific URL path that performs a particular action (like `/add-book` for creating books).

### **API (Application Programming Interface)**
A set of rules and endpoints that allow different applications to communicate with each other.

### **Idempotent**
An operation that produces the same result no matter how many times you run it (GET requests are idempotent).

---

## Status Code Terms

### **200 OK**
HTTP status code meaning the request was successful.

### **302 Found (Redirect)**
HTTP status code meaning the browser should go to a different URL.

### **400 Bad Request**
HTTP status code meaning the request was invalid (missing or incorrect data).

### **404 Not Found**
HTTP status code meaning the requested resource doesn't exist.

---

## Real-World Analogy

Think of building a web application like running a restaurant:

- **Framework (Express.js)** = The restaurant building with kitchen, dining area, and equipment already set up
- **Route** = A menu item (like "Appetizers" or "Main Course")
- **Route Handler** = The chef who prepares that specific dish
- **Middleware** = The prep station where ingredients are cleaned and prepared before cooking
- **Template** = A recipe card with blanks to fill in
- **Templating Engine (EJS)** = The process of following the recipe and filling in the blanks
- **Render** = The act of actually cooking the dish and plating it
- **Request** = A customer's order
- **Response** = The finished dish served to the customer
- **Database** = The pantry/storage where ingredients are kept
- **In-Memory Storage** = Ingredients sitting on the counter (temporary, lost when you clean up)

---

## Quick Reference: Most Important Terms

1. **Framework** = Pre-built tools to build apps faster
2. **Route** = URL path that triggers specific code
3. **Render** = Fill template with data to create HTML
4. **Middleware** = Functions that process requests before they reach routes
5. **Template** = HTML file with placeholders for data
6. **Templating Engine** = Tool that fills templates with data
7. **Request (req)** = Incoming data from the client
8. **Response (res)** = Outgoing data to the client
9. **CRUD** = Create, Read, Update, Delete operations
10. **GET** = Retrieve data, **POST** = Send/create data
