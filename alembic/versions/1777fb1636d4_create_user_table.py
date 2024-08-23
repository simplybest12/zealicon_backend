"""create user table

Revision ID: 1777fb1636d4
Revises: 
Create Date: 2024-08-23 10:18:46.961228

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1777fb1636d4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('username', sa.String(), nullable=False, index=True),
        sa.Column('email', sa.String(), nullable=False, unique=True, index=True),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('phone_number', sa.String(), nullable=False),
        sa.Column('is_admin', sa.Boolean(), default=False),
        sa.Column('created_at', sa.DateTime(), default=sa.func.now())
    )


def downgrade() -> None:
    # Drop the users table
    op.drop_table('users')
