# FastAPI imports
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
# APIRouter → create modular routes for podcasts
# Depends → inject dependencies like DB session or current user
# HTTPException → raise HTTP errors with proper status codes
# UploadFile, File, Form → for handling file uploads and form data (not used in current endpoints)

from sqlalchemy.orm import Session
# SQLAlchemy session for database interactions

from typing import List, Optional
# List → used in response typing for returning multiple podcasts
# Optional → allows optional parameters (not used in current endpoints)

# Project-specific imports
from app import crud, schemas
# crud → functions to interact with the database (get, create, update podcasts)
# schemas → Pydantic models for request validation and response formatting

from app.dependencies import get_current_active_user, get_db
# get_current_active_user → retrieves the logged-in user
# get_db → provides a database session

from app.models.user import User
# User model for ownership checks and authentication

# Create router for podcast endpoints
router = APIRouter(tags=["podcasts"])


# LIST PODCASTS
@router.get("/", response_model=List[schemas.PodcastOut])
def list_podcasts(
):
    """
    Returns a list of podcasts with optional pagination.
    """
    return crud.get_podcasts(db, skip=skip, limit=limit)


# GET PODCAST DETAIL
@router.get("/{podcast_id}", response_model=schemas.PodcastOut)
def get_podcast_detail(
    podcast_id: int,                    # ID of the podcast to retrieve
    db: Session = Depends(get_db),      # Inject database session
):
    """
    Retrieve details of a single podcast by ID.
    Raises 404 if podcast not found.
    """
    podcast = crud.get_podcast(db, podcast_id)
    if not podcast:
        raise HTTPException(404, "Podcast not found")
    return podcast


# CREATE PODCAST
@router.post("/", response_model=schemas.PodcastOut, status_code=201)
def create_podcast(
    podcast_create: schemas.PodcastCreate,                  # Validated input data for creating a podcast
    current_user: User = Depends(get_current_active_user),  # Get logged-in user
    db: Session = Depends(get_db),                          # Inject database session
):
    """
    Create a new podcast and associate it with the current user as the owner.
    Returns the newly created podcast.
    """
    return crud.create_podcast(db, podcast_create, owner_id=current_user.id)


# UPDATE PODCAST
@router.put("/{podcast_id}", response_model=schemas.PodcastOut)
def update_podcast(
    podcast_id: int,                                        # ID of the podcast to update
    update_data: schemas.PodcastUpdate,                     # Validated input data for updates
    current_user: User = Depends(get_current_active_user),  # Get logged-in user
    db: Session = Depends(get_db),                          # Inject database session
):
    """
    Update an existing podcast.
    - Only the owner of the podcast can update it.
    - Raises 404 if podcast not found.
    - Raises 403 if current user is not the owner.
    """
    podcast = crud.get_podcast(db, podcast_id)
    if not podcast:
        raise HTTPException(404, "Podcast not found")
    if podcast.owner_id != current_user.id:
        raise HTTPException(403, "Not authorized")
    return crud.update_podcast(db, podcast_id, update_data)
