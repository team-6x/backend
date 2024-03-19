"""User Schemas."""

from fastapi_users import schemas

from app.models.user import Role


class UserRead(schemas.BaseUser[int]):
    """The reading scheme for the User."""

    role: Role


class UserCreate(schemas.BaseUserCreate):
    """The creation scheme for the User."""

    role: Role


class UserUpdate(schemas.BaseUserUpdate):
    """The update scheme for the User."""

    pass
