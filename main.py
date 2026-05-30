from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from routers import auth, vitals, users



app = FastAPI(
    title= settings.app_name,
    version= settings.version,
    description= "AI - powered early warning systems for chroni disease risk"

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

#------Root and health
@app.get("/")
def root():
    return{
        "app": settings.app_name,
        "version": settings.version,
        "docs":"/docs"
    }

@app.get("health")
def health():
    return{"status":"ok"}