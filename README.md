# Podcast / Audio Content Platform

**Podcast Platform** is a full-stack web application that allows users to upload, discover, stream, comment on, and favorite podcast-style audio content.

It includes a **React (Vite) single-page application** frontend and a **FastAPI** backend with JWT authentication, secure file uploads, and relational database support.

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

## Contributors

- Elvin
- Brian
- Wangeshii
- Muhammad

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
- React (Vite)
- React Router
- Tailwind CSS

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
```text
Podcast-platform/
  backend/
    app/
    requirements.txt
  podacst-frontend/
    src/
    package.json
  README.md
  DEPLOYMENT.md
  render.yaml
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend folder:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in `backend/`:
   ```env
   SECRET_KEY=your-very-long-random-secret-key
   DATABASE_URL=sqlite:///./podcast_app.db
   ```

5. Create database tables:
   ```bash
   python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
   ```

6. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```

API docs:

- `http://127.0.0.1:8000/docs`

### Frontend Setup

1. Navigate to the frontend folder:
   ```bash
   cd podacst-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure the API base URL (optional, recommended for deployment):
   ```env
   VITE_API_URL=http://127.0.0.1:8000
   ```

4. Start the dev server:
   ```bash
   npm run dev
   ```

Frontend typically runs at `http://localhost:5173`.

## API Endpoints Overview

| Method | Endpoint | Description | Auth |
| --- | --- | --- | --- |
| POST | `/auth/register` | Register new user | No |
| POST | `/auth/login` | Login & get JWT | No |
| POST | `/auth/forgot-password` | Request password reset | No |
| PATCH | `/auth/reset-password` | Reset password with token | No |
| GET | `/users/me` | Get current user profile | Yes |
| PUT | `/users/me` | Update profile | Yes |
| GET | `/podcasts` | List podcasts (supports `?search=` and `?category=`) | No |
| GET | `/podcasts/{id}` | Get podcast details | No |
| POST | `/podcasts` | Upload new podcast + audio | Yes |
| PUT | `/podcasts/{id}` | Update podcast (owner only) | Yes |
| DELETE | `/podcasts/{id}` | Delete podcast (owner only) | Yes |
| PATCH | `/podcasts/{id}/listen` | Increment listen count | No |
| GET | `/podcasts/{id}/comments` | Get comments for podcast | No |
| POST | `/comments` | Add comment | Yes |
| DELETE | `/comments/{id}` | Delete own comment | Yes |
| GET | `/favorites` | List user's favorites | Yes |
| POST | `/favorites/{podcast_id}` | Add to favorites | Yes |
| DELETE | `/favorites/{podcast_id}` | Remove from favorites | Yes |
| GET | `/categories` | List all categories | No |
| POST | `/categories` | Create category | Yes |

## Deployment

See `DEPLOYMENT.md` for step-by-step deployment instructions (Render + Vercel).

### Backend

Recommended: Render, Railway, Fly.io, Heroku (free tiers available)
Use PostgreSQL instead of SQLite
Set DATABASE_URL and SECRET_KEY as environment variables
Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT

### Frontend

Recommended: Vercel, Netlify
Build command: npm run build
Output directory: dist (Vite) or build (CRA)

## License
This project is licensed under the MIT License — see the LICENSE file for details.

## Acknowledgments

Built during Phase 4 at Moringa School.
