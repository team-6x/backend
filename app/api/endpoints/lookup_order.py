"""LookUp Order Endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.lookup_order import crud_lookup_order
from app.models.user import User
from app.schemas.lookup_order import LookupOrderCreate

router = APIRouter()


@router.post("/", response_model=LookupOrderCreate)
async def create_lookup_order(
    lookup_order: LookupOrderCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Pass."""
    return await crud_lookup_order.create_lookup_order(
        lookup_order,
        session,
        user,
    )
