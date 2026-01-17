# Podcast / Audio Content Platform

**Podcast Platform** is a full-stack web application that allows users to upload, discover, stream, comment on, and favorite podcast-style audio content.  
It features a **React single-page application (SPA)** frontend and a **FastAPI** backend with JWT authentication, secure file uploads, and relational database support.

**Team Members**  
- Elvin  
- Brian  
- Wangeshii  
- Muhammad  

## Project Overview

This application was built as part of the Phase 4 final project requirements at Moringa School.  
It demonstrates:

- React SPA with protected/private routes
- RESTful API with authentication & authorization
- CRUD operations across multiple resources
- File uploads (audio files)
- Database relationships (1-to-many & many-to-many)
- JWT-based secure authentication
- Password reset flow (basic implementation)
- Clean, responsive UI with Tailwind CSS / Bootstrap

## Features

### Public Features
- Browse all podcasts
- View podcast details & play audio
- Search podcasts by title/category
- View categories
- Register / Login / Forgot Password

### Authenticated Features
- Upload new podcast (with audio file)
- Edit / Delete own podcasts
- Comment on podcasts
- Add / Remove podcasts from favorites
- View personal favorites list
- Update profile

## Tech Stack

**Frontend**
- React (Vite / CRA)
- React Router v6
- Axios (API calls)
- Context API / Zustand / Redux (state management – choose one)
- Tailwind CSS or Bootstrap (styling)

**Backend**
- FastAPI
- SQLAlchemy (ORM)
- Pydantic (validation & settings)
- Python-Jose + Passlib (JWT & password hashing)
- SQLite (development) / PostgreSQL (production recommended)
- Uvicorn (ASGI server)

**Database**
- SQLite (local dev)
- PostgreSQL (recommended for deployment)

**Other**
- JWT Authentication
- Multipart file upload for audio
- CORS enabled

## Project Structure
Podcast-platform/
├── backend/
│   ├── app/
│   │   ├── api/               # Routers (auth, users, podcasts, comments, favorites, categories)
│   │   ├── crud/              # Database operations
│   │   ├── models/            # SQLAlchemy models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── dependencies.py
│   │   ├── database.py
│   │   ├── config.py
│   │   ├── utils.py
│   │   └── main.py
│   ├── uploads/               # Audio files (gitignored)
│   ├── migrations/            # Alembic (optional)
│   ├── .env
│   └── requirements.txt
├── frontend/                  # React app
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── context/ or store/
│   │   └── App.jsx
│   ├── public/
│   └── package.json
├── README.md
└── LICENSE
text## Setup Instructions

### Backend Setup

1. Navigate to backend folder
   ```bash
   cd backend

Create and activate virtual environmentBashpython3 -m venv venv
source venv/bin/activate     # Linux/macOS
# or on Windows: venv\Scripts\activate
Install dependenciesBashpip install -r requirements.txtOr manually:Bashpip install fastapi "uvicorn[standard]" sqlalchemy pydantic python-jose[cryptography] passlib[bcrypt] python-multipart python-dotenv pydantic-settings
Create .env file in backend/ foldertextSECRET_KEY=your-very-long-random-secret-key-here-please-change-this
DATABASE_URL=sqlite:///./podcast_app.db
# For production: postgresql://user:password@host:5432/dbname
Create database tablesBashpython -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
Run the backendBashuvicorn app.main:app --reload
# or
fastapi dev app/main.pyAPI docs will be available at:
http://127.0.0.1:8000/docs

Frontend Setup

Navigate to frontend folderBashcd frontend
Install dependenciesBashnpm install
# or yarn install
Start development serverBashnpm run dev
# or yarn devApp usually runs at: http://localhost:5173 (Vite) or http://localhost:3000 (CRA)

API Endpoints Overview
Method,Endpoint,Description,Auth?
POST,/auth/register,Register new user,No
POST,/auth/login,Login & get JWT,No
POST,/auth/forgot-password,Request password reset,No
PATCH,/auth/reset-password,Reset password with token,No
GET,/users/me,Get current user profile,Yes
PUT,/users/me,Update profile,Yes
GET,/podcasts,List podcasts (with ?search= & ?category=),No
GET,/podcasts/{id},Get podcast details,No
POST,/podcasts,Upload new podcast + audio,Yes
PUT,/podcasts/{id},Update podcast (owner only),Yes
DELETE,/podcasts/{id},Delete podcast (owner only),Yes
PATCH,/podcasts/{id}/listen,Increment listen count,No
GET,/podcasts/{id}/comments,Get comments for podcast,No
POST,/comments,Add comment,Yes
DELETE,/comments/{id},Delete own comment,Yes
GET,/favorites,List user's favorites,Yes
POST,/favorites/{podcast_id},Add to favorites,Yes
DELETE,/favorites/{podcast_id},Remove from favorites,Yes
GET,/categories,List all categories,No
POST,/categories,Create category (admin later),Yes
Deployment
Backend

Recommended: Render, Railway, Fly.io, Heroku (free tiers available)
Use PostgreSQL instead of SQLite
Set DATABASE_URL and SECRET_KEY as environment variables
Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT

Frontend

Recommended: Vercel, Netlify
Build command: npm run build
Output directory: dist (Vite) or build (CRA)

License
This project is licensed under the MIT License — see the LICENSE file for details.
Acknowledgments
Built with passion during Phase 4 at Moringa School.
Special thanks to the instructors and team members for the collaboration.
