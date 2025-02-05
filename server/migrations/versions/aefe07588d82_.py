"""empty message

Revision ID: aefe07588d82
Revises: 56184725f82d
Create Date: 2023-04-27 09:25:14.823480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aefe07588d82'
down_revision = '56184725f82d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Integer(),
               type_=sa.FLOAT(),
               existing_nullable=True)

    # ### end Alembic commands ###
