from dataclasses import dataclass
from uuid import UUID

from src.application.common.dto import DTO
from src.domain.ban_pattern.value_objects import PatternType


@dataclass(frozen=True)
class BanPattern(DTO):
    d: UUID
    pattern_type: PatternType
    pattern: str
    description: str | None
