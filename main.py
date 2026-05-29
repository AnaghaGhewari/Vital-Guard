from fastapi import FastAPI
from core.config import settings
from datetime import datetime

app = FastAPI(
    title= settings.app_name,
    version= settings.version,
    description= "AI - powered early warning systems for chroni disease risk"

)

@app.get("/")
def root():
    return {
        "app":settings.app_name,
        "version": settings.version,
        "status":"running",
        "docs": "/docs"
    }

@app.get("/health")
def health():
    return {"status":"ok","app":settings.app_name}

@app.post("/api/v1/auth/register", response_model=UserResponse)
def register(data: UserRegister):
    # No DB yet — return fake response with correct shape
    return{
        "id":        1,
        "name":     data.name,
        "email":    data.email,
        "created":  datetime.now()

    }

@app.post("api/v1/vitals",response_model=VitalsResponse)
def log_vitals(data: VitalCreate):
    # No DB yet — return fake response with correct shape
    return{
        "id":            1,
        "user_id":       1,
        "heart_rate":    data.heart_rate,
        "sleep_hours":   data.sleep_hours,
        "steps":         data.steps,
        "notes":         data.notes,
        "logged_at":     datetime.now()
    }
