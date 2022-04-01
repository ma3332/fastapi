"""remove phone to users

Revision ID: 75d797949ec3
Revises: 9416e779df37
Create Date: 2022-04-01 02:04:18.418758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "75d797949ec3"
down_revision = "9416e779df37"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("users_phone_number_key", "users", type_="unique")
    op.drop_column("users", "phone_number")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column("phone_number", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.create_unique_constraint("users_phone_number_key", "users", ["phone_number"])
    # ### end Alembic commands ###
