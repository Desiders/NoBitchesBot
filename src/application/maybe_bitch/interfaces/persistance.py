from typing import Protocol
from uuid import UUID

from src.application.maybe_bitch import dto
from src.domain.maybe_bitch import entities


class MaybeBitchReader(Protocol):
    async def get_by_id(self, maybe_bitch_id: UUID) -> dto.MaybeBitch:
        raise NotImplementedError

    async def get_by_user_id(self, user_id: UUID) -> dto.MaybeBitch:
        raise NotImplementedError

    async def get_maybe_bitches(self) -> list[dto.MaybeBitch]:
        raise NotImplementedError

    async def get_maybe_bitches_count(self) -> int:
        raise NotImplementedError


class MaybeBitchRepo(Protocol):
    async def add_maybe_bitch(self, maybe_bitch: entities.MaybeBitch) -> None:
        raise NotImplementedError

    async def delete_maybe_bitch(self, maybe_bitch: entities.MaybeBitch) -> None:
        raise NotImplementedError
