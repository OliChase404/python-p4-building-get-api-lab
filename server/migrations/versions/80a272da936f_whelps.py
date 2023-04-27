"""Whelps...

Revision ID: 80a272da936f
Revises: aefe07588d82
Create Date: 2023-04-27 09:47:51.969585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80a272da936f'
down_revision = 'aefe07588d82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bakery_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_baked_goods_bakery_bakeries', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_baked_goods_bakery_id_bakeries'), 'bakeries', ['bakery_id'], ['id'])
        batch_op.drop_column('bakery')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bakery', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_baked_goods_bakery_id_bakeries'), type_='foreignkey')
        batch_op.create_foreign_key('fk_baked_goods_bakery_bakeries', 'bakeries', ['bakery'], ['id'])
        batch_op.drop_column('bakery_id')

    # ### end Alembic commands ###
