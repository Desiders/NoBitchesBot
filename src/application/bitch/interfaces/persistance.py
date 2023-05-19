from typing import Protocol
from uuid import UUID

from src.application.bitch import dto
from src.domain.bitch import entities


class BitchReader(Protocol):
    async def get_by_id(self, bitch_id: UUID) -> dto.Bitch:
        raise NotImplementedError

    async def get_by_user_id(self, user_id: UUID) -> dto.Bitch:
        raise NotImplementedError

    async def get_bitches(self) -> list[dto.Bitch]:
        raise NotImplementedError

    async def get_bitches_count(self) -> int:
        raise NotImplementedError


class BitchRepo(Protocol):
    async def add_bitch(self, bitch: entities.Bitch) -> None:
        raise NotImplementedError

    async def delete_by_id(self, bitch_id: UUID) -> None:
        raise NotImplementedError
