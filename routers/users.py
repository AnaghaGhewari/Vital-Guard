from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from schemas.user import UserResponse, UserUpdate
from sqlalchemy.orm import Session
from db.session import get_db
from models.user import User
from core.dependencies import get_current_user

routers = APIRouter(prefix="/api/v1/user", tags=["Users"])
#FAKE_USER Relpaced later



#---------GET/api/v1/user/me---------
@routers.get("/me", response_model=UserResponse)
def get_my_profile(
    current_user: User = Depends(get_current_user)
):
    
    return current_user


@routers.put("/me",response_model=UserResponse)
def update_my_profile(
    data:       UserUpdate,
    db:         Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if data.name is not None:
        current_user.name = data.name
    if data.email is not None:
        #check new email is not taken by another user
        existing = db.query(User).filter(
            User.email == data.email,
            User.id != current_user.id
        ).first()
        if existing:
            raise HTTPException(
                status_code= 400,
                detail="Email already taken"
            )
        current_user.email = data.email

    db.commit()
    db.refresh(current_user)
    return current_user