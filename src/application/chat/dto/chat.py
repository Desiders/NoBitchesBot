from dataclasses import dataclass
from uuid import UUID

from src.application.common.dto import DTO


@dataclass(frozen=True)
class Chat(DTO):
    id: UUID
    tg_id: int
    title: str | None
    username: str | None
