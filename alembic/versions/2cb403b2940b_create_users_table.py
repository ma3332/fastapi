"""create users table

Revision ID: 2cb403b2940b
Revises: 287f654b8fd4
Create Date: 2022-03-31 22:30:38.693816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2cb403b2940b"
down_revision = "287f654b8fd4"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("email", sa.String(), nullable=False, unique=True),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
