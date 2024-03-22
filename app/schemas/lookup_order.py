"""Define schemas for lookup order model processing."""

import uuid
from datetime import datetime, timedelta
from typing import Optional

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)
from sqlalchemy_file import FileField

from app.core.constants import (
    MAXIMUM_RECRUITER_QUANTITY,
    MINIMAL_EMPLOYEE_AWAITING_TIME_DAYS,
    ExperienceDuration,
    LegalFormOption,
    TariffOption,
)
from app.core.db import str_256


class FileModelCreate(BaseModel):
    """Model with a file field."""

    file: FileField


class DescriptionModelCreate(BaseModel):
    """Model with a description field."""

    description: str


class NameModelCreate(BaseModel):
    """Model with a name field."""

    name: str_256


class LookupOrderCreate(BaseModel):
    """Model for lookup_order table."""

    model_config = ConfigDict(from_attributes=True)

    employer_id: uuid.UUID
    job_opening_id: uuid.UUID
    tariff: TariffOption
    bounty: int = Field(gt=0)
    urgency_bounty: int = Field(default=0, ge=0)
    awaited_employee_date: datetime
    first_cv_await_date: Optional[datetime] = None
    recruiter_quantity: int = Field(ge=1, le=MAXIMUM_RECRUITER_QUANTITY)
    recruiter_experience: ExperienceDuration = ExperienceDuration.DOESNT_MATTER
    legal_form: LegalFormOption
    additional_info: Optional[str] = None
    responsibilities: Optional[list[DescriptionModelCreate]] = None
    file: Optional[FileModelCreate] = None
    recruiter_requirements: Optional[list[DescriptionModelCreate]] = None

    @field_validator("awaited_employee_date")
    @classmethod
    def check_if_awaited_employee_date_later_than_minimal(
        cls,
        value: datetime,
    ) -> datetime:
        """
        Check awaited_employee_date.

        If it is supposed to be later than minimal allowed.
        """
        if value < datetime.now() + timedelta(
            days=MINIMAL_EMPLOYEE_AWAITING_TIME_DAYS,
        ):
            raise ValueError(
                "Дата ожидания близжайших анкет раньше допустимого",
            )
        return value

    @model_validator(mode="after")
    def check_first_cv_await_date_gt_awaited_employee_date(
        self,
    ) -> "LookupOrderCreate":
        """Check if first_cv_await_date later than awaited_employee_date."""
        if (
            self.first_cv_await_date
            and self.first_cv_await_date > self.awaited_employee_date
        ):
            raise ValueError(
                "Дата ожидания первых резюме должна быть раньше "
                "чем дата ожидания первого работника",
            )
        return self
