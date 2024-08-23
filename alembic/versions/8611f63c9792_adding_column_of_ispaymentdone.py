"""adding column of ispaymentdone

Revision ID: 8611f63c9792
Revises: 92a77913f511
Create Date: 2024-08-23 13:21:39.404515

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8611f63c9792'
down_revision: Union[str, None] = '92a77913f511'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.add_column('users', sa.Column('ispaymentdone', sa.Boolean(), nullable=False, server_default='false'))

def downgrade() -> None:
    op.drop_column('users', 'ispaymentdone')