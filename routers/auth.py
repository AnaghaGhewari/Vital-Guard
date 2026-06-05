from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from schemas.user import UserRegister, UserLogin, UserResponse, TokenResponse
from sqlalchemy.orm import Session
from db.session import get_db
from models.user import User
from core.security import hash_password, verify_password, create_token
from sqlalchemy.exc import SQLAlchemyError
from fastapi.security import OAuth2PasswordRequestForm

#APIRouter is like a mini FastAPI app for one feature
# prefix   → added to every route in this file automatically
# tags     → groups routes together in Swagger docs

routers = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])




@routers.post("/register", response_model=UserResponse, status_code=201)
def register(data: UserRegister, db: Session = Depends(get_db)):
    # Check duplicate email
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    try:
        user= User(
            name=data.name,
            email=data.email,
            password=hash_password(data.password)  #Hashing done
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Could not create user")
    


@routers.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),  # ← replaces UserLogin
    db: Session = Depends(get_db)
):
    # OAuth2PasswordRequestForm uses "username" field
    # We treat username AS email — user types their email in the username box
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user_id=user.id)

    return {
        "access_token": token,
        "token_type":   "bearer",
        "user_id":      user.id
    }
