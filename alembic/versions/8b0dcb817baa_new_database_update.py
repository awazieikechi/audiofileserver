"""New database update

Revision ID: 8b0dcb817baa
Revises: 
Create Date: 2021-03-20 22:02:30.833871

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8b0dcb817baa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audiobooks',
    sa.Column('id', mysql.INTEGER(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('author', sa.String(length=100), nullable=False),
    sa.Column('narrator', sa.String(length=100), nullable=False),
    sa.Column('duration', mysql.INTEGER(), nullable=False),
    sa.Column('uploaded_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_audiobooks_id'), 'audiobooks', ['id'], unique=True)
    op.create_table('podcasts',
    sa.Column('id', mysql.INTEGER(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('duration', mysql.INTEGER(), nullable=False),
    sa.Column('uploaded_time', sa.DateTime(), nullable=True),
    sa.Column('host', sa.String(length=100), nullable=False),
    sa.Column('participants', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_podcasts_id'), 'podcasts', ['id'], unique=True)
    op.create_table('songs',
    sa.Column('id', mysql.INTEGER(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('duration', mysql.INTEGER(), nullable=False),
    sa.Column('uploaded_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_songs_id'), 'songs', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_songs_id'), table_name='songs')
    op.drop_table('songs')
    op.drop_index(op.f('ix_podcasts_id'), table_name='podcasts')
    op.drop_table('podcasts')
    op.drop_index(op.f('ix_audiobooks_id'), table_name='audiobooks')
    op.drop_table('audiobooks')
    # ### end Alembic commands ###
