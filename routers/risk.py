```python
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from db.session import get_db
from models.user import User
from models.vital import Vital
from models.risk import RiskScore
from schemas.vital import RiskResponse, RiskHistoryResponse
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

    try:
        record = RiskScore(
            user_id=current_user.id,
            risk_score=result["risk_score"],
            level=result["level"],
            top_factors=result["top_factors"],
            shap_values=result["shap_explanation"],
            explanation=result["explanation"]
        )

        db.add(record)
        db.commit()

    except SQLAlchemyError:
        db.rollback()  # don't fail request if save fails

    factors_str = ", ".join(result["top_factors"])

    explanation = f"Risk level is {result['level']}."

    if factors_str:
        explanation += f" Key factors: {factors_str}."

    if result["used_defaults"]:
        missing = ", ".join(result["missing_fields"])
        explanation += (
            f" Missing values ({missing}) used population averages."
        )

    return {
        "user_id": current_user.id,
        "risk_score": result["risk_score"],
        "level": result["level"],
        "top_factors": result["top_factors"],
        "shap_explanation": result["shap_explanation"],
        "explanation": result["explanation"],
        "generated_at": datetime.utcnow()
    }


@router.get("/history", response_model=RiskHistoryResponse)
def get_risk_history(
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    records = (
        db.query(RiskScore)
        .filter(RiskScore.user_id == current_user.id)
        .order_by(RiskScore.generated_at.desc())
        .limit(limit)
        .all()
    )

    total = (
        db.query(RiskScore)
        .filter(RiskScore.user_id == current_user.id)
        .count()
    )

    trend = "insufficient_data"

    if len(records) >= 3:
        recent = [r.risk_score for r in records[:3]]

        avg_recent = sum(recent) / len(recent)

        if len(records) > 3:
            avg_older = (
                sum(r.risk_score for r in records[3:])
                / len(records[3:])
            )

            diff = avg_recent - avg_older

            if diff < -0.05:
                trend = "improving"
            elif diff > 0.05:
                trend = "worsening"
            else:
                trend = "stable"
        else:
            trend = "stable"

    return {
        "data": records,
        "total": total,
        "trend": trend
    }

