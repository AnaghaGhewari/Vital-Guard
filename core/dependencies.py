from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db.session import get_db
from models.user import User
from core.security import decode_token


#Read Autherization : Bearer header automatically
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_current_user(
        token: str = Depends(oauth2_scheme),   #Extaracts the token from header
        db : Session = Depends(get_db)        #Gives the database sessions
) -> User:
    


    #Step 1 - decode the token
    payload = decode_token(token)
    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalide or expired token"
        )
    
    #Step 2 - extarct user-id from payload
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail= "Token is missing user information"
        )
    
    #Step 3 - fetch the user from the database
    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User no longer exists"
        )
    
    #Step 4 - check user is still active
    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="User is no longer active"
        )
    
    return user    #passed directly into route function