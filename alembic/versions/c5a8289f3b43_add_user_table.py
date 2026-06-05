"""add user table

Revision ID: c5a8289f3b43
Revises: 6ed4930f2a3bcd
Create Date: 2026-06-05 13:15:45.849273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5a8289f3b43'
down_revision: Union[str, Sequence[str], None] = '6ed4930f2a3bcd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable = False), 
                    sa.Column('email', sa.String(), nullable = False),
                    sa.Column('password', sa.String(), nullable = False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default = sa.text('now()'), nullable = False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass

