"""create posts table

Revision ID: 247cea43c9d4
Revises: 
Create Date: 2022-03-31 22:10:58.592893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "247cea43c9d4"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
