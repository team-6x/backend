"""Settings for database connection and sessions creation."""

import uuid
from typing import AsyncGenerator

from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import (
    Mapped,
    declarative_base,
    declared_attr,
    mapped_column,
)

from app.core.config import settings


class PreBase:
    """Fields and settings for Base model."""

    @declared_attr
    def __tablename__(cls):
        """Bind table name to the class name."""
        return cls.__name__.lower()

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.UUID)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.postgres_connection_url)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Create async db session."""
    async with AsyncSessionLocal() as async_session:
        yield async_session
