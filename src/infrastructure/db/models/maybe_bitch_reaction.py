from uuid import UUID

import sqlalchemy as sa
from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from uuid6 import uuid7

from .base import TimedBaseModel


class MaybeBitchReaction(TimedBaseModel):
    __tablename__ = "maybe_bitches_reactions"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid7, server_default=sa.func.uuid_generate_v7()
    )
    maybe_bitch_id: Mapped[UUID] = mapped_column(ForeignKey("maybe_bitches.id"))
    message_id: Mapped[BigInteger]
    emoji: Mapped[str | None]
    custom_emoji_id: Mapped[str | None]
