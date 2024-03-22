"""Constants and enum classes for a project."""

import enum

LIMIT_CHAR_256 = 256
MINIMAL_EMPLOYEE_AWAITING_TIME_DAYS = 7
MAXIMUM_RECRUITER_QUANTITY = 3


class ExperienceDuration(str, enum.Enum):
    """Enum class for work experience from employee."""

    FROM_ONE_TO_THREE_YEARS = "От 1 года до 3 лет"
    FROM_THREE_TO_SIX_YEARS = "От 3 до 5 лет"
    FIVE_OR_MORE = "Больше 5 лет"
    DOESNT_MATTER = "Не имеет значения"


class EducationLevel(str, enum.Enum):
    """Enum class for education level from employee."""

    MIDDLE = "Среднее"
    SECONDARY = "Среднее специальное"
    INCOMPLETE_HIGHER = "Неоконченное высшее"
    HIGHER = "Высшее"
    BACHELOR = "Бакалавр"
    MASTER = "Магистр"
    PHD_CANDIDATE = "Кандидат наук"
    PHD = "Доктор наук"


class WorkArrangements(str, enum.Enum):
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


class LegalFormOption(str, enum.Enum):
    """Describe a legal form of collaboration options."""

    INDIVIDUAL = "Физическое лицо"
    LEGAL_ENTITY = (
        "Юридическое лицо, Индивидуальный предприниматель, Cамозанятый"
    )
