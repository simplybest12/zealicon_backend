"""create foreign key column in users table

Revision ID: 42cb755792c2
Revises: 30d7fc5491f7
Create Date: 2024-08-23 10:37:41.433399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42cb755792c2'
down_revision: Union[str, None] = '30d7fc5491f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add the payment_id column to the users table, referencing payments.id
    op.add_column('users', sa.Column('payment_id', sa.Integer, sa.ForeignKey('payments.id'), nullable=True))

def downgrade() -> None:
    # Remove the payment_id column from the users table
    op.drop_column('users', 'payment_id')
