# 📖 Key Terms Glossary - Simple One-Line Definitions

## Core Framework Terms

### **FastAPI**
A modern Python web framework that automatically generates API documentation and validates data using type hints.

### **Framework**
A pre-built structure that provides tools and rules to build applications faster, so you don't have to write everything from scratch.

### **ASGI (Asynchronous Server Gateway Interface)**
A Python standard that allows web servers to handle asynchronous requests efficiently, enabling FastAPI to process multiple requests simultaneously.

### **Uvicorn**
An ASGI server that runs FastAPI applications and handles HTTP requests/responses.

---

## API & HTTP Terms

### **REST (Representational State Transfer)**
An architectural style for building web services that uses standard HTTP methods (GET, POST, PUT, DELETE) to perform operations on resources.

### **RESTful API**
An API that follows REST principles, using HTTP methods in a standard way to create, read, update, and delete resources.

### **Endpoint**
A specific URL path that performs a particular action (like `/products` for managing products).

### **API (Application Programming Interface)**
A set of rules and endpoints that allow different applications to communicate with each other over the internet.

### **HTTP Method**
The type of operation being requested: GET (read), POST (create), PUT (update), DELETE (remove).

### **GET Request**
An HTTP method used to retrieve/read data from the server without modifying anything.

### **POST Request**
An HTTP method used to send data to the server to create a new resource.

### **PUT Request**
An HTTP method used to send data to update an existing resource.

### **DELETE Request**
An HTTP method used to remove a resource from the server.

### **Request Body**
The data sent with a POST or PUT request (usually JSON format).

### **Response Model**
The structure/format of data that an endpoint returns to the client.

---

## Database & ORM Terms

### **ORM (Object-Relational Mapping)**
A technique that maps database tables to Python classes, allowing you to work with databases using Python code instead of SQL.

### **SQLAlchemy**
A Python ORM library that provides a Pythonic way to interact with databases without writing raw SQL queries.

### **Model**
A Python class that represents a database table, where each instance represents a row in that table.

### **Table**
A collection of related data organized in rows and columns in a database.

### **Column**
A single field/attribute in a database table (like `name`, `price`, `quantity`).

### **Primary Key**
A unique identifier for each row in a table (usually an auto-incrementing ID).

### **Foreign Key**
A column that references the primary key of another table, creating a relationship between tables.

### **Session**
A connection to the database that manages transactions and tracks changes to objects.

### **Query**
A request to retrieve or manipulate data from the database.

### **Transaction**
A sequence of database operations that are executed as a single unit - either all succeed or all fail.

### **Commit**
Saving changes to the database, making them permanent.

### **Rollback**
Canceling changes and reverting the database to its previous state, usually done when an error occurs.

### **Migration**
The process of updating the database schema (table structure) when your models change.

---

## Data Validation Terms

### **Pydantic**
A Python library that validates data using type hints and automatically converts data types.

### **Schema**
A definition of the expected structure and types of data (like a blueprint for what data should look like).

### **BaseModel**
A Pydantic class that provides automatic data validation and serialization.

### **Type Hint**
Python annotations (like `str`, `int`, `float`) that specify what type of data a variable should contain.

### **Validation**
The process of checking that data meets certain rules and requirements before processing it.

### **Serialization**
Converting Python objects into a format that can be sent over the network (usually JSON).

### **Deserialization**
Converting data received from the network (usually JSON) back into Python objects.

---

## FastAPI Specific Terms

### **@app.get()**
A FastAPI decorator that defines what happens when someone visits a URL using a GET request.

### **@app.post()**
A FastAPI decorator that defines what happens when someone submits data using a POST request.

### **@app.put()**
A FastAPI decorator that defines what happens when someone updates data using a PUT request.

### **@app.delete()**
A FastAPI decorator that defines what happens when someone deletes a resource using a DELETE request.

### **Decorator**
A Python feature that modifies or extends a function's behavior without changing its code directly.

### **Path Parameter**
A variable extracted from the URL path (like `/products/{id}` where `id` is the parameter).

### **Query Parameter**
Optional parameters added to the URL after a `?` (like `/products?skip=0&limit=10`).

### **Dependency Injection**
A design pattern where dependencies (like database sessions) are automatically provided to functions rather than being created inside them.

