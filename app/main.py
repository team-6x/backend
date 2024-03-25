"""Entrypoint for fastapi app."""

from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings
from app.core.init_db import create_first_superuser

app = FastAPI(
    title=settings.app_title,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

app.include_router(main_router)


@app.on_event("startup")
async def startup():
    """Automatic creation of a superuser."""
    await create_first_superuser()
