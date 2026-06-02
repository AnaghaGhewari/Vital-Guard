from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from schemas.user import UserRegister, UserLogin, UserResponse, TokenResponse
from sqlalchemy.orm import Session
from db.session import get_db
from models.user import User
from core.security import hash_password, verify_password
from sqlalchemy.exc import SQLAlchemyError

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
    


@routers.post("/login" , response_model=TokenResponse)
def login (data: UserLogin, db:Session = Depends(get_db)):
    #Find user by  email
    user = db.query(User).filter(User.email == data.email).first()
    if not user or verify_password(data.password, user.password):
        raise HTTPException(
            status_code= 401,
            detail="Invalid Credentials"
        )
    #plain password check for now - bcrypt later
    return {
        "access_token": "fake_token_replaced_week4",
        "token_type":   "bearer",
        "user_id":      user.id
    }
