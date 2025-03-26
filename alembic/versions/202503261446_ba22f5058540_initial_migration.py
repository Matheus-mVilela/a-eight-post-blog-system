"""initial-migration

Revision ID: ba22f5058540
Revises:
Create Date: 2025-03-26 14:46:55.358456
"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'ba22f5058540'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'gpt_post',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('prompt', sa.String(), nullable=True),
        sa.Column(
            'response', postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_gpt_post_id'), 'gpt_post', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_gpt_post_id'), table_name='gpt_post')
    op.drop_table('gpt_post')
