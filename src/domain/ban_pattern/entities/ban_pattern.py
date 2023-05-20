from dataclasses import dataclass
from uuid import UUID

from src.domain.ban_pattern.value_objects import PatternType
from src.domain.common.entities import Entity


@dataclass
class BanPattern(Entity):
    id: UUID
    pattern_type: PatternType
    pattern: str
    description: str | None
