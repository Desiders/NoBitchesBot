from typing import Protocol
from uuid import UUID

from src.application.bitch_chat import dto
from src.domain.bitch_chat import entities


class BitchChatReader(Protocol):
    async def get_by_id(self, bitch_chat_id: UUID) -> dto.BitchChat:
        raise NotImplementedError

    async def get_by_bitch_id(self, bitch_id: UUID) -> dto.BitchChat:
        raise NotImplementedError

    async def get_by_chat_id(self, chat_id: UUID) -> dto.BitchChat:
        raise NotImplementedError

    async def get_bitches_chats(self) -> list[dto.BitchChat]:
        raise NotImplementedError

    async def get_bitches_chats_count(self) -> int:
        raise NotImplementedError


class BitchChatRepo(Protocol):
    async def add_bitch_chat(self, bitch_chat: entities.BitchChat) -> None:
        raise NotImplementedError

    async def delete_bitch_chat(self, bitch_chat: entities.BitchChat) -> None:
        raise NotImplementedError
