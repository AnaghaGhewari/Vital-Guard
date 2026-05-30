from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name : str = "VitalGuard"
    version : str ="1.0.0"
    debug : bool = True
    secret_key : str= "fallback-secret"

    class Config:
        env_file = ".env"


settings = Settings() 


#Quick test - run this file directly to vefify

if __name__== "__main__":
    print(settings.app_name)
    print(settings.secret_key)






    
