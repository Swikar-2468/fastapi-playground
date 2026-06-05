"""add fkey to post table

Revision ID: 75323790b9d8
Revises: c5a8289f3b43
Create Date: 2026-06-05 13:19:52.573403

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75323790b9d8'
down_revision: Union[str, Sequence[str], None] = 'c5a8289f3b43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('Owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('post_users_fk', source_table = 'posts', referent_table='users', local_cols=['Owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk', table_name = 'posts')
    op.drop_column('posts', 'owner_id')
    pass
