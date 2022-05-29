"""create relation from user to donation

Revision ID: 7c02e16d5d48
Revises: 3b2241a51fbf
Create Date: 2022-05-29 19:41:14.581759

"""
from alembic import op
import sqlalchemy as sa
import fastapi_users_db_sqlalchemy

# revision identifiers, used by Alembic.
revision = '7c02e16d5d48'
down_revision = '3b2241a51fbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', fastapi_users_db_sqlalchemy.guid.GUID(), nullable=True))
        batch_op.create_foreign_key('fk_donation_user_id_user', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###