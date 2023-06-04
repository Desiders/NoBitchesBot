from dataclasses import dataclass
from uuid import UUID

from src.application.common.dto import DTO


@dataclass(frozen=True)
class MaybeBitchMessage(DTO):
    id: UUID
    maybe_bitch_id: UUID
    chat_id: UUID
    message_id: int
    message: str | None
    caption: str | None
