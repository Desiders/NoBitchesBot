from dataclasses import dataclass
from uuid import UUID

from src.application.common.dto import DTO


@dataclass(frozen=True)
class BanPatternBitch(DTO):
    id: UUID
    ban_pattern_id: UUID
    bitch_id: UUID
