"""
Contain a model for lookup order.

So as dependent models:
- LookupOrder: for a lookup order
- LookupOrderRecruiter: connects a lookup order with a user (recruiter)
- LookupOrderFile: for a file attached to a lookup order
- RecruiterRequirement: contains requirements for a recruiter
- RecruiterResp: contains recruiter's responsibilities
- LookupOrderRecruiterResp: connects a lookup_order
    with recruiter responsibilities
"""

from datetime import datetime
from typing import List, Optional

from sqlalchemy import UUID, CheckConstraint, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_file import FileField

from app.core.constants import ExperienceOption, LegalFormOption, TariffOption
from app.core.db import Base

User = None  # delete after definition
JobOpening = None  # delete after definition


class LookupOrder(Base):
    """Describe a model that stores a lookup order."""

    __tablename__ = "lookup_order"

    employer_id: Mapped[UUID]  # foreign key to user
    job_opening_id: Mapped[UUID]  # foreign key to job_opening
    tariff: Mapped[TariffOption]
    bounty: Mapped[int]
    urgency_bounty: Mapped[Optional[int]] = mapped_column(default=None)
    awaited_employee_date: Mapped[datetime]  # set default on crud level
    first_cv_await_date: Mapped[Optional[datetime]] = mapped_column(
        default=None,
    )
    recruiter_quantity: Mapped[int] = mapped_column(default=1)
    recruiter_experience: Mapped[ExperienceOption]
    legal_form: Mapped[LegalFormOption]
    additional_info: Mapped[str]
    is_require_security_check: Mapped[bool]

    __table_args__ = (
        CheckConstraint("recruiter_quantity >= 1"),
        CheckConstraint("recruiter_quantity <= 3"),
    )

    employer: Mapped["User"] = relationship(
        back_populates="lookup_orders",
        lazy="selectin",
    )
    responsibilities: Mapped[List["RecruiterResp"]] = relationship(
        back_populates="lookup_order",
        secondary="lookup_order_recruiter_resp",
        lazy="selectin",
    )
    file: Mapped["LookupOrderFile"] = relationship(
        back_populates="lookup_order",
        lazy="selectin",
    )
    recruiter_requirements: Mapped[List["RecruiterRequirement"]] = (
        relationship(
            back_populates="recruiter_requirement",
            lazy="selectin",
        )
    )
    recruiters: Mapped[List["User"]] = relationship(
        back_populates="lookup_orders",
        secondary="lookup_order_recruiter",
        lazy="selectin",
    )
    job_opening: Mapped["JobOpening"] = relationship(
        back_populates="lookup_order",
        lazy="selectin",
    )


class LookupOrderRecruiter(Base):
    """
    Describe a secondary model.

    Connects lookup_order table with user (recruiter) model.
    """

    __tablename__ = "lookup_order_recruiter"

    lookup_order_id: Mapped[UUID] = mapped_column(
        ForeignKey("lookup_order.id", ondelete="CASCADE"),
        primary_key=True,
    )
    recruiter_resp_id: Mapped[UUID] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        primary_key=True,
    )


class LookupOrderFile(Base):
    """
    Describe a model for a file.

    Attached to lookup_order model.
    """

    __tablename__ = "lookup_order_file"

    file = Column(FileField)

    lookup_order_id: Mapped[UUID] = mapped_column(
        ForeignKey("lookup_order.id"),
    )
    lookup_order: Mapped["LookupOrder"] = relationship(
        back_populates="file",
        lazy="selectin",
    )


class RecruiterRequirement(Base):
    """Describe a recruiter requirements model."""

    __tablename__ = "recruiter_requirement"

    description: Mapped[str]

    lookup_order_id: Mapped[UUID] = mapped_column(
        ForeignKey("lookup_order.id"),
    )
    lookup_order: Mapped["LookupOrder"] = relationship(
        back_populates="recruiter_requirements",
        lazy="selectin",
    )


class RecruiterResp(Base):
    """Describe a recruiter responsibilities model."""

    __tablename__ = "recruiter_resp"

    description: Mapped[str]

    responsibilities: Mapped[List["LookupOrder"]] = relationship(
        back_populates="responsibilities",
        secondary="lookup_order_recruiter_resp",
        lazy="selectin",
    )


class LookupOrderRecruiterResp(Base):
    """
    Describe a secondary model.

    Connects lookup_order table with recruiter_resp.
    """

    __tablename__ = "lookup_order_recruiter_resp"

    lookup_order_id: Mapped[UUID] = mapped_column(
        ForeignKey("lookup_order.id", ondelete="CASCADE"),
        primary_key=True,
    )
    recruiter_resp_id: Mapped[UUID] = mapped_column(
        ForeignKey("recruiter_resp.id", ondelete="CASCADE"),
        primary_key=True,
    )
