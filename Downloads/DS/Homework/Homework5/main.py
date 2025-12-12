from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import uvicorn

from database import get_db, engine, Base
from models import Product
from schemas import ProductCreate, ProductUpdate, Product as ProductSchema

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(
    title="Product Management API",
    description="A RESTful API for managing products using FastAPI and SQLAlchemy",
    version="1.0.0"
)

# Configure CORS middleware to allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def read_root():
    """
    Root endpoint that returns API information.
    """
    return {
        "message": "Welcome to Product Management API",
        "version": "1.0.0",
        "endpoints": {
            "GET /products": "Get all products",
            "GET /products/{id}": "Get a specific product",
            "POST /products": "Create a new product",
            "PUT /products/{id}": "Update a product",
            "DELETE /products/{id}": "Delete a product"
        }
    }

# GET all products
@app.get("/products", response_model=List[ProductSchema], status_code=status.HTTP_200_OK)
def get_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Retrieve all products from the database.
    
    Query Parameters:
    - skip: Number of records to skip (for pagination)
    - limit: Maximum number of records to return
    
    Returns:
    - List of all products
    """
    try:
        products = db.query(Product).offset(skip).limit(limit).all()
        return products
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving products: {str(e)}"
        )

# GET a single product by ID
@app.get("/products/{product_id}", response_model=ProductSchema, status_code=status.HTTP_200_OK)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific product by its ID.
    
    Path Parameters:
    - product_id: The unique identifier of the product
    
    Returns:
    - Product object if found
    
    Raises:
    - HTTPException 404 if product not found
    """
    try:
        product = db.query(Product).filter(Product.id == product_id).first()
        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_id} not found"
            )
        return product
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving product: {str(e)}"
        )

# POST - Create a new product
@app.post("/products", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Create a new product in the database.
    
    Request Body:
    - name: Product name (required)
    - description: Product description (optional)
    - price: Product price (required, must be positive)
    - quantity: Product quantity (optional, defaults to 0)
    
    Returns:
    - Created product object
    
    Raises:
    - HTTPException 400 for validation errors
    - HTTPException 500 for database errors
    """
    try:
        # Validate price is positive
        if product.price < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Price must be a positive number"
            )
        
        # Validate quantity is non-negative
        if product.quantity < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Quantity must be a non-negative number"
            )
        
        # Create new product instance
        db_product = Product(
            name=product.name,
            description=product.description,
            price=product.price,
            quantity=product.quantity
        )
        
        # Add to database session
        db.add(db_product)
        # Commit transaction
        db.commit()
        # Refresh to get generated ID and timestamps
        db.refresh(db_product)
        
        return db_product
    except HTTPException:
        raise
    except Exception as e:
        # Rollback transaction on error
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating product: {str(e)}"
        )

# PUT - Update an existing product
@app.put("/products/{product_id}", response_model=ProductSchema, status_code=status.HTTP_200_OK)
def update_product(
    product_id: int,
    product_update: ProductUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing product in the database.
    
    Path Parameters:
    - product_id: The unique identifier of the product to update
    
    Request Body:
    - name: Product name (optional)
    - description: Product description (optional)
    - price: Product price (optional, must be positive if provided)
    - quantity: Product quantity (optional, must be non-negative if provided)
    
    Returns:
    - Updated product object
    
    Raises:
    - HTTPException 404 if product not found
    - HTTPException 400 for validation errors
    - HTTPException 500 for database errors
    """
    try:
        # Find the product
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_id} not found"
            )
        
        # Update only provided fields
        update_data = product_update.model_dump(exclude_unset=True)
        
        # Validate price if provided
        if "price" in update_data and update_data["price"] < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Price must be a positive number"
            )
        
        # Validate quantity if provided
        if "quantity" in update_data and update_data["quantity"] < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Quantity must be a non-negative number"
            )
        
        # Apply updates
        for field, value in update_data.items():
            setattr(db_product, field, value)
        
        # Commit changes
        db.commit()
        # Refresh to get updated timestamps
        db.refresh(db_product)
        
        return db_product
    except HTTPException:
        raise
    except Exception as e:
        # Rollback transaction on error
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating product: {str(e)}"
        )

# DELETE - Delete a product
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a product from the database.
    
    Path Parameters:
    - product_id: The unique identifier of the product to delete
    
    Returns:
    - No content (204 status)
    
    Raises:
    - HTTPException 404 if product not found
    - HTTPException 500 for database errors
    """
    try:
        # Find the product
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_id} not found"
            )
        
        # Delete the product
        db.delete(db_product)
        # Commit transaction
        db.commit()
        
        return None
    except HTTPException:
        raise
    except Exception as e:
        # Rollback transaction on error
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting product: {str(e)}"
        )

# Run the application
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
