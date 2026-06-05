from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


#---------------REQUEST SCHEMAS---------------

class VitalCreate(BaseModel):
    """Used for POST /api/v1/vitals"""
    heart_rate:  int   = Field(..., ge=30, le=220, description="BPM")
    sleep_hours: float = Field(...,ge=0, le=24, description="Hours slept")
    steps:       int   = Field(...,ge=0 , description="Steps today")
    notes: Optional[str] = Field(None, max_length = 300)

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
    top_factor: list[str]
    explaination: str
    generated_at: datetime

    class Config:
        from_attributes = True


