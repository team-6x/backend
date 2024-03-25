"""Base Endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.constants import (
    EducationLevel,
    ExperienceDuration,
    TariffOption,
    WorkArrangements,
)
from app.core.db import get_async_session
from app.crud.base import (
    crud_bonus,
    crud_contract,
    crud_job_type,
    crud_legal_form,
)
from app.schemas.base import DescriptionModelCreate, NameModelCreate

router = APIRouter()


@router.get("/work_experience")
async def get_work_experience():
    """Pass."""
    return {"Work experience": ExperienceDuration.get_list()}


@router.get("/education")
async def get_education_levels():
    """Pass."""
    return {"Education level": EducationLevel.get_list()}


@router.get("/work_arrangement")
async def get_work_arrangements():
    """Pass."""
    return {"Education level": WorkArrangements.get_list()}


@router.get("/tariff")
async def get_tariffs():
    """Pass."""
    return {"Education level": TariffOption.get_list()}


@router.get("/legal_form")
async def get_legal_forms(
    session: AsyncSession = Depends(get_async_session),
):
    """Pass."""
    objs = await crud_legal_form.get_all(session)
    return {"Legal form": [obj.name for obj in objs]}


@router.post("/legal_form")
async def add_legal_form(
    obj_in: NameModelCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Pass."""
    return {
        "Legal form": await crud_legal_form.create(
            obj_in,
            session,
        ),
    }


@router.get("/bonus")
async def get_bonuses(
    session: AsyncSession = Depends(get_async_session),
):
    """Pass."""
    objs = await crud_bonus.get_all(session)
    return {"Bonuses": [obj.description for obj in objs]}


@router.post("/bonus")
async def add_bonus(
    obj_in: DescriptionModelCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Pass."""
    return {
        "Bonus": await crud_bonus.create(
            obj_in,
            session,
        ),
    }


@router.get("/contract")
async def get_contracts(
    session: AsyncSession = Depends(get_async_session),
):
    """Pass."""
    objs = await crud_contract.get_all(session)
    return {"Contract": [obj.name for obj in objs]}


@router.post("/contract")
async def add_contract(
    obj_in: NameModelCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Pass."""
    return {
        "Contract": await crud_contract.create(
            obj_in,
            session,
        ),
    }


@router.get("/job_type")
async def get_job_type(
    session: AsyncSession = Depends(get_async_session),
):
    """Pass."""
    objs = await crud_job_type.get_all(session)
    return {"Job type": [obj.description for obj in objs]}


@router.post("/job_type")
async def add_job_type(
    obj_in: DescriptionModelCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Pass."""
    return {
        "Job type": await crud_job_type.create(
            obj_in,
            session,
        ),
    }
