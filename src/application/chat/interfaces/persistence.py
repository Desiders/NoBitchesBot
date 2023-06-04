from typing import Protocol
from uuid import UUID

from src.application.chat import dto
from src.domain.chat import entities


class ChatReader(Protocol):
    async def get_by_id(self, chat_id: UUID) -> dto.Chat:
        raise NotImplementedError

    async def get_by_tg_id(self, tg_id: int) -> dto.Chat:
        raise NotImplementedError

    async def get_chats(self) -> list[dto.Chat]:
        raise NotImplementedError

    async def get_chats_count(self) -> int:
        raise NotImplementedError


class ChatRepo(Protocol):
    async def add_chat(self, chat: entities.Chat) -> None:
        raise NotImplementedError
