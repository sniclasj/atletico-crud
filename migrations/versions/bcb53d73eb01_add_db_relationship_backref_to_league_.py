"""Add db.relationship backref to league and club models, remove redundant fields from player model

Revision ID: bcb53d73eb01
Revises: a8603aea617e
Create Date: 2022-06-14 10:13:22.224223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcb53d73eb01'
down_revision = 'a8603aea617e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('player_player_image_url_key', 'player', type_='unique')
    op.drop_column('player', 'player_age')
    op.drop_column('player', 'player_image_url')
    op.drop_column('player', 'player_dob')
    op.drop_column('player', 'player_position')
    op.drop_column('player', 'player_nationality')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player', sa.Column('player_nationality', sa.VARCHAR(length=25), autoincrement=False, nullable=False))
    op.add_column('player', sa.Column('player_position', sa.VARCHAR(length=25), autoincrement=False, nullable=False))
    op.add_column('player', sa.Column('player_dob', sa.DATE(), autoincrement=False, nullable=False))
    op.add_column('player', sa.Column('player_image_url', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
    op.add_column('player', sa.Column('player_age', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_unique_constraint('player_player_image_url_key', 'player', ['player_image_url'])
    # ### end Alembic commands ###
