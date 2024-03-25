"""Contain a schmemas for JobOpening model."""

from typing import Optional

from pydantic import BaseModel, Field, model_validator

from app.core.constants import (
    MINIMUM_SALARY,
    EducationLevel,
    ExperienceDuration,
    WorkArrangements,
)
from app.core.db import str_256
from app.schemas.base import DescriptionModelCreate, NameModelCreate


class JobOpeningCreate(BaseModel):
    """Describe a model for jop_opening table."""

    name: str_256
    activity_field: str_256
    description: Optional[str] = None
    responsibilities: list[DescriptionModelCreate]
    work_experience: ExperienceDuration
    education: EducationLevel
    job_types: list[DescriptionModelCreate]
    skills: Optional[list[NameModelCreate]] = None
    min_salary: int = Field(gt=MINIMUM_SALARY)
    max_salary: int = Field(gt=MINIMUM_SALARY)
    arrangement: WorkArrangements
    contracts: list[NameModelCreate]
    insurance: Optional[bool] = None
    bonuses: Optional[list[DescriptionModelCreate]] = None
    location: Optional[str_256] = None
    # file: Optional[FileModelCreate] = None
    additional_info: Optional[str]
    stop_list: Optional[list[DescriptionModelCreate]]

    @model_validator(mode="after")
    def check_salary(self) -> "JobOpeningCreate":
        """Check if max_salary field is grater or equal then min_salary."""
        min = self.min_salary
        max = self.max_salary
        if max is not None and max < min:
            raise ValueError(
                "Максимальная заработная плата должна быть \n"
                "больше или равна минимальной заработной плате",
            )
        return self
