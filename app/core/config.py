"""Project settings."""

import os  # noqa
from typing import Optional

from libcloud.storage.drivers.local import LocalStorageDriver  # noqa
from pydantic import EmailStr, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL
from sqlalchemy_file.storage import StorageManager  # noqa


class Settings(BaseSettings):
    """Pydantic validated settings."""

    secret: str = "SECRET"
    first_superuser_email: Optional[EmailStr] = "q@q.ru"
    first_superuser_password: Optional[str] = "qweqweqwe1!"
    first_superuser_phone_number: Optional[str] = "+79871509287"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_title: str = "HRSpace"

    postgres_db: str
    postgres_user: str
    postgres_password: SecretStr
    postgres_host: str
    postgres_port: int

    @property
    def postgres_connection_url(self) -> URL:
        """Return URL for connections establishing to postgres."""
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.postgres_user,
            password=self.postgres_password.get_secret_value(),
            host=self.postgres_host,
            port=self.postgres_port,
            database=self.postgres_db,
        )


settings = Settings()
