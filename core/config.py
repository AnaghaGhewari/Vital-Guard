from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name : str = "VitalGuard"
    version : str ="1.0.0"
    debug : bool = True
    secret_key : str= "changeme"
    database_url : str = "postgresql://postgres:postgres@localhost:5432/vitalguard"
    jwt_secret_key: str= "changeme_jwt"
    jwt_algorithm: str= "HS256"
    jwt_expire_days: int = 30

    class Config:
        env_file = ".env"


settings = Settings() 










    
