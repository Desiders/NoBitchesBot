from dataclasses import dataclass
from uuid import UUID

from src.application.common.dto import DTO


@dataclass(frozen=True)
class MaybeBitchReaction(DTO):
    id: UUID
    maybe_bitch_id: UUID
    message_id: int
    emoji: str | None
    custom_emoji_id: str | None
