"""Contain a JobOpening model for a project."""

from typing import List, Optional

from sqlalchemy import UUID, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_file import FileField

from app.core.constants import (
    ContractType,
    EducationLevel,
    EmploymentType,
    ExperienceDuration,
    WorkArrangements,
)
from app.core.db import Base, str_256


class JobOpening(Base):
    """
    Describe a model that makes a job opening for employer.
    """

    __tablename__ = "job_opening"

    employer_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    description: Mapped[Optional[str]]
    name: Mapped[str_256]
    acitivity_feild: Mapped[str]
    responsibilities: Mapped[list["ApplicantResponsibility"]] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    skills: Mapped[Optional[list["JobOpeningSkill"]]] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    work_experience: Mapped[ExperienceDuration]
    education: Mapped[EducationLevel]
    job_type: Mapped[EmploymentType]
    min_salary: Mapped[Optional[int]]
    max_salary: Mapped[Optional[int]]
    contract: Mapped[ContractType]
    insurance: Mapped[Optional[bool]]
    arrangement: Mapped[WorkArrangements]
    bonuses: Mapped[Optional[list["JobOpeningBonus"]]] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    location: Mapped[Optional[str]]
    stop_list: Mapped[Optional[list["StopList"]]] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    file: Mapped["JobOpeningFile"] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    additional_info: Mapped[Optional[str]]


class ApplicantResponsibility(Base):
    """Describe a model for responobility of applicant."""

    __tablename__ = "applicant_responsibility"

    job_opening_id: Mapped[UUID] = mapped_column(
        ForeignKey("job_opening.id", ondelete="CASCADE"),
        primary_key=True,
    )
    job_opening: Mapped["JobOpening"] = relationship(
        back_populates="responsibilities",
        lazy="selectin",
    )
    description: Mapped[str]


class StopList(Base):
    """Describe a model for stop list of applicant or a company."""

    __tablename__ = "stop_list"

    job_opening_id: Mapped[UUID] = mapped_column(
        ForeignKey("job_opening.id", ondelete="CASCADE"),
        primary_key=True,
    )
    job_opening: Mapped["JobOpening"] = relationship(
        back_populates="stop_list",
        lazy="selectin",
    )
    description: Mapped[str]


class JobOpeningFile(Base):
    """Model to attach a file for job_opening.file."""

    __tablename__ = "job_opening_file"

    job_opening_id: Mapped[UUID] = mapped_column(
        ForeignKey("job_opening.id", ondelete="CASCADE"),
        primary_key=True,
    )
    job_opening: Mapped["JobOpening"] = relationship(
        back_populates="file",
        lazy="selectin",
    )
    file: Column[FileField]


class JobOpeningBonus(Base):
    """Describe a model for bonus for applicant."""

    __tablename__ = "job_opening_bonus"

    job_opening_id: Mapped[UUID] = mapped_column(
        ForeignKey("job_opening.id", ondelete="CASCADE"),
        primary_key=True,
    )
    bonus_id: Mapped[UUID] = mapped_column(
        ForeignKey("bonus.id", ondelete="CASCADE"),
        primary_key=True,
    )


class Bonus(Base):
    """Describe a model for bonus of applicant."""

    __tablename__ = "applicant_bonus"

    job_opening_id: Mapped[UUID] = mapped_column(
        ForeignKey("job_opening.id", ondelete="CASCADE"),
        primary_key=True,
    )
    bonus: Mapped[List["JobOpening"]] = relationship(
        back_populates="bonuses",
        secondary="job_opening_bonus",
        lazy="selectin",
    )
    description: Mapped[str]


class JobOpeningSkill(Base):
    """Describe a model for skill of applicant."""

    __tablename__ = "job_opening_skill"

    job_opening_id: Mapped[UUID] = mapped_column(
        ForeignKey("job_opening.id", ondelete="CASCADE"),
        primary_key=True,
    )
    skill_id: Mapped[UUID] = mapped_column(
        ForeignKey("skill.id", ondelete="CASCADE"),
        primary_key=True,
    )


class Skill(Base):
    """Connects job_opening table with job_opening_skill."""

    __tablename__ = "applicant_skill"

    job_opening_id: Mapped[UUID] = mapped_column(
        ForeignKey("job_opening.id"),
    )
    skill: Mapped[List["JobOpening"]] = relationship(
        back_populates="skills",
        secondary="job_opening_skill",
        lazy="selectin",
    )
    name: Mapped[str]
