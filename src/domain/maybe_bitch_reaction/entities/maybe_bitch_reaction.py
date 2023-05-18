from dataclasses import dataclass
from uuid import UUID

from src.domain.common.entities import Entity


@dataclass
class MaybeBitchReaction(Entity):
    id: UUID
    maybe_bitch_id: UUID
    message_id: int
    emoji: str | None
    custom_emoji_id: str | None
