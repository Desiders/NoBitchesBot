import datetime
from dataclasses import dataclass
from uuid import UUID

from src.application.common.dto import DTO


@dataclass(frozen=True)
class BitchChat(DTO):
    id: UUID
    bitch_id: UUID
    chat_id: UUID
    joined_date: datetime.datetime | None
    banned_at: datetime.datetime | None
