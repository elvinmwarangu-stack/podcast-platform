from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import user, podcast, comment, category, favorite

from app.api import (
    auth_router,
    users_router,
    podcasts_router,
    comments_router,
    favorites_router,
    categories_router,
)

app = FastAPI(
    title="Podcast Platform API",
    description="Backend API for Podcast / Audio Content Platform",
    version="0.1.0"
)

# Allow frontend to connect (update origins later for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(podcasts_router, prefix="/podcasts", tags=["Podcasts"])
app.include_router(comments_router, prefix="/comments", tags=["Comments"])
app.include_router(favorites_router, prefix="/favorites", tags=["Favorites"])
app.include_router(categories_router, prefix="/categories", tags=["Categories"])


@app.get("/")
def root():
    return {"message": "Podcast Platform API is running"}