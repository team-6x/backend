"""Contain a schmemas for JobOpening model."""

import uuid
from typing import Optional, Union

from pydantic import BaseModel, Field, field_validator, model_validator
from sqlalchemy_file import FileField

from app.core.constants import (
    EducationLevel,
    ExperienceDuration,
    WorkArrangements,
)
from app.core.db import str_256


class FileCreate(BaseModel):
    """Describe a model to create a file."""

    file: FileField


class NameCreate(BaseModel):
    """Describe a model to create a name field."""

    name: str_256


class DescriptionCreate(BaseModel):
    """Describe a model to create a description field."""

    description: str


class JobOpeningCreate(BaseModel):
    """Describe a model for jop_opening table."""

    name: str_256
    activity_field: str_256
    description: Optional[str]
    responsibilities: list[str]
    work_experience: ExperienceDuration
    education: EducationLevel
    job_types: list[DescriptionCreate]
    skills: Optional[list[NameCreate]]
    min_salary: int = Field(gt=0)
    max_salary: int = Field(gt=0)
    arrangement: WorkArrangements
    contracts: list[NameCreate]
    insurance: Optional[bool]
    bonuses: Optional[list[DescriptionCreate]]
    location: Optional[str_256]
    file: Optional[FileCreate]
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
            NameCreate,
        ],
    ):
        """Check if all requierd fields are not empty."""
        if value is None:
            raise ValueError("Это поле не может быть пустым!")
        return value
