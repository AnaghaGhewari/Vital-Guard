from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.session import Base

class RiskScore(Base):
    __tablename__="risk_score"

    id              =  Column(Integer, primary_key=True, index=True)
    user_id         =  Column(Integer, ForeignKey("users.id"), nullable=False)
    risk_score      =  Column(Float, nullable=False)
    level           =  Column(String(10), nullable=False)
    top_factors     =  Column(JSON, nullable=True)    #stores List as JSON
    shap_values     =  Column(JSON, nullable=True)    #stores Dict as JSON
    explanation     =  Column(String(500), nullable=True)
    generated_at    =  Column(DateTime(timezone=True),server_default=func.now())

    user = relationship("User", backref="risk_scores")