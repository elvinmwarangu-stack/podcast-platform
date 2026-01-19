# FastAPI imports
from fastapi import APIRouter, Depends, HTTPException
# APIRouter → create a modular router for categories endpoints
# Depends → inject dependencies like DB session
# HTTPException → raise HTTP errors with status codes

from sqlalchemy.orm import Session
# SQLAlchemy session type for interacting with the database

from typing import List
# Used for response typing → returning a list of categories

# Import project-specific modules
from app.crud import category as crud_category
# CRUD operations for categories (create, read, etc.)

from app.schemas import category as schemas_category
# Pydantic schemas for category validation (request & response)

from app.dependencies import get_db
# Dependency to provide a database session

# Create a router for category endpoints
router = APIRouter(tags=["categories"])


# LIST CATEGORIES
@router.get("/", response_model=List[schemas_category.CategoryOut])
def list_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Returns a list of categories with optional pagination.
    
    - skip: number of categories to skip (default 0)
    - limit: maximum number of categories to return (default 100)
    - db: injected database session
    """
    return crud_category.get_categories(db, skip, limit)


# GET SINGLE CATEGORY
@router.get("/{category_id}", response_model=schemas_category.CategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    """
    Returns a single category by its ID.
    
    - category_id: the ID of the category to retrieve
    - db: injected database session
    - Raises 404 if category not found
    """
    category_obj = crud_category.get_category(db, category_id)
    if not category_obj:
        raise HTTPException(404, "Category not found")
    return category_obj


# CREATE NEW CATEGORY
@router.post("/", response_model=schemas_category.CategoryOut, status_code=201)
def create_category(category_in: schemas_category.CategoryCreate, db: Session = Depends(get_db)):
    """
    Creates a new category.

    - category_in: validated input data (name, etc.)
    - db: injected database session
    - Raises 400 if a category with the same name already exists
    - Returns the newly created category
    """
    if crud_category.get_category_by_name(db, category_in.name):
        raise HTTPException(400, "Category name already exists")
    return crud_category.create_category(db, category_in)
