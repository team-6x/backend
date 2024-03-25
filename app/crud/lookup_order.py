"""Pass."""

from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import LookupOrder, User


class CRUDLookupOrder:
    """Pass."""

    def __init__(self, model):
        """Initialize the CRUDBase object."""
        self.model = model

    async def create_lookup_order(
        self,
        obj_schema,
        session: AsyncSession,
        user: Optional[User],
    ):
        """Create a new object."""
        obj_data = obj_schema.model_dump()

        # obj_data["employer_id"] = user.id

        db_obj = self.model(**obj_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


crud_lookup_order = CRUDLookupOrder(LookupOrder)
