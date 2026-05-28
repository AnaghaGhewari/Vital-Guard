from pydantic_settings import BaseSettings
from pydantic import BaseModel, Field

class Settings(BaseSettings):
    app_name : str = "VitalGuard"
    version : str ="1.0.0"
    debug : bool = True

settings = Settings() 

class VitalLog(BaseModel):
    heart_rate : int = Field(..., ge = 30, le = 220)
    sleep_hours : float = Field(..., ge= 0, le= 24)
    steps: int = Field(..., ge=0)

    




    
