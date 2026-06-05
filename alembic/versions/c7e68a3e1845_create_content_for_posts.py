"""create content for posts

Revision ID: 6ed4930f2a3bcd
Revises: 9a8a790c605e
Create Date: 2026-06-05 12:27:50.682394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ed4930f2a3bcd'
down_revision: Union[str, Sequence[str], None] = '9a8a790c605e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
