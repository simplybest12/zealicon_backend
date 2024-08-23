"""creating fk payment id

Revision ID: 92a77913f511
Revises: 789a3b645d55
Create Date: 2024-08-23 13:11:40.410071

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92a77913f511'
down_revision: Union[str, None] = '789a3b645d55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Add payment_id column to users table
    op.add_column('users', sa.Column('payment_id', sa.Integer(), nullable=True))
    # Create a foreign key constraint on payment_id
    op.create_foreign_key('fk_user_payment', 'users', 'payments', ['payment_id'], ['id'])

def downgrade():
    # Remove foreign key constraint
    op.drop_constraint('fk_user_payment', 'users', type_='foreignkey')
    # Remove payment_id column from users table
    op.drop_column('users', 'payment_id')
