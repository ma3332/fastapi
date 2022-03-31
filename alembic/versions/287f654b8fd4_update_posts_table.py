"""update posts table

Revision ID: 287f654b8fd4
Revises: 247cea43c9d4
Create Date: 2022-03-31 22:25:20.951863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "287f654b8fd4"
down_revision = "247cea43c9d4"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("content", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_column(
        "posts",
        "content",
    )
    pass
