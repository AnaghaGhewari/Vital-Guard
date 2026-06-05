from fastapi import APIRouter,Depends
from datetime import datetime
from sqlalchemy.orm import Session
from db.session import get_db
from models.user import User
from models.vital import Vital
from schemas.vital import RiskResponse
from core.dependencies import get_current_user

router = APIRouter(prefix="/api/v1/risk", tags = ["Risk"])

@router.get("/score", response_model= RiskResponse)
def get_risk_response(
    db:       Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    #Fetch user's last 7 vitals
    vitals = db.query(Vital).\
             filter(Vital.user_id == current_user.id).\
            order_by(Vital.logged_at.desc()).\
            limit(7).all()
    
    #Placeholder  -  real ML replaceses this in the week 5

    return{
        "risk_score":  0.0,
        "level":      "unavailable",
        "top_factor": [],
        "explanation": f"ML model comming in the 5th week{len(vitals)}",
        "generated_at": datetime.now()
    }
@router.get("/history")
def get_risk_history(
    current_user: User = Depends(get_current_user)
):
    
    #Placeholder in the week 5
    return{"message":"Risk history coming in week 5", "data":[]}
    
