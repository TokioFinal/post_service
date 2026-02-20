import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    AUTH_SERVICE_URL : str
    class Config:
        env_file = f".env.local"
        
settings = Settings()