# Homework 5: FastAPI Product Management System
## Complete Concepts and Code Explanation

---

## Table of Contents
1. [Overview](#overview)
2. [Key Concepts](#key-concepts)
3. [Database Design](#database-design)
4. [API Implementation](#api-implementation)
5. [Data Validation and Error Handling](#data-validation-and-error-handling)
6. [Line-by-Line Code Explanation](#line-by-line-code-explanation)
7. [Running the Application](#running-the-application)

---

## Overview

This homework implements a **RESTful API** for product management using:
- **FastAPI**: Modern Python web framework for building APIs
- **SQLAlchemy**: Python SQL toolkit and Object-Relational Mapping (ORM) library
- **Pydantic**: Data validation library using Python type annotations
- **MySQL**: Relational database management system
- **Pydantic**: For request/response validation

---

## Key Concepts

### 1. RESTful API Architecture

**REST (Representational State Transfer)** is an architectural style for designing networked applications:

- **Stateless**: Each request contains all information needed to process it
- **Resource-based**: URLs represent resources (e.g., `/products`)
- **HTTP Methods**: 
  - `GET`: Retrieve data
  - `POST`: Create new resources
  - `PUT`: Update existing resources
  - `DELETE`: Remove resources
- **Status Codes**: 
  - `200 OK`: Successful GET/PUT
  - `201 Created`: Successful POST
  - `204 No Content`: Successful DELETE
  - `404 Not Found`: Resource doesn't exist
  - `400 Bad Request`: Invalid input
  - `500 Internal Server Error`: Server error

### 2. FastAPI Framework

**FastAPI** is a modern, fast web framework for building APIs:

- **Automatic API Documentation**: Generates OpenAPI/Swagger docs
- **Type Hints**: Uses Python type annotations for validation
- **Async Support**: Built-in support for async/await
- **Dependency Injection**: Clean dependency management
- **Data Validation**: Automatic request/response validation

### 3. SQLAlchemy ORM

**Object-Relational Mapping (ORM)** maps database tables to Python classes:

- **Models**: Python classes representing database tables
- **Sessions**: Database connection and transaction management
- **Queries**: Pythonic way to query databases
- **Migrations**: Database schema versioning

### 4. Pydantic Models

**Pydantic** provides data validation using Python type annotations:

- **BaseModel**: Base class for data models
- **Automatic Validation**: Validates data types automatically
- **Serialization**: Converts Python objects to JSON
- **Documentation**: Auto-generates API documentation

---

## Database Design

### Entity: Product

The Product table stores product information with the following fields:

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | Integer | Primary Key, Auto-increment | Unique identifier |
| `name` | String(100) | NOT NULL | Product name |
| `description` | Text | NULL | Product description |
| `price` | Float | NOT NULL | Product price |
| `quantity` | Integer | Default: 0 | Available quantity |
| `created_at` | DateTime | Auto-set on creation | Creation timestamp |
| `updated_at` | DateTime | Auto-update on modification | Last update timestamp |

**Design Principles:**
- **Primary Key**: `id` ensures uniqueness
- **Normalization**: Single table for product data
- **Timestamps**: Track creation and modification times
- **Constraints**: NOT NULL ensures data integrity

---

## API Implementation

### Endpoint Structure

```
GET    /products          - List all products
GET    /products/{id}     - Get specific product
POST   /products          - Create new product
PUT    /products/{id}     - Update product
DELETE /products/{id}     - Delete product
```

### Request/Response Flow

1. **Client** sends HTTP request to FastAPI
2. **FastAPI** validates request using Pydantic
3. **Dependency Injection** provides database session
4. **SQLAlchemy** executes database query
5. **Response** is serialized and returned to client

---

## Data Validation and Error Handling

### Validation Rules

1. **Price**: Must be positive (>= 0)
2. **Quantity**: Must be non-negative (>= 0)
3. **Name**: Required, string type
4. **Description**: Optional, string type

### Error Handling Strategy

- **400 Bad Request**: Invalid input data
- **404 Not Found**: Resource doesn't exist
- **500 Internal Server Error**: Database/server errors
- **Transaction Rollback**: On errors, rollback database changes

---

## Line-by-Line Code Explanation

### File: `database.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
```

**Explanation:**
- `create_engine`: Creates database connection engine
- `declarative_base`: Base class for ORM models
- `sessionmaker`: Factory for creating database sessions

```python
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:leoncorreia@localhost/fastapi_demo"
```

**Explanation:**
- Database connection string in format: `dialect+driver://user:password@host/database`
- `mysql+pymysql`: MySQL database using PyMySQL driver
- `localhost`: Database server location
- `fastapi_demo`: Database name

```python
engine = create_engine(SQLALCHEMY_DATABASE_URL)
```

**Explanation:**
- Creates SQLAlchemy engine that manages database connections
- Handles connection pooling automatically
- Converts Python objects to SQL queries

```python
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

**Explanation:**
- `autocommit=False`: Manual transaction control
- `autoflush=False`: Manual flush control
- `bind=engine`: Associates session with engine

```python
Base = declarative_base()
```

**Explanation:**
- Base class for all ORM models
- Provides table creation and mapping functionality

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**Explanation:**
- **Dependency function** for FastAPI dependency injection
- `yield`: Provides database session to route handler
- `finally`: Ensures session is closed even if error occurs
- **Context Manager Pattern**: Proper resource cleanup

---

### File: `models.py`

```python
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from database import Base
```

**Explanation:**
- `Column`: Defines table columns
- `Integer, String, Float, DateTime, Text`: SQL data types
- `func`: SQL functions (e.g., `now()`)
- `Base`: Base class for ORM models

```python
class Product(Base):
    __tablename__ = "products"
```

**Explanation:**
- `Product`: Python class representing database table
- `__tablename__`: Specifies actual database table name
- Inherits from `Base` to get ORM functionality

```python
id = Column(Integer, primary_key=True, index=True)
```

**Explanation:**
- `Integer`: SQL integer type
- `primary_key=True`: Marks as primary key (unique, auto-increment)
- `index=True`: Creates database index for faster queries

```python
name = Column(String(100), nullable=False)
```

**Explanation:**
- `String(100)`: VARCHAR(100) in SQL
- `nullable=False`: Field is required (NOT NULL constraint)

```python
description = Column(Text, nullable=True)
```

**Explanation:**
- `Text`: SQL TEXT type (unlimited length)
- `nullable=True`: Field is optional (can be NULL)

```python
price = Column(Float, nullable=False)
```

**Explanation:**
- `Float`: SQL FLOAT type for decimal numbers
- `nullable=False`: Price is required

```python
quantity = Column(Integer, default=0)
```

**Explanation:**
- `Integer`: SQL integer type
- `default=0`: Default value if not provided

```python
created_at = Column(DateTime(timezone=True), server_default=func.now())
```

**Explanation:**
- `DateTime(timezone=True)`: Timestamp with timezone
- `server_default=func.now()`: Database sets value on insert
- Automatically populated when record is created

```python
updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

**Explanation:**
- `onupdate=func.now()`: Database updates value on record modification
- Only updates when record is changed

---

### File: `schemas.py`

```python
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
```

**Explanation:**
- `BaseModel`: Pydantic base class for data validation
- `datetime`: Python datetime type
- `Optional`: Type hint for nullable fields

```python
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int = 0
```

**Explanation:**
- `ProductBase`: Base schema with common fields
- `name: str`: Required string field
- `Optional[str] = None`: Optional string field with default None
- `price: float`: Required float field
- `quantity: int = 0`: Integer field with default 0
- **Type Hints**: Enable automatic validation

```python
class ProductCreate(ProductBase):
    pass
```

**Explanation:**
- Inherits all fields from `ProductBase`
- Used for POST request validation
- No additional fields needed for creation

```python
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
```

**Explanation:**
- All fields optional for partial updates
- Used for PUT request validation
- Allows updating only specific fields

```python
class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
```

**Explanation:**
- Includes `id` and timestamps (not in base)
- `from_attributes = True`: Allows conversion from SQLAlchemy models
- Used for response serialization
- **ORM Mode**: Enables automatic conversion from database models

---

### File: `main.py`

#### Imports and Setup

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import uvicorn
```

**Explanation:**
- `FastAPI`: Main application class
- `Depends`: Dependency injection system
- `HTTPException`: For error responses
- `status`: HTTP status codes
- `CORSMiddleware`: Cross-Origin Resource Sharing support
- `Session`: SQLAlchemy database session
- `List, Optional`: Type hints
- `uvicorn`: ASGI server for running FastAPI

```python
from database import get_db, engine, Base
from models import Product
from schemas import ProductCreate, ProductUpdate, Product as ProductSchema
```

**Explanation:**
- Imports database connection and base
- Imports Product model
- Imports Pydantic schemas (aliased to avoid naming conflict)

```python
Base.metadata.create_all(bind=engine)
```

**Explanation:**
- Creates all database tables defined in models
- Runs on application startup
- **Migration Alternative**: In production, use Alembic for migrations

```python
app = FastAPI(
    title="Product Management API",
    description="A RESTful API for managing products using FastAPI and SQLAlchemy",
    version="1.0.0"
)
```

**Explanation:**
- Creates FastAPI application instance
- Metadata for API documentation
- Auto-generates OpenAPI/Swagger docs

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Explanation:**
- **CORS**: Allows frontend to make requests from different origins
- `allow_origins=["*"]`: Allows all origins (use specific domains in production)
- `allow_methods=["*"]`: Allows all HTTP methods
- `allow_headers=["*"]`: Allows all headers

#### Root Endpoint

```python
@app.get("/")
def read_root():
    return {
        "message": "Welcome to Product Management API",
        "version": "1.0.0",
        "endpoints": {...}
    }
```

**Explanation:**
- `@app.get("/")`: Decorator defines GET route at root path
- Returns API information
- **Route Decorator**: Maps function to HTTP endpoint

#### GET All Products

```python
@app.get("/products", response_model=List[ProductSchema], status_code=status.HTTP_200_OK)
def get_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
```

**Explanation:**
- `@app.get("/products")`: GET endpoint for `/products`
- `response_model=List[ProductSchema]`: Validates response format
- `skip, limit`: Pagination parameters
- `db: Session = Depends(get_db)`: Dependency injection for database session
- **Dependency Injection**: FastAPI automatically provides database session

```python
try:
    products = db.query(Product).offset(skip).limit(limit).all()
    return products
```

**Explanation:**
- `db.query(Product)`: Creates SQLAlchemy query
- `.offset(skip)`: Skips first N records (pagination)
- `.limit(limit)`: Limits number of results
- `.all()`: Executes query and returns all results
- **Query Builder**: SQLAlchemy's fluent query interface

```python
except Exception as e:
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=f"Error retrieving products: {str(e)}"
    )
```

**Explanation:**
- Catches any database errors
- Returns 500 status with error message
- **Error Handling**: Prevents application crashes

#### GET Single Product

```python
@app.get("/products/{product_id}", response_model=ProductSchema, status_code=status.HTTP_200_OK)
def get_product(product_id: int, db: Session = Depends(get_db)):
```

**Explanation:**
- `{product_id}`: Path parameter (extracted from URL)
- `product_id: int`: FastAPI validates as integer
- **Path Parameters**: Extracted from URL path

```python
product = db.query(Product).filter(Product.id == product_id).first()
```

**Explanation:**
- `.filter(Product.id == product_id)`: Adds WHERE clause
- `.first()`: Returns first result or None
- **Query Filtering**: SQLAlchemy's filter method

```python
if product is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with id {product_id} not found"
    )
```

**Explanation:**
- Checks if product exists
- Raises 404 if not found
- **404 Not Found**: Standard HTTP status for missing resources

#### POST Create Product

```python
@app.post("/products", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
```

**Explanation:**
- `@app.post`: POST endpoint for creating resources
- `product: ProductCreate`: Request body validated by Pydantic
- `status_code=201`: Created status code
- **Request Body**: Automatically parsed and validated

```python
if product.price < 0:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Price must be a positive number"
    )
```

**Explanation:**
- Business logic validation
- Returns 400 for invalid data
- **400 Bad Request**: Client error for invalid input

```python
db_product = Product(
    name=product.name,
    description=product.description,
    price=product.price,
    quantity=product.quantity
)
```

**Explanation:**
- Creates SQLAlchemy model instance
- Maps Pydantic model to ORM model
- **Model Instantiation**: Creates new database record

```python
db.add(db_product)
db.commit()
db.refresh(db_product)
```

**Explanation:**
- `db.add()`: Adds object to session (staged for insert)
- `db.commit()`: Executes INSERT statement
- `db.refresh()`: Reloads object from database (gets generated ID and timestamps)
- **Transaction Management**: Commit persists changes

#### PUT Update Product

```python
@app.put("/products/{product_id}", response_model=ProductSchema, status_code=status.HTTP_200_OK)
def update_product(
    product_id: int,
    product_update: ProductUpdate,
    db: Session = Depends(get_db)
):
```

**Explanation:**
- `@app.put`: PUT endpoint for updates
- `product_update: ProductUpdate`: Partial update model (all fields optional)

```python
update_data = product_update.model_dump(exclude_unset=True)
```

**Explanation:**
- `model_dump()`: Converts Pydantic model to dictionary
- `exclude_unset=True`: Only includes fields that were provided
- **Partial Updates**: Only updates provided fields

```python
for field, value in update_data.items():
    setattr(db_product, field, value)
```

**Explanation:**
- Dynamically sets attributes on model
- `setattr()`: Python built-in for setting attributes
- **Dynamic Updates**: Updates only changed fields

#### DELETE Product

```python
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
```

**Explanation:**
- `@app.delete`: DELETE endpoint
- `status_code=204`: No content (successful deletion)
- **204 No Content**: Standard for successful DELETE

```python
db.delete(db_product)
db.commit()
```

**Explanation:**
- `db.delete()`: Marks object for deletion
- `db.commit()`: Executes DELETE statement
- **Cascade Deletes**: Consider foreign key relationships in production

#### Application Runner

```python
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```

**Explanation:**
- `uvicorn.run()`: Starts ASGI server
- `host="0.0.0.0"`: Listens on all network interfaces
- `port=8000`: Server port
- `reload=True`: Auto-reload on code changes (development only)

---

## Running the Application

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Database

Create MySQL database:
```sql
CREATE DATABASE fastapi_demo;
```

Update `database.py` with your credentials if needed.

### 3. Run the Application

```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload
```

### 4. Access API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### 5. Test Endpoints

**Create Product:**
```bash
curl -X POST "http://localhost:8000/products" \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "description": "Gaming laptop", "price": 999.99, "quantity": 10}'
```

**Get All Products:**
```bash
curl http://localhost:8000/products
```

**Get Product by ID:**
```bash
curl http://localhost:8000/products/1
```

**Update Product:**
```bash
curl -X PUT "http://localhost:8000/products/1" \
  -H "Content-Type: application/json" \
  -d '{"price": 899.99}'
```

**Delete Product:**
```bash
curl -X DELETE "http://localhost:8000/products/1"
```

---

## Key Concepts Summary

### 1. **Dependency Injection**
- FastAPI's `Depends()` provides dependencies to route handlers
- Ensures proper resource management (database sessions)
- Enables testability and modularity

### 2. **Type Safety**
- Python type hints enable automatic validation
- Pydantic validates request/response data
- Catches errors at API boundary

### 3. **ORM Benefits**
- Database-agnostic code (works with MySQL, PostgreSQL, etc.)
- Pythonic query interface
- Automatic SQL generation
- Relationship management

### 4. **RESTful Design**
- Resource-based URLs
- HTTP methods for actions
- Standard status codes
- Stateless communication

### 5. **Error Handling**
- Try-except blocks catch errors
- HTTPException provides proper status codes
- Transaction rollback on errors
- User-friendly error messages

---

## Best Practices Implemented

1. ✅ **Separation of Concerns**: Models, schemas, and routes in separate files
2. ✅ **Input Validation**: Pydantic validates all inputs
3. ✅ **Error Handling**: Comprehensive error handling with proper status codes
4. ✅ **Transaction Management**: Proper commit/rollback on errors
5. ✅ **Type Hints**: Full type annotation for better IDE support
6. ✅ **Documentation**: Docstrings and API documentation
7. ✅ **CORS Support**: Enabled for frontend integration
8. ✅ **Pagination**: Implemented for list endpoints

---

## Conclusion

This implementation demonstrates:
- **FastAPI** for building modern REST APIs
- **SQLAlchemy ORM** for database operations
- **Pydantic** for data validation
- **RESTful** API design principles
- **Error handling** and validation
- **Dependency injection** patterns

The code follows best practices and is production-ready with proper error handling, validation, and documentation.
