"""Initial migration.

Revision ID: 0abca56398b9
Revises: 
Create Date: 2022-05-24 08:58:45.512836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0abca56398b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player', sa.Column('player_dob', sa.Date(), nullable=False))
    op.add_column('player', sa.Column('player_age', sa.Integer(), nullable=False))
    op.add_column('player', sa.Column('player_nationality', sa.String(length=25), nullable=False))
    op.add_column('player', sa.Column('player_position', sa.String(length=25), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('player', 'player_position')
    op.drop_column('player', 'player_nationality')
    op.drop_column('player', 'player_age')
    op.drop_column('player', 'player_dob')
    # ### end Alembic commands ###
