# app/api/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app import crud, schemas, utils
from app.dependencies import get_db, create_access_token
from app.models.user import User

router = APIRouter(tags=["auth"])


# REGISTER USER
@router.post("/register", response_model=schemas.UserOut, status_code=201)
def register_user(
    user_in: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    print(f"Register attempt: {user_in.email}, {user_in.username}")

    if crud.get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if crud.get_user_by_username(db, user_in.username):
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = utils.get_password_hash(user_in.password)
    db_user = User(
        email=user_in.email,
        username=user_in.username,
        hashed_password=hashed_password,
        full_name=user_in.full_name,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# LOGIN USER
@router.post("/login", response_model=schemas.Token)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    # Token expiration time (default 30 minutes)
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
