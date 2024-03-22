"""User Models."""

from typing import List

import phonenumbers
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import PhoneNumberType

from app.core.constants import Role
from app.core.db import Base, str_256


class User(SQLAlchemyBaseUserTable[int], Base):
    """Describe the model that stores the User."""

    __tablename__ = "user"

    name: Mapped[str_256]
    surname: Mapped[str_256]
    role: Mapped[Role]
    phone_number: Mapped[phonenumbers] = mapped_column(
        PhoneNumberType(),
        unique=True,
    )
    job_openings_employer: Mapped[List["JobOpening"]] = relationship(  # noqa
        back_populates="employer",
        lazy="selectin",
    )
    lookup_orders_employer: Mapped[List["LookupOrder"]] = relationship(  # noqa
        back_populates="employer",
        lazy="selectin",
    )
    lookup_orders_recruiters: Mapped[List["LookupOrder"]] = (  # noqa
        relationship(
            back_populates="recruiters",
            secondary="lookup_order_recruiter",
            lazy="selectin",
        )
    )
