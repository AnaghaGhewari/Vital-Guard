from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, UTC
from typing import Optional
from core.config import settings

#CryotContext tells passlib which algorithm to use
#bcrypt is the industry standard for passwords

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#-------Password Hsahing---------
def hash_password(plain_password: str) -> str:
    """Hash a plain text password - call this on register"""
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password:str) ->  bool:
    """Check plain password against stored hash - call this on login"""
    return pwd_context.verify(plain_password, hashed_password)


#--------JWT token function--------
def create_token(user_id: int)->str:
    """ Generate a JWT token for the given user_id"""
    expire = datetime.now(UTC)+ timedelta(days=settings.jwt_expire_days)

    payload = {
        "sub": str(user_id),   #Subject -  who is this token for
        "exp": expire,         #Expiry - when the token will expire
        "iat":datetime.now(UTC)#issue at when token was created

    }

    return jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm= settings.jwt_algorithm
    )


def decode_token(token:str) ->Optional[dict]:
    """Decode and verify a JWT token - return payload or None"""
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm]
        )

        return payload
    except JWTError:
        return None  #expired, tempered, or invalide token



