import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from uuid6 import uuid7

from .base import TimedBaseModel


class BitchChat(TimedBaseModel):
    __tablename__ = "bitches_chats"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid7, server_default=sa.func.uuid_generate_v7()
    )
    bitch_id: Mapped[UUID] = mapped_column(ForeignKey("bitches.id"))
    chat_id: Mapped[UUID] = mapped_column(ForeignKey("chats.id"))
    joined_date: Mapped[datetime.datetime | None]
    banned_at: Mapped[datetime.datetime | None]
