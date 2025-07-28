"""add content column to post table

Revision ID: 467e04b1c222
Revises: 35569c654363
Create Date: 2025-07-28 16:13:54.033864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '467e04b1c222'
down_revision: Union[str, Sequence[str], None] = '35569c654363'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', 
                  sa.Column('content', sa.String(), nullable=False)
                  )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
