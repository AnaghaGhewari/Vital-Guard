from fastapi import APIRouter, HTTPException
from datetime import datetime
from schemas.user import UserRegister, UserLogin, UserResponse, TokenResponse

#APIRouter is like a mini FastAPI app for one feature
# prefix   → added to every route in this file automatically
# tags     → groups routes together in Swagger docs

routers = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])

#Fake in-memory user - replaced by the DB later
FAKE_USERS= []

@routers.post("/register", response_model=UserResponse, status_code =201)
def register(data: UserRegister):
    #Check if the email already exists
    existing = [u for u in FAKE_USERS if u["email"]==data.email]
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already regitered"

        )
    user={
        "id":         len(FAKE_USERS)+1,
        "name":       data.name,
        "email":      data.email,
        "created_at": datetime.now()

    }

    FAKE_USERS.append(user)
    return user

@routers.post("/login" , response_model=TokenResponse)
def login (data: UserLogin):
    #Find user by  email
    user = next((u for u in FAKE_USERS if u["email"] == data.email),None)
    if not user:
        raise HTTPException(
            status_code= 401,
            detail="Invalid email or password"
        )
    #Real password check comes later
    return{
        "access_token":   "fake_token_replace_in_week4",
        "token_type":     "bearer",
        "user_id":        user["id"]
    }
