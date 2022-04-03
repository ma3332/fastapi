"""add CDP

Revision ID: acb7f0961bac
Revises: b0fb9806efcc
Create Date: 2022-04-03 22:15:45.918923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acb7f0961bac'
down_revision = 'b0fb9806efcc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CDP',
    sa.Column('STT', sa.Integer(), nullable=False),
    sa.Column('depositor', sa.String(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('published', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False),
    sa.PrimaryKeyConstraint('STT')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('CDP')
    # ### end Alembic commands ###