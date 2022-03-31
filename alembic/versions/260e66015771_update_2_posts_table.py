"""update 2 posts table

Revision ID: 260e66015771
Revises: 2258d538a68b
Create Date: 2022-03-31 22:51:41.629863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "260e66015771"
down_revision = "2258d538a68b"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="True"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column(table_name="posts", column_name="published")
    op.drop_column(table_name="posts", column_name="created_at")
    pass
