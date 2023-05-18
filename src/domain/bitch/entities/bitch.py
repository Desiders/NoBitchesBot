from dataclasses import dataclass
from uuid import UUID

from src.domain.common.entities import Entity


@dataclass
class Bitch(Entity):
    id: UUID
    user_id: UUID
    reason: str | None
