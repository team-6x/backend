"""Contains basic CRUD operations."""

import uuid
from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


class CRUDBase:
    """A base class for performing CRUD operations."""

    def __init__(self, model):
        """Initialize the CRUDBase object."""
        self.model = model

    async def get(
        self,
        obj_id: uuid.UUID,
        session: AsyncSession,
    ):
        """Get an object by its UUID."""
        db_obj = await session.get(self.model, obj_id)
        return db_obj

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

    async def update(
        self,
        db_obj,
        obj_schema,
        session: AsyncSession,
    ):
        """Update an existing object."""
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_schema.dict()
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        await session.refresh(db_obj)
        await session.commit()
        return db_obj

    async def remove(
        self,
        db_obj,
        session: AsyncSession,
    ):
        """Delete an existing object."""
        await session.delete(db_obj)
        await session.commit()
        return db_obj
