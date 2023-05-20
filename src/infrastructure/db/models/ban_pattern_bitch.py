from uuid import UUID

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from uuid6 import uuid7

from .base import TimedBaseModel


class BanPatternBitch(TimedBaseModel):
    __tablename__ = "ban_patterns_bitches"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid7, server_default=sa.func.uuid_generate_v7()
    )
    ban_pattern_id: Mapped[UUID] = mapped_column(ForeignKey("ban_patterns.id"))
    bitch_id: Mapped[UUID] = mapped_column(ForeignKey("bitches.id"))
