"""User Schemas."""

from typing import Optional

from fastapi_users import schemas
from pydantic_extra_types.phone_numbers import PhoneNumber

from app.core.constants import Role


class UserRead(schemas.BaseUser[int]):
    """Describe the scheme for the User to read."""

    name: str
    surname: str
    role: Role
    phone_number: PhoneNumber


class UserCreate(schemas.BaseUserCreate):
    """Describe the scheme for creating a User."""

    name: str
    surname: str
    role: Role
    phone_number: PhoneNumber


class UserUpdate(schemas.BaseUserUpdate):
    """Describe the scheme for updating the User."""

    name: Optional[str]
    surname: Optional[str]
    phone_number: Optional[PhoneNumber]
