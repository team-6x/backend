"""Project settings."""

from pydantic import SecretStr
import os

from libcloud.storage.drivers.local import LocalStorageDriver
from typing import Optional

from pydantic import EmailStr, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL
from sqlalchemy_file.storage import StorageManager


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

    app_title: str = "WhatsApp bot"

    db_name: str
    db_username: str
    db_password: SecretStr
    db_host: str
    db_port: int

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
            username=self.db_username,
            password=self.db_password.get_secret_value(),
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
        )


settings = Settings()
