"""API routers."""

from fastapi import APIRouter

from app.api.endpoints import base_endpoints, lookup_order_router, user_router

main_router = APIRouter(prefix="/api/v1")
main_router.include_router(user_router)
main_router.include_router(lookup_order_router, tags=["lookup order"])
main_router.include_router(base_endpoints, tags=["base endpoints"])
