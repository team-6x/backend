"""First

Revision ID: 77586a0ee7cb
Revises:
Create Date: 2024-03-22 10:11:04.117579

"""

from typing import Sequence, Union

import sqlalchemy_file
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "77586a0ee7cb"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    sa.Enum("EMPLOYER", "RECRUITER", name="role").create(op.get_bind())
    sa.Enum("INDIVIDUAL", "LEGAL_ENTITY", name="legalformoption").create(
        op.get_bind(),
    )
    sa.Enum(
        "NO_EXPERIENCE",
        "FROM_1_TO_3_YEARS",
        "FROM_3_TO_6_YEARS",
        "MORE_THAN_6_YEARS",
        name="experienceoption",
    ).create(op.get_bind())
    sa.Enum(
        "ALL_BEFORE",
        "HALF_BEFORE_HALF_AFTER",
        "ALL_AFTER",
        name="tariffoption",
    ).create(op.get_bind())
    sa.Enum("OFFICE", "REMOTE", "HYBRID", name="workarrangements").create(
        op.get_bind(),
    )
    sa.Enum(
        "MIDDLE",
        "SECONDARY",
        "INCOMPLETE_HIGHER",
        "HIGHER",
        "BACHELOR",
        "MASTER",
        "PHD_CANDIDATE",
        "PHD",
        name="educationlevel",
    ).create(op.get_bind())
    sa.Enum(
        "FROM_ONE_TO_THREE_YEARS",
        "FROM_THREE_TO_SIX_YEARS",
        "FIVE_OR_MORE",
        "DOESNT_MATTER",
        name="experienceduration",
    ).create(op.get_bind())
    op.create_table(
        "bonus",
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "contract",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "job_type",
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "legal_form",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "recruiter_responsibility",
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "skill",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("surname", sa.String(), nullable=False),
        sa.Column(
            "role",
            postgresql.ENUM(
                "EMPLOYER",
                "RECRUITER",
                name="role",
                create_type=False,
            ),
            nullable=False,
        ),
        sa.Column(
            "phone_number",
            sqlalchemy_utils.types.phone_number.PhoneNumberType(length=20),
            nullable=False,
        ),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("phone_number"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_table(
        "job_opening",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("activity_field", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column(
            "work_experience",
            postgresql.ENUM(
                "FROM_ONE_TO_THREE_YEARS",
                "FROM_THREE_TO_SIX_YEARS",
                "FIVE_OR_MORE",
                "DOESNT_MATTER",
                name="experienceduration",
                create_type=False,
            ),
            nullable=False,
        ),
        sa.Column(
            "education",
            postgresql.ENUM(
                "MIDDLE",
                "SECONDARY",
                "INCOMPLETE_HIGHER",
                "HIGHER",
                "BACHELOR",
                "MASTER",
                "PHD_CANDIDATE",
                "PHD",
                name="educationlevel",
                create_type=False,
            ),
            nullable=False,
        ),
        sa.Column("min_salary", sa.Integer(), nullable=True),
        sa.Column("max_salary", sa.Integer(), nullable=True),
        sa.Column(
            "arrangement",
            postgresql.ENUM(
                "OFFICE",
                "REMOTE",
                "HYBRID",
                name="workarrangements",
                create_type=False,
            ),
            nullable=False,
        ),
        sa.Column("insurance", sa.Boolean(), nullable=True),
        sa.Column("location", sa.String(), nullable=True),
        sa.Column("additional_info", sa.String(), nullable=True),
        sa.Column("employer_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["employer_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "applicant_responsibilities",
        sa.Column("job_opening_id", sa.Uuid(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["job_opening_id"],
            ["job_opening.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("job_opening_id", "id"),
    )
    op.create_table(
        "job_opening_bonus",
        sa.Column("job_opening_id", sa.Uuid(), nullable=False),
        sa.Column("bonus_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["bonus_id"],
            ["bonus.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["job_opening_id"],
            ["job_opening.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("job_opening_id", "bonus_id", "id"),
    )
    op.create_table(
        "job_opening_contract",
        sa.Column("job_opening_id", sa.Uuid(), nullable=False),
        sa.Column("contract_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["contract_id"],
            ["contract.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["job_opening_id"],
            ["job_opening.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("job_opening_id", "contract_id", "id"),
    )
    op.create_table(
        "job_opening_file",
        sa.Column("job_opening_id", sa.Uuid(), nullable=False),
        sa.Column("file", sqlalchemy_file.types.FileField(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["job_opening_id"],
            ["job_opening.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("job_opening_id", "id"),
    )
    op.create_table(
        "job_opening_job_type",
        sa.Column("job_opening_id", sa.Uuid(), nullable=False),
        sa.Column("job_type_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["job_opening_id"],
            ["job_opening.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["job_type_id"],
            ["job_type.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("job_opening_id", "job_type_id", "id"),
    )
    op.create_table(
        "job_opening_skill",
        sa.Column("job_opening_id", sa.Uuid(), nullable=False),
        sa.Column("skill_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["job_opening_id"],
            ["job_opening.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["skill_id"],
            ["skill.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("job_opening_id", "skill_id", "id"),
    )
    op.create_table(
        "lookup_order",
        sa.Column("employer_id", sa.Uuid(), nullable=False),
        sa.Column("job_opening_id", sa.Uuid(), nullable=False),
        sa.Column(
            "tariff",
            postgresql.ENUM(
                "ALL_BEFORE",
                "HALF_BEFORE_HALF_AFTER",
                "ALL_AFTER",
                name="tariffoption",
                create_type=False,
            ),
            nullable=False,
        ),
        sa.Column("bounty", sa.Integer(), nullable=False),
        sa.Column("urgency_bounty", sa.Integer(), nullable=True),
        sa.Column("awaited_employee_date", sa.DateTime(), nullable=False),
        sa.Column("first_cv_await_date", sa.DateTime(), nullable=True),
        sa.Column("recruiter_quantity", sa.Integer(), nullable=False),
        sa.Column(
            "recruiter_experience",
            postgresql.ENUM(
                "NO_EXPERIENCE",
                "FROM_1_TO_3_YEARS",
                "FROM_3_TO_6_YEARS",
                "MORE_THAN_6_YEARS",
                name="experienceoption",
                create_type=False,
            ),
            nullable=False,
        ),
        sa.Column(
            "legal_form",
            postgresql.ENUM(
                "INDIVIDUAL",
                "LEGAL_ENTITY",
                name="legalformoption",
                create_type=False,
            ),
            nullable=False,
        ),
        sa.Column("additional_info", sa.String(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.CheckConstraint("recruiter_quantity <= 3"),
        sa.CheckConstraint("recruiter_quantity >= 1"),
        sa.ForeignKeyConstraint(["employer_id"], ["user.id"]),
        sa.ForeignKeyConstraint(["job_opening_id"], ["job_opening.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "stop_list",
        sa.Column("job_opening_id", sa.Uuid(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["job_opening_id"],
            ["job_opening.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("job_opening_id", "id"),
    )
    op.create_table(
        "lookup_order_file",
        sa.Column("file", sqlalchemy_file.types.FileField(), nullable=True),
        sa.Column("lookup_order_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["lookup_order_id"],
            ["lookup_order.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "lookup_order_legal_form",
        sa.Column("lookup_order_id", sa.Uuid(), nullable=False),
        sa.Column("legal_form_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["legal_form_id"],
            ["legal_form.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["lookup_order_id"],
            ["lookup_order.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("lookup_order_id", "legal_form_id", "id"),
    )
    op.create_table(
        "lookup_order_recruiter",
        sa.Column("lookup_order_id", sa.Uuid(), nullable=False),
        sa.Column("recruiter_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["lookup_order_id"],
            ["lookup_order.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["recruiter_id"],
            ["user.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("lookup_order_id", "recruiter_id", "id"),
    )
    op.create_table(
        "lookup_order_recruiter_resp",
        sa.Column("lookup_order_id", sa.Uuid(), nullable=False),
        sa.Column("recruiter_resp_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["lookup_order_id"],
            ["lookup_order.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["recruiter_resp_id"],
            ["recruiter_responsibility.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("lookup_order_id", "recruiter_resp_id", "id"),
    )
    op.create_table(
        "recruiter_requirement",
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("lookup_order_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["lookup_order_id"],
            ["lookup_order.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("recruiter_requirement")
    op.drop_table("lookup_order_recruiter_resp")
    op.drop_table("lookup_order_recruiter")
    op.drop_table("lookup_order_legal_form")
    op.drop_table("lookup_order_file")
    op.drop_table("stop_list")
    op.drop_table("lookup_order")
    op.drop_table("job_opening_skill")
    op.drop_table("job_opening_job_type")
    op.drop_table("job_opening_file")
    op.drop_table("job_opening_contract")
    op.drop_table("job_opening_bonus")
    op.drop_table("applicant_responsibilities")
    op.drop_table("job_opening")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    op.drop_table("skill")
    op.drop_table("recruiter_responsibility")
    op.drop_table("legal_form")
    op.drop_table("job_type")
    op.drop_table("contract")
    op.drop_table("bonus")
    sa.Enum(
        "FROM_ONE_TO_THREE_YEARS",
        "FROM_THREE_TO_SIX_YEARS",
        "FIVE_OR_MORE",
        "DOESNT_MATTER",
        name="experienceduration",
    ).drop(op.get_bind())
    sa.Enum(
        "MIDDLE",
        "SECONDARY",
        "INCOMPLETE_HIGHER",
        "HIGHER",
        "BACHELOR",
        "MASTER",
        "PHD_CANDIDATE",
        "PHD",
        name="educationlevel",
    ).drop(op.get_bind())
    sa.Enum("OFFICE", "REMOTE", "HYBRID", name="workarrangements").drop(
        op.get_bind(),
    )
    sa.Enum(
        "ALL_BEFORE",
        "HALF_BEFORE_HALF_AFTER",
        "ALL_AFTER",
        name="tariffoption",
    ).drop(op.get_bind())
    sa.Enum(
        "NO_EXPERIENCE",
        "FROM_1_TO_3_YEARS",
        "FROM_3_TO_6_YEARS",
        "MORE_THAN_6_YEARS",
        name="experienceoption",
    ).drop(op.get_bind())
    sa.Enum("INDIVIDUAL", "LEGAL_ENTITY", name="legalformoption").drop(
        op.get_bind(),
    )
    sa.Enum("EMPLOYER", "RECRUITER", name="role").drop(op.get_bind())
    # ### end Alembic commands ###
