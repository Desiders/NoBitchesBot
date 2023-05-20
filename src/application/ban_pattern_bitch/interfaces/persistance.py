from typing import Protocol
from uuid import UUID

from src.application.ban_pattern_bitch import dto
from src.domain.ban_pattern_bitch import entities


class BanPatternBitchReader(Protocol):
    async def get_by_id(self, ban_pattern_bitch_id: UUID) -> dto.BanPatternBitch:
        raise NotImplementedError

    async def get_by_ban_pattern_id(
        self, ban_pattern_id: UUID
    ) -> list[dto.BanPatternBitch]:
        raise NotImplementedError

    async def get_by_bitch_id(self, bitch_id: UUID) -> list[dto.BanPatternBitch]:
        raise NotImplementedError

    async def get_ban_pattern_bitches(self) -> list[dto.BanPatternBitch]:
        raise NotImplementedError

    async def get_ban_pattern_bitches_count(self) -> int:
        raise NotImplementedError


class BanPatternBitchRepo(Protocol):
    async def add_ban_pattern_bitch(
        self, ban_pattern_bitch: entities.BanPatternBitch
    ) -> None:
        raise NotImplementedError

    async def delete_by_id(self, ban_pattern_bitch_id: UUID) -> None:
        raise NotImplementedError
