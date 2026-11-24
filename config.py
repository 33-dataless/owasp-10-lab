from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent / ".env")

    host: str = "127.0.0.1"
    port: int = 8000
    debug: bool = False
