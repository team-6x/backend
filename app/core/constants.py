"""Constants."""

import enum

LIMIT_CHAR_256 = 256


class Role(enum.Enum):
    """Roles for User."""

    employer = "Работодатель"
    recruiter = "Рекрутер"
