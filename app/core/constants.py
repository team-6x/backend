"""Constants."""

import enum

LIMIT_CHAR_256 = 256


class Role(enum.Enum):
    """Describe the User role options."""

    EMPLOYER = "Работодатель"
    RECRUITER = "Рекрутер"
