from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from db.session import get_db
from models.user import User
from models.vital import Vital
from schemas.vital import RiskResponse
from core.dependencies import get_current_user
from services import risk_engine


router = APIRouter(
    prefix="/api/v1/risk",
    tags=["Risk"]
)


@router.get("/score", response_model=RiskResponse)
def get_risk_score(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Generate a diabetes risk score for the current user.
    Uses the most recent vital record.
    """

    latest = (
        db.query(Vital)
        .filter(Vital.user_id == current_user.id)
        .order_by(Vital.logged_at.desc())
        .first()
    )

    if latest is None:
        raise HTTPException(
            status_code=404,
            detail="No vitals logged yet. Please log your vitals first."
        )

    result = risk_engine.predict(
        glucose=latest.glucose,
        blood_pressure=latest.blood_pressure,
        bmi=latest.bmi,
        age=latest.age
    )

    factors_str = ", ".join(result["top_factors"])

    explanation = (
        f"Risk level is {result['level']}."
    )

    if factors_str:
        explanation += f" Key factors: {factors_str}."

    if result["used_defaults"]:
        missing = ", ".join(result["missing_fields"])
        explanation += (
            f" Missing values ({missing}) were estimated using "
            f"population averages."
        )

    return {
        "user_id": current_user.id,
        "risk_score": result["risk_score"],
        "level": result["level"],
        "top_factors": result["top_factors"],
        "explanation": explanation,
        "generated_at": datetime.utcnow()
    }


@router.get("/history")
def get_risk_history(
    current_user: User = Depends(get_current_user)
):
    """
    Placeholder endpoint for future risk history tracking.
    """

    return {
        "message": "Risk history coming in Week 5",
        "data": []
    }