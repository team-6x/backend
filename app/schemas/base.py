"""Contain secondary models for job_opening and lookup_order models."""

from pydantic import BaseModel
from sqlalchemy_file import FileField

from app.core.db import str_256


class FileModelCreate(BaseModel):
    """Model with a file field."""

    file: FileField


class DescriptionModelCreate(BaseModel):
    """Model with a description field."""

    description: str


class NameModelCreate(BaseModel):
    """Model with a name field."""

    name: str_256
