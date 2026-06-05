"""add more columns to post table

Revision ID: 560ed7afa402
Revises: 75323790b9d8
Create Date: 2026-06-05 13:43:27.047313

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '560ed7afa402'
down_revision: Union[str, Sequence[str], None] = '75323790b9d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', 
                    sa.Column('published', sa.Boolean(), nullable = False, server_default = 'True'))
    op.add_column('posts', 
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable = False, server_default = sa.text('now()')))
    pass



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
