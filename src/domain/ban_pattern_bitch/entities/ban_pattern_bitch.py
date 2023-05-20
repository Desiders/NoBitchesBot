from dataclasses import dataclass
from uuid import UUID

from src.domain.common.entities import Entity


@dataclass
class BanPatternBitch(Entity):
    id: UUID
    ban_pattern_id: UUID
    bitch_id: UUID
