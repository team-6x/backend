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
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

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

    """os.makedirs("./upload_dir/lookup_order_file", 0o777, exist_ok=True)
    container = LocalStorageDriver("./upload_dir").get_container(
        "lookup_order_file",
    )
    container = LocalStorageDriver("./upload_dir").get_container(
        "job_opening_file",
    )
    StorageManager.add_storage("default", container)"""

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
