import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    ANALYTIC_DATABASE_URL: str = os.getenv("ANALYTIC_DATABASE_URL")

    ANALYTIC_API_KEY: str = os.getenv("ANALYTIC_API_KEY")
    ANALYTIC_API_KEY_NAME: str = os.getenv("ANALYTIC_API_KEY_NAME")

    ANALYTIC_CORS_ORIGIN: str = os.getenv("ANALYTIC_CORS_ORIGIN")

    class Config:
        env_file =".env"

settings = Settings()