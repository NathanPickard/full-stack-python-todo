"""empty message

Revision ID: 06cb6324206c
Revises: 0d576e2c5729
Create Date: 2020-05-19 17:56:34.745112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06cb6324206c'
down_revision = '0d576e2c5729'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###

    op.execute('UPDATE todos SET completed = False WHERE completed is NULL;')

    op.alter_column('todos', 'completed', nullable=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
