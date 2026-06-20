from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Optional
from schemas.vital import VitalCreate, VitalResponse, VitalListResponse
from sqlalchemy.orm import Session
from db.session import get_db
from models.vital import Vital
from sqlalchemy.exc import SQLAlchemyError
from core.dependencies import get_current_user
from models.user import User



routers = APIRouter(prefix="/api/v1/vitals", tags=["Vitals"])



# ── POST /api/v1/vitals ───────────────────────────────
@routers.post("", response_model=VitalResponse, status_code=201)
def log_vital(data: VitalCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        vital = Vital(
            user_id=current_user.id,
            heart_rate=data.heart_rate,
            sleep_hours=data.sleep_hours,
            steps=data.steps,
            
#The vitals that the model requires
            glucose = data.glucose,
            blood_pressure=data.blood_pressure,
            bmi=data.bmi,
            age=data.age,

            notes=data.notes
        )
        db.add(vital)
        db.commit()
        db.refresh(vital)
        return vital
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Could not save vital")
      
    
# ── GET /api/v1/vitals ────────────────────────────────
# Query params: ?page=1&limit=20
@routers.get("", response_model=VitalListResponse)
def get_vitals(
    page:  int = Query(1,  ge=1,         description="Page number"),
    limit: int = Query(20, ge=1, le=100,  description="Items per page"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    
    #Filter by current_user.id -  user only will see their own vitals
    query = db.query(Vital).filter(Vital.user_id == current_user.id)
    total  = query.count()
    vitals = query\
    .offset((page-1)*limit)\
    .limit(limit)\
    .all()
    

    return {
        "data":     vitals,
        "total":    total,
        "page":     page,
        "has_next": (page*limit)<total
    }

# ── GET /api/v1/vitals/{id} ───────────────────────────
# {id} is a path parameter — part of the URL itself
@routers.get("/{vital_id}", response_model=VitalResponse)
def get_vital(vital_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    vital = db.query(Vital).filter(Vital.id == vital_id, Vital.user_id == current_user.id).first()
    if not vital:
        raise HTTPException(status_code=404, detail=f"Vital {vital_id} not found")
    return vital

# ── DELETE /api/v1/vitals/{id} ────────────────────────
@routers.delete("/{vital_id}", status_code=204)
def delete_vital(vital_id: int, db: Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    vital = db.query(Vital).filter(Vital.id == vital_id, Vital.user_id == current_user.id).first()
    if not vital:
        raise HTTPException(status_code=404, detail=f"Vital {vital_id} not found")
    db.delete(vital)
    db.commit()
