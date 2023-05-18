from dataclasses import dataclass
from uuid import UUID

from src.domain.common.entities import Entity


@dataclass
class MaybeBitchMessage(Entity):
    id: UUID
    maybe_bitch_id: UUID
    message_id: int
    message: str | None
    caption: str | None
