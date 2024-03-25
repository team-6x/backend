"""Define schemas for lookup order model processing."""

import datetime as dt
from typing import Optional

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)

from app.core.constants import (
    MAXIMUM_RECRUITER_QUANTITY,
    MINIMAL_EMPLOYEE_AWAITING_TIME_DAYS,
    MINIMUM_BOUNTY,
    MINIMUM_RECRUITER_QUANTITY,
    MINIMUM_URGENCY_BOUNTY,
    ExperienceDuration,
    TariffOption,
)
from app.schemas.base import DescriptionModelCreate, NameModelCreate
from app.schemas.job_opening import JobOpeningCreate


class LookupOrderCreate(BaseModel):
    """Model for lookup_order table."""

    model_config = ConfigDict(from_attributes=True)

    job_opening: JobOpeningCreate
    tariff: TariffOption
    bounty: int = Field(gt=MINIMUM_BOUNTY)
    urgency_bounty: int = Field(
        default=MINIMUM_URGENCY_BOUNTY,
        ge=MINIMUM_URGENCY_BOUNTY,
    )
    awaited_employee_date: dt.date
    first_cv_await_date: Optional[dt.date] = None
    recruiter_quantity: int = Field(
        ge=MINIMUM_RECRUITER_QUANTITY,
        le=MAXIMUM_RECRUITER_QUANTITY,
    )
    recruiter_experience: ExperienceDuration = ExperienceDuration.DOESNT_MATTER
    legal_form: list[NameModelCreate]
    additional_info: Optional[str] = None
    responsibilities: Optional[list[DescriptionModelCreate]] = None
    # file: Optional[FileModelCreate] = None
    recruiter_requirements: Optional[list[DescriptionModelCreate]] = None

    @field_validator("awaited_employee_date")
    @classmethod
    def check_if_awaited_employee_date_later_than_minimal(
        cls,
        value: dt.datetime,
    ) -> dt.datetime:
        """
        Check awaited_employee_date.

        If it is supposed to be later than minimal allowed.
        """
        date_with_delta = dt.date.today() + dt.timedelta(
            days=MINIMAL_EMPLOYEE_AWAITING_TIME_DAYS,
        )
        if value < date_with_delta:
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
