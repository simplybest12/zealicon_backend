"""dropping payment id

Revision ID: bbf14aa18863
Revises: 2cac4b8d3d77
Create Date: 2024-08-23 13:38:30.185568

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bbf14aa18863'
down_revision: Union[str, None] = '2cac4b8d3d77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
