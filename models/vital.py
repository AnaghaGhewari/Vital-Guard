from sqlalchemy import Column, Integer,Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.session import Base

class Vital(Base):
    __tablename__="vitals"


    id              =  Column(Integer, primary_key=True, index=True)
    user_id         =  Column(Integer, ForeignKey("users.id"), nullable=False)
    heart_rate      =  Column(Integer, nullable=False)
    sleep_hours     =  Column(Integer, nullable=False)
    steps           =  Column(Integer, nullable=False)
    glucose         =  Column(Integer, nullable=True)
    blood_pressure  =  Column(Integer, nullable=True)
    bmi             =  Column(Integer, nullable=True)
    age             =  Column(Integer, nullable=True)
    notes           =  Column(String(300), nullable=True)
    logged_at       =  Column(DateTime(timezone=True), server_default=func.now())

    #Relationship - lets you do vital.user to get the User objects

    user = relationship("User", backref="vitals")