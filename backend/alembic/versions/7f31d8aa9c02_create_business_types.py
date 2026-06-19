"""create business types

Revision ID: 7f31d8aa9c02
Revises: 50966b549bdd
Create Date: 2026-06-20 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "7f31d8aa9c02"
down_revision: Union[str, Sequence[str], None] = "50966b549bdd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


BUSINESS_TYPES = [
    {"id": 1, "name": "CLOTHING", "description": "Clothing and apparel business"},
    {"id": 2, "name": "RETAIL", "description": "General retail business"},
    {"id": 3, "name": "GROCERY", "description": "Grocery and daily essentials business"},
    {"id": 4, "name": "RESTAURANT", "description": "Restaurant and dining business"},
    {"id": 5, "name": "CAFE", "description": "Cafe and beverage business"},
    {"id": 6, "name": "HARDWARE", "description": "Hardware and tools business"},
    {"id": 7, "name": "ELECTRONICS", "description": "Electronics and appliances business"},
]


def upgrade() -> None:
    business_types_table = op.create_table(
        "business_types",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_index(
        op.f("ix_business_types_name"),
        "business_types",
        ["name"],
        unique=False,
    )
    op.bulk_insert(business_types_table, BUSINESS_TYPES)

    op.add_column(
        "businesses",
        sa.Column("business_type_id", sa.Integer(), nullable=True),
    )
    op.execute(
        """
        UPDATE businesses
        SET business_type_id = business_types.id
        FROM business_types
        WHERE UPPER(businesses.business_type) = business_types.name
        """
    )
    op.execute(
        """
        UPDATE businesses
        SET business_type_id = 2
        WHERE business_type_id IS NULL
        """
    )
    op.alter_column("businesses", "business_type_id", nullable=False)
    op.create_foreign_key(
        "fk_businesses_business_type_id_business_types",
        "businesses",
        "business_types",
        ["business_type_id"],
        ["id"],
    )
    op.drop_column("businesses", "business_type")


def downgrade() -> None:
    op.add_column(
        "businesses",
        sa.Column("business_type", sa.String(length=100), nullable=True),
    )
    op.execute(
        """
        UPDATE businesses
        SET business_type = business_types.name
        FROM business_types
        WHERE businesses.business_type_id = business_types.id
        """
    )
    op.drop_constraint(
        "fk_businesses_business_type_id_business_types",
        "businesses",
        type_="foreignkey",
    )
    op.drop_column("businesses", "business_type_id")
    op.drop_index(op.f("ix_business_types_name"), table_name="business_types")
    op.drop_table("business_types")
