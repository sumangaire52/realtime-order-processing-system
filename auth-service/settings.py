import os

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "your-database-url"
    SECRET_KEY: str = "your-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()