"""Contains basic CRUD operations."""

import uuid
from typing import Optional, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base
from app.models import (
    Bonus,
    Contract,
    JobType,
    LegalForm,
    RecruiterRequirement,
    RecruiterResponsibility,
    Skill,
)
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
        db_objs = await session.execute(
            select(self.model),
        )
        return db_objs.scalars().all()

    async def create(
        self,
        obj_schema,
        session: AsyncSession,
        user: Optional[User] = None,
    ):
        """Create a new object."""
        obj_data = obj_schema.model_dump()
        if user:
            obj_data["employer_id"] = user.id
        db_obj = self.model(**obj_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


class CRUDDescriptionModel(CRUDBase):
    """CRUD for model with a description field."""

    async def get_by_description(
        self,
        session: AsyncSession,
        description: str,
    ):
        """Get an object of this type."""
        db_obj = await session.execute(
            select(self.model).where(
                self.model.description == description,
            ),
        )
        return db_obj.scalars().first()


class CRUDNameModel(CRUDBase):
    """CRUD for model with a name field."""

    async def get_by_name(
        self,
        session: AsyncSession,
        name: str,
    ):
        """Get an object of this type."""
        db_obj = await session.execute(
            select(self.model).where(
                self.model.name == name,
            ),
        )
        return db_obj.scalars().first()


crud_recruiter_requirements = CRUDBase(RecruiterRequirement)

crud_job_type = CRUDDescriptionModel(JobType)
crud_bonus = CRUDDescriptionModel(Bonus)

crud_skill = CRUDNameModel(Skill)
crud_contract = CRUDNameModel(Contract)
crud_legal_form = CRUDNameModel(LegalForm)
crud_recruiter_responsibility = CRUDDescriptionModel(RecruiterResponsibility)
