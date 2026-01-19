# FastAPI imports
from fastapi import APIRouter, Depends, HTTPException
# APIRouter → create modular routes
# Depends → inject dependencies like DB session or current user
# HTTPException → raise HTTP errors with status codes

from sqlalchemy.orm import Session
# SQLAlchemy session for database operations

from typing import List
# Used for response typing → returning a list of podcasts

# Project-specific imports
from app import crud, schemas
# crud → functions for database operations
# schemas → Pydantic models for request/response validation

from app.dependencies import get_current_active_user, get_db
# get_current_active_user → retrieves the currently logged-in user
# get_db → provides a database session

from app.models.user import User
# User model used for authentication and ownership checks

# Create router for favorites endpoints
router = APIRouter(tags=["favorites"])


# GET USER FAVORITES
@router.get("/", response_model=List[schemas.PodcastOut])
def get_user_favorites(
    current_user: User = Depends(get_current_active_user),  # Get logged-in user
    db: Session = Depends(get_db),                           # Inject DB session
    skip: int = 0,                                           # Pagination: number of items to skip
    limit: int = 20,                                         # Pagination: maximum number of items
):
    """
    Retrieve the current user's favorite podcasts.
    Returns a list of PodcastOut schema objects.
    """
    return crud.get_user_favorite_podcasts(db, current_user.id, skip, limit)


# ADD FAVORITE
@router.post("/{podcast_id}")
def add_favorite(
    podcast_id: int,                                        # ID of the podcast to add to favorites
    current_user: User = Depends(get_current_active_user),  # Get logged-in user
    db: Session = Depends(get_db),                           # Inject DB session
):
    """
    Add a podcast to the current user's favorites.
    Raises 400 if the podcast is already favorited.
    """
    if crud.is_podcast_favorited(db, current_user.id, podcast_id):
        raise HTTPException(400, "Already favorited")
    
    crud.add_favorite(db, current_user.id, podcast_id)
    return {"message": "Added to favorites"}


# REMOVE FAVORITE
@router.delete("/{podcast_id}")
def remove_favorite(
    podcast_id: int,                                        # ID of the podcast to remove from favorites
    current_user: User = Depends(get_current_active_user),  # Get logged-in user
    db: Session = Depends(get_db),                           # Inject DB session
):
    """
    Remove a podcast from the current user's favorites.
    Raises 404 if the podcast is not in favorites.
    """
    if not crud.is_podcast_favorited(db, current_user.id, podcast_id):
        raise HTTPException(404, "Not in favorites")
    
    crud.remove_favorite(db, current_user.id, podcast_id)
    return {"message": "Removed from favorites"}