### **Depends()**
A FastAPI function that injects dependencies (like database sessions) into route handlers.

### **HTTPException**
A FastAPI class used to return error responses with appropriate HTTP status codes.

### **Status Code**
A number that indicates the result of an HTTP request (200 = success, 404 = not found, 500 = server error).

---

## Middleware Terms

### **Middleware**
Functions that run between receiving a request and sending a response, processing data before it reaches your route handler.

### **CORS (Cross-Origin Resource Sharing)**
A security feature that allows web pages from one domain to make requests to a server on a different domain.

### **CORSMiddleware**
FastAPI middleware that handles CORS, allowing frontend applications to communicate with the API.

---

## Database Connection Terms

### **Engine**
A SQLAlchemy object that manages database connections and connection pooling.

### **Connection String**
A string that contains all information needed to connect to a database (username, password, host, database name).

### **SessionLocal**
A factory function that creates database sessions when needed.

### **Connection Pooling**
A technique that reuses database connections instead of creating new ones for each request, improving performance.

---

## SQLAlchemy Specific Terms

### **Base**
A base class (from `declarative_base()`) that all ORM models inherit from, providing table creation and mapping functionality.

### **__tablename__**
A class attribute that specifies the actual name of the database table.

### **nullable**
A column property that determines whether a field can be NULL (empty) in the database.

### **server_default**
A default value that the database sets automatically when a new record is created.

### **onupdate**
A function that runs automatically when a record is updated (like updating a timestamp).

### **db.query()**
A SQLAlchemy method that starts building a database query.

### **filter()**
A SQLAlchemy method that adds a WHERE clause to a query, narrowing down results.

### **first()**
A SQLAlchemy method that executes a query and returns the first result, or None if no results.

### **all()**
A SQLAlchemy method that executes a query and returns all matching results as a list.

### **offset()**
A SQLAlchemy method that skips a certain number of records (used for pagination).

### **limit()**
A SQLAlchemy method that restricts the number of results returned (used for pagination).

### **db.add()**
A SQLAlchemy method that stages a new object to be inserted into the database.

### **db.delete()**
A SQLAlchemy method that stages an object to be deleted from the database.

### **db.refresh()**
A SQLAlchemy method that reloads an object from the database, getting the latest values (like auto-generated IDs).

---

## Pydantic Specific Terms

### **ProductCreate**
A Pydantic schema used to validate data when creating a new product.

### **ProductUpdate**
A Pydantic schema used to validate data when updating an existing product (all fields optional for partial updates).

### **Optional**
A type hint that indicates a field may be None (not required).

### **model_dump()**
A Pydantic method that converts a model instance into a Python dictionary.

### **exclude_unset=True**
A Pydantic option that only includes fields that were explicitly provided, ignoring fields with default values.

### **from_attributes = True**
A Pydantic configuration that allows automatic conversion from SQLAlchemy models to Pydantic models.

---

## Data Operations Terms

### **CRUD**
The four basic operations: **C**reate, **R**ead, **U**pdate, **D**elete - everything you can do with data.

### **Create**
Adding a new record to the database (POST request).

### **Read**
Retrieving data from the database (GET request).

### **Update**
Modifying an existing record in the database (PUT request).

### **Delete**
Removing a record from the database (DELETE request).

### **Pagination**
Breaking large result sets into smaller chunks (pages) to improve performance and user experience.

---

## Error Handling Terms

### **Try-Except Block**
Python code structure that catches and handles errors gracefully instead of crashing the application.

### **Exception**
An error that occurs during program execution.

### **HTTP Status Code 200**
Success - the request was completed successfully.

### **HTTP Status Code 201**
Created - a new resource was successfully created.

### **HTTP Status Code 204**
No Content - the request was successful but there's no content to return (common for DELETE).

### **HTTP Status Code 400**
Bad Request - the request was invalid (missing or incorrect data).

### **HTTP Status Code 404**
Not Found - the requested resource doesn't exist.

### **HTTP Status Code 500**
Internal Server Error - something went wrong on the server side.

---

## Python Terms Used

### **Type Annotation**
Specifying the expected data type for variables, function parameters, and return values (like `name: str`).

