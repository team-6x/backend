"""Constants and enum classes for a project."""

import enum

LIMIT_CHAR_256 = 256
MINIMAL_EMPLOYEE_AWAITING_TIME_DAYS = 7
MINIMUM_BOUNTY = 0
MINIMUM_URGENCY_BOUNTY = 0
MAXIMUM_RECRUITER_QUANTITY = 3
MINIMUM_RECRUITER_QUANTITY = 1
MINIMUM_SALARY = 0


class ExtendedEnum(enum.Enum):
    """Extend Enum class."""

    @classmethod
    def get_list(cls):
        """Return a list of Enum's entities."""
        return [value for value in cls]


class ExperienceDuration(str, ExtendedEnum):
    """Enum class for work experience from employee."""

    FROM_ONE_TO_THREE_YEARS = "От 1 года до 3 лет"
    FROM_THREE_TO_SIX_YEARS = "От 3 до 5 лет"
    FIVE_OR_MORE = "Больше 5 лет"
    DOESNT_MATTER = "Не имеет значения"


class EducationLevel(str, ExtendedEnum):
    """Enum class for education level from employee."""

    MIDDLE = "Среднее"
    SECONDARY = "Среднее специальное"
    INCOMPLETE_HIGHER = "Неоконченное высшее"
    HIGHER = "Высшее"
    BACHELOR = "Бакалавр"
    MASTER = "Магистр"
    PHD_CANDIDATE = "Кандидат наук"
    PHD = "Доктор наук"


class WorkArrangements(str, ExtendedEnum):
    """Enum class for work format from employee."""

    OFFICE = "Офис"
    REMOTE = "Удаленная работа"
    HYBRID = "Гибрид"


class Role(str, enum.Enum):
    """Describe the User role options."""

    EMPLOYER = "Работодатель"
    RECRUITER = "Рекрутер"


class TariffOption(str, enum.Enum):
    """Describe a payment tariff options."""

    ALL_BEFORE = "100% до выхода"
    HALF_BEFORE_HALF_AFTER = "50% до выхода 50% после гарантийного срока"
    ALL_AFTER = "100% после гарантийного срока"
