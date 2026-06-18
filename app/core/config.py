from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Resume Agent Platform"
    app_env: str = "local"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    llm_provider: str = "mock"
    llm_api_key: str | None = None
    llm_model: str = "mock-resume-agent"
    database_path: str = "data/resume_agent.db"
    outputs_dir: str = "outputs"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