### **List**
A Python type hint indicating a collection of items (like `List[Product]` means a list of Product objects).

### **Optional**
A Python type hint indicating a value can be the specified type or None.

### **from typing import**
Importing type hint utilities from Python's typing module.

### **yield**
A Python keyword that produces a value and pauses function execution, used in generator functions (like dependency injection).

### **setattr()**
A Python built-in function that sets an attribute on an object dynamically.

### **if __name__ == "__main__"**
A Python pattern that runs code only when the script is executed directly (not when imported).

---

## API Documentation Terms

### **OpenAPI**
A specification for describing REST APIs in a standard format.

### **Swagger UI**
An interactive web interface that displays API documentation, automatically generated by FastAPI.

### **ReDoc**
An alternative documentation interface for REST APIs, also auto-generated by FastAPI.

### **API Documentation**
Automatically generated documentation that shows all available endpoints, their parameters, and response formats.

---

## Database Types

### **MySQL**
A popular relational database management system that stores data in tables with relationships.

### **Relational Database**
A database that organizes data into tables with relationships between them (like MySQL, PostgreSQL).

### **Integer**
A whole number data type (like 1, 42, -10).

### **Float**
A decimal number data type (like 3.14, 99.99).

### **String**
A text data type (like "Laptop", "Product name").

### **Text**
A large text data type for longer strings (like product descriptions).

### **DateTime**
A data type that stores both date and time information.

### **Boolean**
A data type that stores True or False values.

---

## Real-World Analogy

Think of building a REST API like running a library system:

- **FastAPI** = The library building with all the systems and rules already set up
- **Endpoint** = A specific service desk (like "Checkout Desk" or "Return Desk")
- **Route Handler** = The librarian who handles requests at that desk
- **Model** = A catalog card that describes what a book looks like
- **Database** = The actual book storage shelves
- **ORM (SQLAlchemy)** = A system that lets librarians work with books using simple instructions instead of complex shelf navigation
- **Session** = A librarian's shift where they can check out/return books
- **Transaction** = A complete checkout process (get book, record it, give to customer) - all or nothing
- **Schema (Pydantic)** = A form that validates information before processing (like checking ID before checkout)
- **Middleware** = The security checkpoint that checks bags before entering the library
- **CORS** = Rules that allow people from other libraries to use your library's services
- **Request** = A customer asking for a book
- **Response** = The librarian giving the book (or saying it's not available)
- **Status Code** = The result indicator (200 = "Here's your book", 404 = "Book not found", 400 = "Invalid request")

---

## Quick Reference: Most Important Terms

1. **FastAPI** = Modern Python framework for building APIs
2. **ORM (SQLAlchemy)** = Work with databases using Python instead of SQL
3. **Model** = Python class representing a database table
4. **Schema (Pydantic)** = Blueprint for validating data structure
5. **Endpoint** = URL path that performs a specific action
6. **Dependency Injection** = Automatic provision of resources (like database sessions)
7. **Session** = Database connection that manages transactions
8. **CRUD** = Create, Read, Update, Delete operations
9. **GET** = Retrieve data, **POST** = Create data, **PUT** = Update data, **DELETE** = Remove data
10. **Validation** = Checking data meets requirements before processing
11. **Transaction** = All-or-nothing database operations
12. **Status Code** = Number indicating request result (200 = success, 404 = not found, etc.)
13. **CORS** = Rules allowing cross-origin requests
14. **Type Hint** = Annotation specifying expected data type
15. **Middleware** = Functions that process requests before reaching handlers

---

## Common Patterns

### **Dependency Injection Pattern**
```python
def get_products(db: Session = Depends(get_db)):
    # db is automatically provided by FastAPI
```

### **Error Handling Pattern**
```python
try:
    # operation
except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
```

### **Query Pattern**
```python
products = db.query(Product).filter(Product.id == 1).first()
```

### **Create Pattern**
```python
db_product = Product(name="Laptop", price=999.99)
db.add(db_product)
db.commit()
db.refresh(db_product)
```

### **Update Pattern**
```python
db_product.name = "New Name"
db.commit()
db.refresh(db_product)
```

### **Delete Pattern**
```python
db.delete(db_product)
db.commit()
```
