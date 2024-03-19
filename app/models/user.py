"""User Models."""

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped

from app.core.constants import Role
from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    """The model for the User."""

    role: Mapped[Role]
