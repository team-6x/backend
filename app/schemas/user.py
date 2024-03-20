"""User Schemas."""

from typing import Optional

from fastapi_users import schemas
from pydantic_extra_types.phone_numbers import PhoneNumber

from app.core.constants import Role


class UserRead(schemas.BaseUser[int]):
    """The reading scheme for the User."""

    name: str
    surname: str
    role: Role
    phone_number: PhoneNumber


class UserCreate(schemas.BaseUserCreate):
    """The creation scheme for the User."""

    name: str
    surname: str
    role: Role
    phone_number: PhoneNumber


class UserUpdate(schemas.BaseUserUpdate):
    """The update scheme for the User."""

    name: Optional[str]
    surname: Optional[str]
    phone_number: Optional[PhoneNumber]
