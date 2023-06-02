"""Added custom url path in db

Revision ID: e74550eb93e7
Revises: 
Create Date: 2023-06-02 17:49:51.514092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e74550eb93e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('link', schema=None) as batch_op:
        batch_op.add_column(sa.Column('custom_url', sa.String(length=50), nullable=True))
        batch_op.alter_column('short_url',
               existing_type=sa.VARCHAR(length=5),
               type_=sa.String(length=4),
               existing_nullable=True)
        batch_op.create_unique_constraint('uq_custom_url', ['custom_url'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('link', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('short_url',
               existing_type=sa.String(length=4),
               type_=sa.VARCHAR(length=5),
               existing_nullable=True)
        batch_op.drop_column('custom_url')

    # ### end Alembic commands ###
