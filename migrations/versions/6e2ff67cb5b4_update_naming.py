"""update naming

Revision ID: 6e2ff67cb5b4
Revises: 70be79cf09ae
Create Date: 2022-03-06 23:37:49.725313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e2ff67cb5b4'
down_revision = '70be79cf09ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment', sa.String(), nullable=True))
    op.drop_column('comments', 'pitch_comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_comment', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('comments', 'comment')
    # ### end Alembic commands ###
