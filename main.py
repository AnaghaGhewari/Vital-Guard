from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from routers import auth, vitals, users, risk
from db.session import engine, Base
from models import user, vital
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from core.exception import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler
)



#Create all tables in PostgreSQL on startup
Base.metadata.create_all(bind = engine)


app = FastAPI(
    title= settings.app_name,
    version= settings.version,
    description= "AI - powered early warning systems for chronic disease risk"

)
#Exception Handler
app.add_exception_handler(
    StarletteHTTPException,
    http_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)



#-------CORS - allows the React frontend to call this API

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#------Plug in all routers-------
app.include_router(auth.routers)
app.include_router(users.routers)
app.include_router(vitals.routers)
app.include_router(risk.router)

#------Root and health
@app.get("/")
def root():
    return{
        "app": settings.app_name,
        "version": settings.version,
        "docs":"/docs"
    }

@app.get("/health")
def health():
    return{"status":"ok"}
