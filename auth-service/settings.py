import os

from pydantic_settings import BaseSettings
from urllib.parse import quote_plus

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str
    SECRET_KEY: str = "your-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

    @property
    def DATABASE_URL(self) -> str:
        safe_password = quote_plus(self.DB_PASSWORD)
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{safe_password}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
settings = Settings()