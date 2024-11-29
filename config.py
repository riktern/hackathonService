import os


class Config:
    """Service configurations"""

    APP_TITLE = os.environ.get("APP_TITLE", "FastAPI template")
    APP_DESCRIPTION = os.environ.get("APP_DESCRIPTION", "A template for FastAPI.")
    VERSION = os.environ.get("VERSION", "0.0.0")
    OPENAPI_URL = os.environ.get("OPENAPI_URL", "/openapi.json")

    DB_URL = os.environ.get(
        "DB_URL", "postgresql+asyncpg://postgres:password@db:5432/hack_service_db"
    )