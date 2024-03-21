"""Constants and enum classes for a project."""

import enum

LIMIT_CHAR_256 = 256


class ExperienceDuration(enum.Enum):
    """Enum class for work experience from employee."""

    FROM_ONE_TO_THREE_YEARS = "От 1 года до 3 лет"
    FROM_THREE_TO_SIX_YEARS = "От 3 до 5 лет"
    FIVE_OR_MORE = "Больше 5 лет"
    DOESNT_MATTER = "Не имеет значения"


class EducationLevel(enum.Enum):
    """Enum class for education level from employee."""

    MIDDLE = "Среднее"
    SECONDARY = "Среднее специальное"
    INCOMPLETE_HIGHER = "Неоконченное высшее"
    HIGHER = "Высшее"
    BACHELOR = "Бакалавр"
    MASTER = "Магистр"
    PHD_CANDIDATE = "Кандидат наук"
    PHD = "Доктор наук"


class WorkArrangements(enum.Enum):
    """Enum class for work format from employee."""

    OFFICE = "Офис"
    REMOTE = "Удаленная работа"
    HYBRID = "Гибрид"


class Role(enum.Enum):
    """Describe the User role options."""

    EMPLOYER = "Работодатель"
    RECRUITER = "Рекрутер"
