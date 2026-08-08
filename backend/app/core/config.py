import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Universal Wakala Agency System"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "WAKALA_BUSINESS_SUPER_SECRET_KEY_2026_PRODUCTION")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # Siku 1

    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./wakala_system.db")

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()