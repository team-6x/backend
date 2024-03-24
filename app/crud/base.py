"""Contains basic CRUD operations."""

import uuid
from typing import Optional, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base
from app.models.user import User

ModelType = TypeVar("ModelType", bound=Base)


class CRUDBase:
    """A base class for performing CRUD operations."""

    def __init__(self, model):
        """Initialize the CRUDBase object."""
        self.model = model

    async def get(
        self,
        session: AsyncSession,
        obj_id: uuid.UUID,
    ) -> Optional[ModelType]:
        """Get an object of this type."""
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == obj_id,
            ),
        )
        return db_obj.scalars().first()

    async def get_all(
        self,
        session: AsyncSession,
    ):
        """Get all objects of this type."""
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()

    async def create(
        self,
        obj_schema,
        session: AsyncSession,
        user: Optional[User] = None,
    ):
        """Create a new object."""
        obj_data = obj_schema.dict()
        if user:
            obj_data["employer_id"] = user.id
        db_obj = self.model(**obj_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj
