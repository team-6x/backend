"""Base Endpoints."""

from fastapi import APIRouter

from app.core.constants import (
    EducationLevel,
    ExperienceDuration,
    WorkArrangements,
)
from app.models.job_opening import JobOpening

router = APIRouter()


@router.get("/work_experience")
async def get_work_experience():
    """Return ENUM from ExperienceDuration model."""
    return {"Work Experience": ExperienceDuration.get_list()}


@router.get("/recruiter_experience")
async def get_recruiter_experience():
    """Return ENUM from ExperienceDuration model."""
    return {"Recruiter Experience": ExperienceDuration.get_list()}


@router.get("/education")
async def get_education_level():
    """Return ENUM from EducationLevel model."""
    return {"Education Levels": EducationLevel.get_list()}


@router.get("/arrangement")
async def get_arrangement():
    """Return ENUM from WorkArrangements model."""
    return {"Work Arrangements": WorkArrangements.get_list()}


@router.get("/job_types")  # need fix
async def get_job_types():
    """Pass."""
    return {"Job Types": JobOpening()}


@router.get("/contracts")  # need fix
async def get_contracts():
    """Pass."""
    return {"Contracts": JobOpening()}


@router.get("/bonuses")  # need fix
async def get_bonuses():
    """Pass."""
    return {"Bonuses": JobOpening()}


@router.get("/test_item")  # need fix
async def get_test_item():
    """Pass."""
    return {"Test item": JobOpening()}
