from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

#Engine the actual connection to the PostgreSQL
engine = create_engine(settings.database_url)

#SessionLocal - a factory that creates the DB sessions
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)


#Base all your ORM models inherit from this 

Base = declarative_base()

#get_db - FastAPI dependency, gives each request a DB session
#yield gives the session to the route, finally closes it
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close ()

  
