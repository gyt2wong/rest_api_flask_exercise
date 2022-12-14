"""empty message

Revision ID: 318addb6bc19
Revises: 54807bd6d5ac
Create Date: 2022-11-14 02:27:47.178484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '318addb6bc19'
down_revision = '54807bd6d5ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
