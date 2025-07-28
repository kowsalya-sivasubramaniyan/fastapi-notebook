"""add last few cols

Revision ID: a2ff919ab10b
Revises: 536f45391502
Create Date: 2025-07-28 17:08:10.122933

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2ff919ab10b'
down_revision: Union[str, Sequence[str], None] = '536f45391502'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',
                   sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE')
                   )
    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()'))
                  )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
