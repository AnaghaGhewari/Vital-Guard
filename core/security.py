from passlib.context import CryptContext

#CryotContext tells passlib which algorithm to use
#bcrypt is the industry standard for passwords

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    """Hash a plain text password - call this on register"""
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password:str) ->  bool:
    """Check plain pawword against stored hash - call this on login"""
    return pwd_context.verify(plain_password, hashed_password)


