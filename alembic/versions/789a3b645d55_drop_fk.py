"""drop fk

Revision ID: 789a3b645d55
Revises: 42cb755792c2
Create Date: 2024-08-23 11:18:12.548761

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '789a3b645d55'
down_revision: Union[str, None] = '42cb755792c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('users', 'payment_id')
    op.drop_column('payments','payment_id')


def downgrade() -> None:
    pass
