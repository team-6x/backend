"""Constants and enum classes for a project."""

from enum import Enum


class ExperienceDuration(str, Enum):
    """Enum class for work experience from employee."""

    NOT_REQUIRED = "Не требуется"
    FROM_ONE_TO_THREE_YEARS = "От 1 года до 3 лет"
    FROM_THREE_TO_SIX_YEARS = "От 3 до 5 лет"
    FIVE_OR_MORE = "Больше 5 лет"
    DOESNT_MATTER = "Не имеет значения"


class EducationLevel(str, Enum):
    """Enum class for education level from employee."""

    MIDDLE = "Среднее"
    SECONDARY = "Среднее специальное"
    INCOMPLETE_HIGHER = "Неоконченное высшее"
    HIGHER = "Высшее"
    BACHELOR = "Бакалавр"
    MASTER = "Магистр"
    PHD_CANDIDATE = "Кандидат наук"
    PHD = "Доктор наук"


class EmploymentType(str, Enum):
    """Enum class for employment status from employee."""

    FULL_TIME = "Полная"
    PART_TIME = "Частичная"
    PROJECT_BASED = "Проектная работа/разовое задание"
    VOLUNTEERING = "Волонтерство"
    INTERSHIP = "Стажировка"


class ContractType(str, Enum):
    """Enum class for contract type from employee."""

    LABOR_CODE_CONTRACT = "Оформление по ТК РФ"
    EMPLOYMENT_CONTRACT = "Трудовой договор"
    CIVIL_CONTRACT = "ГПХ"
    ENTREPRENEUR = "ИП"
    SELF_EMPLOYMENT = "Самозанятость"


class WorkArrangements(str, Enum):
    """Enum class for work format from employee."""

    OFFICE = "Офис"
    REMOTE = "Удаленная работа"
    HYBRID = "Гибрид"
