"""added fields to Comment and Post model that reference each other

Revision ID: 33d03c2f6176
Revises: 6ba0e37c3edd
Create Date: 2019-05-16 17:23:25.117686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33d03c2f6176'
down_revision = '6ba0e37c3edd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('post_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comment', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'post_id')
    # ### end Alembic commands ###
