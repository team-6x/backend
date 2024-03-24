"""User Schemas."""

import uuid
from typing import Optional

from fastapi_users import schemas

from app.core.constants import Role


class UserRead(schemas.BaseUser[uuid.UUID]):
    """Describe the scheme for the User to read."""

    name: str
    surname: str
    role: Role
    phone_number: str


class UserCreate(schemas.BaseUserCreate):
    """Describe the scheme for creating a User."""

    name: str
    surname: str
    role: Role
    phone_number: str


class UserUpdate(schemas.BaseUserUpdate):
    """Describe the scheme for updating the User."""

    name: Optional[str]
    surname: Optional[str]
    phone_number: Optional[str]
