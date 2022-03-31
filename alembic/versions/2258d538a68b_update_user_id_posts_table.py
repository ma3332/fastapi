"""update user_id posts table

Revision ID: 2258d538a68b
Revises: 2cb403b2940b
Create Date: 2022-03-31 22:44:01.619390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2258d538a68b"
down_revision = "2cb403b2940b"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("user_id", sa.Integer(), nullable=False),
    )
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["user_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column(table_name="posts", column_name="user_id")
    pass
