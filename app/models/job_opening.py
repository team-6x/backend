"""Contain a JobOpening model for a project."""

import uuid
from typing import List, Optional

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_file import FileField

from app.core.constants import (
    EducationLevel,
    ExperienceDuration,
    WorkArrangements,
)
from app.core.db import Base, str_256
from app.models.user import User


class JobOpening(Base):
    """Describe a model that makes a job opening for employer."""

    __tablename__ = "job_opening"

    name: Mapped[str_256]
    activity_field: Mapped[str_256]
    description: Mapped[Optional[str]]
    responsibilities: Mapped[list["ApplicantResponsibility"]] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    work_experience: Mapped[ExperienceDuration]
    education: Mapped[EducationLevel]
    job_types: Mapped[Optional[list["JobType"]]] = relationship(
        back_populates="job_openings",
        secondary="job_opening_job_type",
        lazy="selectin",
    )
    skills: Mapped[Optional[list["Skill"]]] = relationship(
        back_populates="job_openings",
        secondary="job_opening_skill",
        lazy="selectin",
    )
    min_salary: Mapped[Optional[int]]
    max_salary: Mapped[Optional[int]]
    arrangement: Mapped[WorkArrangements]
    contracts: Mapped[Optional[list["Contract"]]] = relationship(
        back_populates="job_openings",
        secondary="job_opening_contract",
        lazy="selectin",
    )
    insurance: Mapped[Optional[bool]]
    bonuses: Mapped[Optional[list["Bonus"]]] = relationship(
        back_populates="job_openings",
        secondary="job_opening_bonus",
        lazy="selectin",
    )
    location: Mapped[Optional[str_256]]
    stop_list: Mapped[Optional[list["StopList"]]] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    file: Mapped["JobOpeningFile"] = relationship(
        back_populates="job_opening",
        lazy="selectin",
    )
    additional_info: Mapped[Optional[str]]
    employer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"))
    employer: Mapped["User"] = relationship(
        back_populates="job_openings_employer",
        lazy="selectin",
    )


class ApplicantResponsibility(Base):
    """Describe a model for responobility of applicant."""

    __tablename__ = "applicant_responsibilities"

    job_opening_id: Mapped[uuid.UUID] = mapped_column(
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

    job_opening_id: Mapped[uuid.UUID] = mapped_column(
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

    job_opening_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("job_opening.id", ondelete="CASCADE"),
        primary_key=True,
    )
    job_opening: Mapped["JobOpening"] = relationship(
        back_populates="file",
        lazy="selectin",
    )
    file = Column(FileField)


class JobOpeningBonus(Base):
    """
    Describe a secondary model.

    Connects applicant_bonus with job_opening.bonuses.
    """

    __tablename__ = "job_opening_bonus"

    job_opening_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("job_opening.id", ondelete="CASCADE"),
        primary_key=True,
    )
    bonus_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("bonus.id", ondelete="CASCADE"),
        primary_key=True,
    )


class Bonus(Base):
    """Describe a model for bonus of applicant."""

    __tablename__ = "bonus"

    job_openings: Mapped[List["JobOpening"]] = relationship(
        back_populates="bonuses",
        secondary="job_opening_bonus",
        lazy="selectin",
    )
    description: Mapped[str]


class JobOpeningContract(Base):
    """
    Describe a secondary model.

    Connects applicant_contract with job_opening.contracts.
    """

    __tablename__ = "job_opening_contract"

    job_opening_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("job_opening.id", ondelete="CASCADE"),
        primary_key=True,
    )
    contract_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("contract.id", ondelete="CASCADE"),
        primary_key=True,
    )


class Contract(Base):
    """Describe a model for bonus of applicant."""

    __tablename__ = "contract"

    job_openings: Mapped[List["JobOpening"]] = relationship(
        back_populates="contracts",
        secondary="job_opening_contract",
        lazy="selectin",
    )
    name: Mapped[str_256]


class JobOpeningJobType(Base):
    """
    Describe a secondary model.

    Connects applicant_job_type with job_opening.job_types.
    """

    __tablename__ = "job_opening_job_type"

    job_opening_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("job_opening.id", ondelete="CASCADE"),
        primary_key=True,
    )
    job_type_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("job_type.id", ondelete="CASCADE"),
        primary_key=True,
    )


class JobType(Base):
    """Describe a model for job type for applicant."""

    __tablename__ = "job_type"

    job_openings: Mapped[List["JobOpening"]] = relationship(
        back_populates="job_types",
        secondary="job_opening_job_type",
        lazy="selectin",
    )
    description: Mapped[str]


class JobOpeningSkill(Base):
    """
    Describe a secondary model.

    Connects applicant_skill with job_opening.skills.
    """

    __tablename__ = "job_opening_skill"

    job_opening_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("job_opening.id", ondelete="CASCADE"),
        primary_key=True,
    )
    skill_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("skill.id", ondelete="CASCADE"),
        primary_key=True,
    )


class Skill(Base):
    """Describe a model for skill of applicant."""

    __tablename__ = "skill"

    job_openings: Mapped[List["JobOpening"]] = relationship(
        back_populates="skills",
        secondary="job_opening_skill",
        lazy="selectin",
    )
    name: Mapped[str]
