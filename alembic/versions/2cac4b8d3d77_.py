"""empty message

Revision ID: 2cac4b8d3d77
Revises: 8611f63c9792
Create Date: 2024-08-23 13:30:13.311628

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2cac4b8d3d77'
down_revision: Union[str, None] = '8611f63c9792'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
