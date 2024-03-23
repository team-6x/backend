"""Contain a schmemas for JobOpening model."""

import uuid
from typing import Optional, Union

from pydantic import BaseModel, Field, field_validator, model_validator

from app.core.constants import (
    MINIMUM_SALARY,
    EducationLevel,
    ExperienceDuration,
    WorkArrangements,
)
from app.core.db import str_256
from app.schemas.base import (
    DescriptionModelCreate,
    FileModelCreate,
    NameModelCreate,
)


class JobOpeningCreate(BaseModel):
    """Describe a model for jop_opening table."""

    name: str_256
    activity_field: str_256
    description: Optional[str] = None
    responsibilities: list[str]
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
    file: Optional[FileModelCreate] = None
    additional_info: Optional[str]
    employer_id: uuid.UUID

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


class JobOpeningUpdate(JobOpeningCreate):  # сделал на будущее на всякий
    """Describe an model to update a jop_opening table."""  # если что уберем

    @field_validator(
        "name",
        "activity_field",
        "responsibilities",
        "work_experience",
        "education",
        "job_types",
        "min_salary",
        "max_salary",
        "arrangement",
        "contracts",
    )
    @classmethod
    def field_cannot_be_null(
        cls,
        value: Union[
            str,
            int,
            list[str],
            WorkArrangements,
            ExperienceDuration,
            EducationLevel,
            NameModelCreate,
        ],
    ) -> Union[
        str,
        int,
        list[str],
        WorkArrangements,
        ExperienceDuration,
        EducationLevel,
        NameModelCreate,
    ]:
        """Check if all requierd fields are not empty."""
        if value is None:
            raise ValueError("Это поле не может быть пустым!")
        return value
