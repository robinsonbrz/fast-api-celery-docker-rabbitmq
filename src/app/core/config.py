from pydantic import BaseSettings, PostgresDsn
from typing import Optional

import os
from enum import Enum
from starlette.config import Config

current_file_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(current_file_dir, "..", "..", ".env")
config = Config(env_path)

class AppSettings(BaseSettings):
    APP_NAME: str = config("APP_NAME", default="FastAPI app")
    APP_DESCRIPTION: str | None = config("APP_DESCRIPTION", default=None)
    APP_VERSION: str | None = config("APP_VERSION", default=None)
    LICENSE_NAME: str | None = config("LICENSE", default=None)
    CONTACT_NAME: str | None = config("CONTACT_NAME", default=None)
    CONTACT_EMAIL: str | None = config("CONTACT_EMAIL", default=None)


class CryptSettings(BaseSettings):
    SECRET_KEY: str = config("SECRET_KEY")
    ALGORITHM: str = config("ALGORITHM", default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = config("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)
    REFRESH_TOKEN_EXPIRE_DAYS: int = config("REFRESH_TOKEN_EXPIRE_DAYS", default=7)


class EnvironmentOption(Enum):
    LOCAL = "local"
    STAGING = "staging"
    PRODUCTION = "production"


class DBOption(Enum):
    POSTGRES = "postgres"
    SQLITE = "sqlite"


class EnvironmentSettings(BaseSettings):
    ENVIRONMENT: EnvironmentOption = config("ENVIRONMENT", default="local")
    DB_ENGINE: DBOption = config("DB_ENGINE", default="POSTGRES")


class DatabaseSettings(BaseSettings):
    pass

class SQLiteSettings(DatabaseSettings):
    SQLITE_URI: str = config("SQLITE_URI", default="./sql_app.db")
    SQLITE_SYNC_PREFIX: str = config("SQLITE_SYNC_PREFIX", default="sqlite:///")
    SQLITE_ASYNC_PREFIX: str = config("SQLITE_ASYNC_PREFIX", default="sqlite+aiosqlite:///")


class PostgresSettings(DatabaseSettings):
    POSTGRES_USER: str = config("POSTGRES_USER", default="postgres")
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD", default="postgres")
    POSTGRES_SERVER: str = config("POSTGRES_SERVER", default="localhost")
    POSTGRES_PORT: int = config("POSTGRES_PORT", default=5432)
    POSTGRES_DB: str = config("POSTGRES_DB", default="postgres")
    POSTGRES_SYNC_PREFIX: str = config("POSTGRES_SYNC_PREFIX", default="postgresql://")
    POSTGRES_ASYNC_PREFIX: str = config("POSTGRES_ASYNC_PREFIX", default="postgresql+asyncpg://")
    POSTGRES_URI: str = f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    POSTGRES_URL: str | None = config("POSTGRES_URL", default=None)
    

# class Settings(BaseSettings):
#     # Database configurations
#     POSTGRES_DB: str
#     POSTGRES_USER: str
#     POSTGRES_PASSWORD: str
#     POSTGRES_SERVER: str
#     POSTGRES_PORT: str
#     RABBITMQ_DEFAULT_USER: str
#     RABBITMQ_DEFAULT_PASS: str
#     RABBITMQ_DEFAULT_HOST: str

    
db_type = PostgresSettings
if config("DB_ENGINE", default="sqlite") == "sqlite":
    db_type = SQLiteSettings

class RabbitMqQueueSettings(BaseSettings):
    RABBITMQ_DEFAULT_USER: str = config("RABBITMQ_DEFAULT_USER", default="guest")
    RABBITMQ_DEFAULT_PASS: str = config("RABBITMQ_DEFAULT_PASS", default="guest")
    RABBITMQ_DEFAULT_HOST: str = config("RABBITMQ_DEFAULT_HOST", default="localhost")
    RABBITMQ_DEFAULT_PORT: int = config("RABBITMQ_DEFAULT_PORT", default=5672)
    RABBIT_URL: str = f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@{RABBITMQ_DEFAULT_HOST}:{RABBITMQ_DEFAULT_PORT}//"


class Settings(
    AppSettings,
    db_type,
    CryptSettings,
    EnvironmentSettings,
    RabbitMqQueueSettings,
):
    pass


settings = Settings()
