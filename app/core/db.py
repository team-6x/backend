"""Settings for database connection and sessions creation."""

import uuid
from typing import Annotated, AsyncGenerator

from sqlalchemy import String
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

from app.core.config import settings
from app.core.constants import LIMIT_CHAR_256

str_256 = Annotated[str, LIMIT_CHAR_256]


class PreBase:
    """Fields and settings for Base model."""

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    type_annotation_map = {
        str_256: String(LIMIT_CHAR_256),
    }


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.postgres_connection_url)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Create async db session."""
    async with AsyncSessionLocal() as async_session:
        yield async_session
