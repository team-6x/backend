"""Contain a JobOpening model for a project."""

from typing import List, Optional

from sqlalchemy import UUID, Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_file import FileField

from app.core.constants import (
    ContractType,
    EducationLevel,
    EmploymentType,
    ExperienceDuration,
    WorkArrangements,
)
from app.core.db import Base


class JobOpening(Base):
    """
    Describe a model that makes a job opening for employer.
    """

    __tablename__ = "job_opening"

    employer_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    description: Mapped[Optional[str]]
    name: Mapped[str]
    acitivity_feild: Mapped[str]
    responsibilities: Mapped[list["ApplicantResponsibility"]] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    skills: Mapped[Optional[list["Skill"]]] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    work_experience: Mapped[ExperienceDuration]
    education: Mapped[EducationLevel]
    job_type: Mapped[EmploymentType]
    min_salary: Mapped[int] = mapped_column(Integer(100))
    max_salary: Mapped[int] = mapped_column(Integer(1000000))
    contract: Mapped[ContractType]
    insurance: Mapped[Optional[bool]] = mapped_column(default=True)
    arrangement: Mapped[WorkArrangements]
    bonuses: Mapped[Optional[list["Bonus"]]] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    location: Mapped[Optional[str]] = mapped_column(default=None)
    stop_list: Mapped[Optional[list["StopList"]]] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    file: Mapped["JobOpeningFile"] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    additional_info: Mapped[Optional[str]] = mapped_column(default=None)


class JobOpeningId(Base):
    """Decribe a base model for extra fields of JobOpening."""

    job_opening_id: Mapped[UUID] = mapped_column(
        ForeignKey("job_opening.id", ondelete="CASCADE"),
        primary_key=True,
    )


class ApplicantResponsibility(JobOpeningId):
    """Dectribe a model for responobility of applicant."""

    __tablename__ = "applicant_responsibility"

    job_opening: Mapped["JobOpening"] = relationship(
        back_populates="responsibilities",
        lazy="selectin",
    )
    description: Mapped[str]


class Bonus(JobOpeningId):
    """Dectribe a model for bonus of applicant."""

    __tablename__ = "applicant_bonuses"

    job_opening: Mapped["JobOpening"] = relationship(
        back_populates="bonuses",
        lazy="selectin",
    )
    description: Mapped[str]


class StopList(JobOpeningId):
    """Dectribe a model for stop list of applicant or a company."""

    __tablename__ = "stop_list"

    job_opening: Mapped["JobOpening"] = relationship(
        back_populates="stop_list",
        lazy="selectin",
    )
    description: Mapped[str]


class JobOpeningFile(JobOpeningId):
    """Model to attach a file for job_opening.file."""

    __tablename__ = "job_opening_file"

    job_opening: Mapped["JobOpening"] = relationship(
        back_populates="file",
        lazy="selectin",
    )
    file: Column[Optional[FileField]]


class JobOpeningSkill(JobOpeningId):
    """Dectribe a model for skill of applicant."""

    __tablename__ = "job_opening_skill"

    skill_id: Mapped[UUID] = mapped_column(
        ForeignKey("skill.id", ondelete="CASCADE"),
        primary_key=True,
    )


class Skill(Base):
    """Connects job_opening table with job_opening_skill."""

    __tablename__ = "skill"

    job_opening_id: Mapped[UUID] = mapped_column(
        ForeignKey("job_opening.id"),
    )
    skill: Mapped[List["JobOpening"]] = relationship(
        back_populates="skills",
        secondary="job_opening_skill",
        lazy="selectin",
    )
    name: Mapped[Optional[str]]
