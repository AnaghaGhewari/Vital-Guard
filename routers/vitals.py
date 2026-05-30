from fastapi import APIRouter, HTTPException, Query
from datetime import datetime
from typing import Optional
from schemas.vital import VitalCreate, VitalResponse, VitalListResponse

routers = APIRouter(prefix="/api/v1/vitals", tags=["Vitals"])

# Fake in-memory store — replaced by DB in week 3
FAKE_VITALS = [
    {"id": 1, 
     "user_id": 1, 
     "heart_rate": 88,
     "sleep_hours": 5.5, 
     "steps": 4200, "notes": None,
     "logged_at": datetime.now()},

    {"id": 2, 
     "user_id": 1, 
     "heart_rate": 72,
     "sleep_hours": 7.0, 
     "steps": 8900, "notes": "good day",
     "logged_at": datetime.now()},
]
next_id = 3

# ── POST /api/v1/vitals ───────────────────────────────
@routers.post("", response_model=VitalResponse, status_code=201)
def log_vital(data: VitalCreate):
    global next_id
    record = {
        "id":          next_id,
        "user_id":     1,       # hardcoded for now, week 4 uses real auth
        "heart_rate":  data.heart_rate,
        "sleep_hours": data.sleep_hours,
        "steps":       data.steps,
        "notes":       data.notes,
        "logged_at":   datetime.now()
    }
    FAKE_VITALS.append(record)
    next_id += 1
    return record

# ── GET /api/v1/vitals ────────────────────────────────
# Query params: ?page=1&limit=20
@routers.get("", response_model=VitalListResponse)
def get_vitals(
     page:  int = Query(1,  ge=1,         description="Page number"),
    limit: int = Query(20, ge=1, le=100,  description="Items per page")
):
    start = (page - 1) * limit
    end   = start + limit
    page_data = FAKE_VITALS[start:end]

    return {
        "data":     page_data,
        "total":    len(FAKE_VITALS),
        "page":     page,
        "has_next": end < len(FAKE_VITALS)
    }

# ── GET /api/v1/vitals/{id} ───────────────────────────
# {id} is a path parameter — part of the URL itself
@routers.get("/{vital_id}", response_model=VitalResponse)
def get_vital(vital_id: int):
    vital = next((v for v in FAKE_VITALS if v["id"] == vital_id), None)
    if not vital:
        raise HTTPException(status_code=404, detail=f"Vital {vital_id} not found")
    return vital

# ── DELETE /api/v1/vitals/{id} ────────────────────────
@routers.delete("/{vital_id}", status_code=204)
def delete_vital(vital_id: int):
    global FAKE_VITALS
    original_len = len(FAKE_VITALS)
    FAKE_VITALS = [v for v in FAKE_VITALS if v["id"] != vital_id]
    if len(FAKE_VITALS) == original_len:
        raise HTTPException(status_code=404, detail=f"Vital {vital_id} not found")
    # 204 No Content — return nothing on delete
