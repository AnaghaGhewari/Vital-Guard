from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from typing import Dict, List


#---------------REQUEST SCHEMAS---------------

class VitalCreate(BaseModel):
    """Used for POST /api/v1/vitals"""
    heart_rate:  int   = Field(..., ge=30, le=220, description="BPM")
    sleep_hours: float = Field(...,ge=0, le=24, description="Hours slept")
    steps:       int   = Field(...,ge=0 , description="Steps today")
    notes: Optional[str] = Field(None, max_length = 300)

    #Few new fields that are present in the ML model
    glucose:          Optional[float]=Field(None, ge=0, le=300, description="Blood glucose mg/dL")
    blood_pressure:   Optional[float]=Field(None, ge=0, le=200, description="Diastolic BP mmHg")
    bmi:              Optional[float]=Field(None, ge=0, le=80, description="Body mass index")
    age:              Optional[float]=Field(None, ge=1, le=120, description="Age in years")

#---------------RESPONSE SCHEMAS---------------

class VitalResponse(BaseModel):
    """Returned after POST /vitals or GET /vitals/{id}"""
    id:          int
    user_id:     int
    heart_rate:  int
    sleep_hours: float
    steps:       int
    notes:       Optional[str]
    logged_at:   datetime

    class Config:
        from_attributes=True

class VitalListResponse(BaseModel):
    """returned for GET/vitals - paginated list"""
    data:     list[VitalResponse]
    total:    int
    page:     int
    has_next: bool

#---------RISK SCHEMAS---------

class RiskFactor(BaseModel):
    factor:         int
    description:    str
    severity:       str 

class RiskResponse(BaseModel):
    """Returned for GET/risk/score"""
    user_id:    int
    risk_score: float = Field(..., ge=0.0, le=1.0)
    level:      str
    top_factors: list[str]
    shap_explanation: Dict[str, float] = {}
    explanation: str
    generated_at: datetime

    class Config:
        from_attributes = True

class RiskHistoryItem(BaseModel):
    id:         int
    risk_score: float
    level:      str
    top_factor: List[str]
    explanation:str
    generated_at:datetime

    class Config:
        from_attribute = True


class RiskHistoryResponse(BaseModel):
    data:    List[RiskHistoryItem]
    total:   int
    trend:   str



