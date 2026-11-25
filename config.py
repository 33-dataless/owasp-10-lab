from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent / ".env")

    POSTGRES_USER: SecretStr = Field(validation_alias="POSTGRES_USER")
    POSTGRES_PSWD: SecretStr = Field(validation_alias="POSTGRES_PASSWORD")
    POSTGRES_HOST: SecretStr = Field(validation_alias="POSTGRES_HOST")
    POSTGRES_PORT: SecretStr = Field(validation_alias="POSTGRES_PORT")
    POSTGRES_DATABASE_NAME: SecretStr = Field(validation_alias="POSTGRES_DATABASE_NAME")

    DATABASE_URL: SecretStr = Field(validation_alias="DATABASE_URL")


config = Config()