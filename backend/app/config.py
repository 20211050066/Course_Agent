from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    JWT_SECRET: str
    JWT_EXPIRE_HOURS: int = 24
    JWT_ALGORITHM: str = "HS256"
    DATABASE_URL: str
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
