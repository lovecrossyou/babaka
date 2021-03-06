"""update data

Revision ID: d8ff0f81aa5f
Revises: a1df3d3dd40a
Create Date: 2017-05-08 17:44:26.078832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8ff0f81aa5f'
down_revision = 'a1df3d3dd40a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('sex', sa.String(length=12), nullable=True))
    op.create_index(op.f('ix_user_sex'), 'user', ['sex'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_sex'), table_name='user')
    op.drop_column('user', 'sex')
    # ### end Alembic commands ###
