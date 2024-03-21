"""User Models."""

from typing import List

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from pydantic_extra_types.phone_numbers import PhoneNumber
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.constants import Role
from app.core.db import Base, str_256
from app.models.job_opening import JobOpening

# from app.models.lookup_order import LookupOrder

LookupOrder = None


class User(SQLAlchemyBaseUserTable[int], Base):
    """Describe the model that stores the User."""

    __tablename__ = "user"

    name: Mapped[str_256]
    surname: Mapped[str_256]
    role: Mapped[Role]
    phone_number: Mapped[PhoneNumber] = mapped_column(
        unique=True,
    )
    job_openings_employer: Mapped[List["JobOpening"]] = relationship(
        back_populates="employer",
        lazy="selectin",
    )
    lookup_orders_employer: Mapped[List["LookupOrder"]] = relationship(
        back_populates="employer",
        lazy="selectin",
    )
    lookup_orders_recruiters: Mapped[List["LookupOrder"]] = relationship(
        back_populates="recruiters",
        secondary="lookup_order_recruiter",
        lazy="selectin",
    )
