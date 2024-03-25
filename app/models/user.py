"""Contain a model for User."""

from typing import List

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.constants import Role
from app.core.db import Base, str_256


class User(SQLAlchemyBaseUserTableUUID, Base):
    """Describe the model that stores the User."""

    __tablename__ = "user"

    name: Mapped[str_256]
    surname: Mapped[str_256]
    role: Mapped[Role]
    phone_number: Mapped[str] = mapped_column(
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
