from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from src.domain.ban_pattern.value_objects import PatternType
from uuid6 import uuid7

from .base import TimedBaseModel


class BanPattern(TimedBaseModel):
    __tablename__ = "ban_patterns"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid7, server_default=sa.func.uuid_generate_v7()
    )
    pattern_type: Mapped[PatternType]
    pattern: Mapped[str]
    description: Mapped[str | None]
