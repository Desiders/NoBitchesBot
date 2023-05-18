from dataclasses import dataclass
from uuid import UUID

from src.domain.common.entities import Entity


@dataclass
class Chat(Entity):
    id: UUID
    tg_id: int
    title: str | None
    username: str | None
