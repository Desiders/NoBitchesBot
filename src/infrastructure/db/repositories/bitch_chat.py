from uuid import UUID

from sqlalchemy import delete, func, select
from sqlalchemy.exc import IntegrityError
from src.application.bitch_chat import dto
from src.application.bitch_chat.exceptions import (
    BitchChatIdAlreadyExists,
    BitchChatIdNotExist,
)
from src.application.bitch_chat.interfaces import BitchChatReader, BitchChatRepo
from src.domain.bitch_chat import entities
from src.infrastructure.db import models
from src.infrastructure.db.exception_mapper import exception_mapper
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class BitchChatReaderImpl(SQLAlchemyRepo, BitchChatReader):
    @exception_mapper
    async def get_by_id(self, bitch_chat_id: UUID) -> dto.BitchChat:
        bitch_chat = await self._session.scalar(
            select(models.BitchChat).where(
                models.BitchChat.id == bitch_chat_id,
            )
        )
        if bitch_chat is None:
            raise BitchChatIdNotExist(bitch_chat_id)

        return self._mapper.load(bitch_chat, dto.BitchChat)

    @exception_mapper
    async def get_by_bitch_id(self, bitch_id: UUID) -> list[dto.BitchChat]:
        result = await self._session.scalars(
            select(models.BitchChat).where(
                models.BitchChat.bitch_id == bitch_id,
            )
        )
        bitches_chats = result.all()

        return self._mapper.load(bitches_chats, list[dto.BitchChat])

    @exception_mapper
    async def get_by_chat_id(self, chat_id: UUID) -> list[dto.BitchChat]:
        result = await self._session.scalars(
            select(models.BitchChat).where(
                models.BitchChat.chat_id == chat_id,
            )
        )
        bitches_chats = result.all()

        return self._mapper.load(bitches_chats, list[dto.BitchChat])

    @exception_mapper
    async def get_bitches_chats(self) -> list[dto.BitchChat]:
        result = await self._session.scalars(select(models.BitchChat))
        bitches_chats = result.all()

        return self._mapper.load(bitches_chats, list[dto.BitchChat])

    @exception_mapper
    async def get_bitches_chats_count(self) -> int:
        return await self._session.scalar(select(func.count(models.BitchChat.id))) or 0


class BitchChatRepoImpl(SQLAlchemyRepo, BitchChatRepo):
    @exception_mapper
    async def add_bitch_chat(self, bitch_chat: entities.BitchChat) -> None:
        bitch_chat_model = self._mapper.load(bitch_chat, models.BitchChat)
        self._session.add(bitch_chat_model)

        try:
            await self._session.flush((bitch_chat_model,))
        except IntegrityError as err:
            raise BitchChatIdAlreadyExists(bitch_chat.id) from err

    @exception_mapper
    async def delete_by_id(self, bitch_chat_id: UUID) -> None:
        await self._session.execute(
            delete(models.BitchChat).where(models.BitchChat.id == bitch_chat_id)
        )

        return None
