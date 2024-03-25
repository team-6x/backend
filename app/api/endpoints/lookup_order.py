"""LookUp Order Endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.lookup_order import LookupOrderCreate

router = APIRouter()


SessionLocal = sessionmaker(autocommit=False, autoflush=False)


@router.post("/", response_model=LookupOrderCreate)
async def create_lookup_order(
    lookup_order: LookupOrderCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Create Lookup Order model."""
    new_lookup_order = await CRUDBase.create(
        lookup_order,
        session,
        user,
    )
    return new_lookup_order
