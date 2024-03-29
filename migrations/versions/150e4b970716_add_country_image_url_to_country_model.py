"""Add country_image_url to country model

Revision ID: 150e4b970716
Revises: d055b8c3b88f
Create Date: 2022-05-30 09:45:43.435013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '150e4b970716'
down_revision = 'd055b8c3b88f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('country', sa.Column('country_image_url', sa.String(length=250), nullable=True))
    op.create_unique_constraint(None, 'country', ['country_image_url'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'country', type_='unique')
    op.drop_column('country', 'country_image_url')
    # ### end Alembic commands ###
