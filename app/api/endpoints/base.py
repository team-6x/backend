"""Base Endpoints."""

from fastapi import APIRouter

from app.core.constants import EducationLevel, ExperienceDuration

router = APIRouter()


@router.get("/work_experience")
async def get_work_experience():
    """Pass."""
    return {"Work Experience": ExperienceDuration.get_list()}


@router.get("/education")
async def get_education_level():
    """Pass."""
    return {"Education Level": EducationLevel.get_list()}
