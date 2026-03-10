from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import SessionLocal, Base, engine  # Import Base and engine
from app.models import Podcast
from sqlalchemy import text
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

# --- Create all tables if they don't exist ---
try:
    Base.metadata.create_all(bind=engine)  # ✅ This ensures all models create their tables
    print("✅ Database tables created successfully")
except Exception as e:
    print(f"⚠️  Database table creation warning: {e}")
    print("   This may be expected if database is not yet available")

# --- Run database migrations if needed ---
# Skip migrations on startup to avoid issues - run manually if needed
# Migration is now handled separately via startup_and_seed.py or manually

#CORS Middleware 
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://brians-fullstack.vercel.app",  # Deployed frontend
        "http://localhost:5173",                # Local Vite dev
        "http://localhost:3000",                # Alternative local dev
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(podcasts_router, prefix="/podcasts", tags=["Podcasts"])
app.include_router(comments_router, prefix="/comments", tags=["Comments"])
app.include_router(favorites_router, prefix="/favorites", tags=["Favorites"])
app.include_router(categories_router, prefix="/categories", tags=["Categories"])

#Root endpoint
@app.get("/")
def root():
    return {
        "message": "Podcast Platform API",
        "status": "healthy",
        "routes": {
            "auth": {"register": "POST /auth/register", "login": "POST /auth/login"},
            "users": {"me": "GET /users/me", "update": "PUT /users/me"},
            "podcasts": {
                "list": "GET /podcasts/",
                "get": "GET /podcasts/{id}",
                "create": "POST /podcasts/",
                "update": "PUT /podcasts/{id}",
            },
            "categories": {
                "list": "GET /categories/",
                "get": "GET /categories/{id}",
                "create": "POST /categories/",
            },
            "comments": {
                "list": "GET /comments/podcast/{podcast_id}",
                "create": "POST /comments/",
                "delete": "DELETE /comments/{id}",
            },
            "favorites": {
                "list": "GET /favorites/",
                "add": "POST /favorites/{podcast_id}",
                "remove": "DELETE /favorites/{podcast_id}",
            },
            "docs": "GET /docs",
            "redoc": "GET /redoc",
        },
    }

@app.get("/health")
def health_check():
    """Health check endpoint to verify database connection"""
    try:
        db = SessionLocal()
        # Test database connection
        db.execute(text("SELECT 1"))
        db.close()
        return {
            "status": "healthy",
            "database": "connected",
            "message": "API is running and database is accessible"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }
