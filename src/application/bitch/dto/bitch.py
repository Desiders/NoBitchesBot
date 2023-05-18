from dataclasses import dataclass
from uuid import UUID

from src.application.common.dto import DTO


@dataclass(frozen=True)
class Bitch(DTO):
    id: UUID
    user_id: UUID
    reason: str | None
