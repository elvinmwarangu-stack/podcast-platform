# 🚀 Deployment Guide

## Backend (Render)

### Step 1: Push to GitHub
```bash
cd backend
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repo
4. Select the `backend` folder
5. Configure:
   - **Name**: podcast-api
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Click "Create Web Service"

### Step 3: Add PostgreSQL Database
1. In Render dashboard, click "New +" → "PostgreSQL"
2. Name: podcast-db
3. Click "Create Database"
4. Copy the "Internal Database URL"

### Step 4: Set Environment Variables
In your web service settings:
- `DATABASE_URL` = (paste Internal Database URL)
- `SECRET_KEY` = (generate random string)

### Step 5: Deploy and Auto-Setup
1. Push your code to GitHub (Render will auto-deploy)
2. The application will automatically:
   - Create database tables
   - Run migrations (add missing columns)
   - Seed the database if empty
3. Monitor the deployment logs to ensure everything completes successfully

### Manual Setup (if needed):
If auto-setup fails, you can manually run:
1. Go to your web service → "Shell"
2. Run: `python3 startup_and_seed.py`

### Your Backend URL:
`https://your-app-name.onrender.com`

---

## Frontend (Vercel)

### Step 1: Create .env file
```bash
cd podacst-frontend
echo "VITE_API_URL=https://your-app-name.onrender.com" > .env
```

### Step 2: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### Step 3: Deploy on Vercel
1. Go to https://vercel.com
2. Click "Add New" → "Project"
3. Import your GitHub repo
4. Configure:
   - **Framework Preset**: Vite
   - **Root Directory**: podacst-frontend
   - **Build Command**: `npm run build`
   - **Output Directory**: dist
5. Add Environment Variable:
   - `VITE_API_URL` = `https://your-app-name.onrender.com`
6. Click "Deploy"

### Step 4: Update Backend CORS
Update `backend/app/main.py` with your Vercel URL:
```python
allow_origins=[
    "https://your-app.vercel.app",
]
```

---

## 🎉 Done!

**Frontend**: https://your-app.vercel.app
**Backend**: https://your-app-name.onrender.com
**API Docs**: https://your-app-name.onrender.com/docs

## Test Users:
- Username: `john_doe` / Password: `password123`
- Username: `jane_smith` / Password: `password123`
- Username: `mike_wilson` / Password: `password123`
