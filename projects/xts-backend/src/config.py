from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration, loaded from environment variables (and a .env
    file when present). Add new settings here as typed fields so there is a
    single, documented place for configuration."""

    # Maps to the SQLALCHEMY_DATABASE_URL env var (matching is case-insensitive).
    sqlalchemy_database_url: str = "postgresql://postgres:test1234!@localhost/fastapi"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
