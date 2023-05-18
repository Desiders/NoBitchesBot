import datetime
from dataclasses import dataclass
from uuid import UUID

from src.domain.common.entities import Entity


@dataclass
class BitchChat(Entity):
    id: UUID
    bitch_id: UUID
    chat_id: UUID
    joined_date: datetime.datetime | None
    banned_at: datetime.datetime | None
