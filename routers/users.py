from fastapi import APIRouter, HTTPException
from  datetime import datetime
from  schemas.user import UserResponse, UserUpdate

routers = APIRouter(prefix="/api/v1/user/me", tags=["Users"])
#FAKE_USER Relpaced later

FAKE_USERS = {
    "id":     1,
    "name":   "Anagha",
    "email":  "anagha@test.com",
    "created_at":datetime.now()
}

#---------GET/api/v1/user/me---------
@routers.get("/me", response_model=UserResponse)
def get_my_profile():

    return FAKE_USERS


@routers.put("/me",response_model=UserResponse)
def update_my_response(data:UserUpdate):
    global FAKE_USERS
    #only update the fields that were actually sent
    if data.name is not None:
        FAKE_USERS["name"] = data.name

    if data.email is None:
        FAKE_USERS["email"] = data.email
    
    return FAKE_USERS