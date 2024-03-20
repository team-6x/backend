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


class TariffOption(enum.Enum):
    """Describe a payment tariff options."""

    all_before = "100% до выхода"
    half_before_half_after = "50% до выхода 50% после гарантийного срока"
    all_after = "100% после гарантийного срока"


class LegalFormOption(enum.Enum):
    """Describe a legal form of collaboration options."""

    individual = "Физическое лицо"
    legal_entity = (
        "Юридическое лицо, " "Индивидуальный предприниматель, " "Cамозанятый"
    )


class ExperienceOption(enum.Enum):
    """Describe a lifespan experience."""

    no_experience = "Нет опыта"
    from_1_to_3_years = "От 1 до 3 лет"
    from_3_to_6_years = "От 3 до 6 лет"
    more_than_6_years = "6+ лет"
