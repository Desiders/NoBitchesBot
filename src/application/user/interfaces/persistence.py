from typing import Protocol
from uuid import UUID

from src.application.user import dto
from src.domain.user import entities


class UserReader(Protocol):
    async def get_by_id(self, user_id: UUID) -> dto.User:
        raise NotImplementedError

    async def get_by_tg_id(self, tg_id: int) -> dto.User:
        raise NotImplementedError

    async def get_users(self) -> list[dto.User]:
        raise NotImplementedError

    async def get_users_count(self) -> int:
        raise NotImplementedError


class UserRepo(Protocol):
    async def add_user(self, user: entities.User) -> None:
        raise NotImplementedError
