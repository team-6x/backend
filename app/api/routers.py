"""API routers."""

from fastapi import APIRouter

from app.api.endpoints import user_router

main_router = APIRouter(prefix="/api/v1")
main_router.include_router(user_router)
