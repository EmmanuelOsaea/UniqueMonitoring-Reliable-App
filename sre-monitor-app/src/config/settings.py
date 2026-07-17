import os
from pydantic_settings import
BaseSettings

class Settings(BaseSettings):
 APP_NAME:str = "SRE Monitor Detector"
 AZURE_CLIENT_ID: str = 
 os.getenv("AZURE_CLIENT_ID", "")

AZURE_TENANT_ID: str =
os.getenv("AZURE_TENANT_ID", "")

class Config
env_file = ".env"
        
settings = Settings()
