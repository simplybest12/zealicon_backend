"""create payments table

Revision ID: 30d7fc5491f7
Revises: 1777fb1636d4
Create Date: 2024-08-23 10:36:11.308790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30d7fc5491f7'
down_revision: Union[str, None] = '1777fb1636d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        op.create_table(
        'payments',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('payment_id', sa.String(6), unique=True, nullable=False, index=True),
        sa.Column('payment_date', sa.DateTime(), default=sa.func.now()),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'))
    )


def downgrade() -> None:
    op.drop_table('payments')
