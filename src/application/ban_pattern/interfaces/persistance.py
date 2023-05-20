from typing import Protocol
from uuid import UUID

from src.application.ban_pattern import dto
from src.domain.ban_pattern import entities


class BanPatternReader(Protocol):
    async def get_by_id(self, ban_pattern_id: UUID) -> dto.BanPattern:
        raise NotImplementedError

    async def get_ban_patterns(self) -> list[dto.BanPattern]:
        raise NotImplementedError

    async def get_ban_patterns_count(self) -> int:
        raise NotImplementedError


class BanPatternRepo(Protocol):
    async def add_ban_pattern(self, ban_pattern: entities.BanPattern) -> None:
        raise NotImplementedError

    async def delete_by_id(self, ban_pattern_id: UUID) -> None:
        raise NotImplementedError
