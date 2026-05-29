from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

#------------REQUEST SCHEMAS(WHAT CLIENT SENDS IN)--------------

class UserRegister(BaseModel):
    """Used for POST /auth/register"""
    name: str = Field(..., min_length=2, max_length =50)
    email:  EmailStr     #valid email format
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    """Used for POST/auth/login"""
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    """User for PUT/users/me - all field optional"""
    name: Optional[str]  = Field(None, min_length=2, max_length =50)
    email: Optional[EmailStr] = None

#------------RESPONSE SCHEMAS(WHAT SERVER SENDS OUT)--------------

"""Return after register or GET /usres/me
NOTE: password is NOT here - it never goes to the client"""

class UserResponse(BaseModel):
    id:         int
    name:       str
    email:      str
    created_at: datetime

    class Config:
        from_attributes = True   #allows reading from DB object 

class TokenResponse(BaseModel):
    """Returns after the successful login"""
    access_token: str
    token_type:   str ="bearer"
    user_id:      int

