from uuid import UUID

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from uuid6 import uuid7

from .base import TimedBaseModel


class MaybeBitch(TimedBaseModel):
    __tablename__ = "maybe_bitches"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid7, server_default=sa.func.uuid_generate_v7()
    )
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
