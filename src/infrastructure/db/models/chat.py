from uuid import UUID

import sqlalchemy as sa
from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from uuid6 import uuid7

from .base import TimedBaseModel


class Chat(TimedBaseModel):
    __tablename__ = "chats"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid7, server_default=sa.func.uuid_generate_v7()
    )
    tg_id: Mapped[BigInteger] = mapped_column(unique=True)
    title: Mapped[str | None]
    username: Mapped[str | None]
