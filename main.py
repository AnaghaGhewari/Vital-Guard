from fastapi import FastAPI
from core.config import settings

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
    return {"status":"ok"}

