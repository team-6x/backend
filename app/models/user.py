"""User Models."""

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from pydantic_extra_types.phone_numbers import PhoneNumber
from sqlalchemy.orm import Mapped, mapped_column

from app.core.constants import Role
from app.core.db import Base, str_256


class User(SQLAlchemyBaseUserTable[int], Base):
    """The model for the User."""

    __tablename__ = "user"

    name: Mapped[str_256]
    surname: Mapped[str_256]
    role: Mapped[Role]
    phone_number: Mapped[PhoneNumber] = mapped_column(
        unique=True,
    )
