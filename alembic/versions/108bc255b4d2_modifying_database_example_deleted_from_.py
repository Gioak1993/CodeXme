"""modifying database, example deleted from problem db

Revision ID: 108bc255b4d2
Revises: 7c2fa4b593c1
Create Date: 2024-04-30 19:49:55.009299

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '108bc255b4d2'
down_revision: Union[str, None] = '7c2fa4b593c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('problem', sa.Column('input_values', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.drop_column('problem', 'input_description')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('problem', sa.Column('input_description', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('problem', 'input_values')
    # ### end Alembic commands ###
