from typing import NoReturn
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.exc import DBAPIError, IntegrityError
from src.application.chat import dto
from src.application.chat.exceptions import (
    ChatIdAlreadyExists,
    ChatIdNotExist,
    ChatTgIdAlreadyExists,
    ChatTgIdNotExist,
)
from src.application.chat.interfaces import ChatReader, ChatRepo
from src.application.common.exceptions import RepoError
from src.domain.chat import entities
from src.infrastructure.db import models
from src.infrastructure.db.exception_mapper import exception_mapper
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class ChatReaderImpl(SQLAlchemyRepo, ChatReader):
    @exception_mapper
    async def get_by_id(self, chat_id: UUID) -> dto.Chat:
        chat = await self._session.scalar(
            select(models.Chat).where(
                models.Chat.id == chat_id,
            )
        )
        if chat is None:
            raise ChatIdNotExist(chat_id)

        return self._mapper.load(chat, dto.Chat)

    @exception_mapper
    async def get_by_tg_id(self, tg_id: int) -> dto.Chat:
        chat = await self._session.scalar(
            select(models.Chat).where(
                models.Chat.tg_id == tg_id,
            )
        )
        if chat is None:
            raise ChatTgIdNotExist(tg_id)

        return self._mapper.load(chat, dto.Chat)

    @exception_mapper
    async def get_chats(self) -> list[dto.Chat]:
        result = await self._session.scalars(select(models.Chat))
        chats = result.all()

        return self._mapper.load(chats, list[dto.Chat])

    @exception_mapper
    async def get_chats_count(self) -> int:
        return await self._session.scalar(select(func.count(models.Chat.id))) or 0


class ChatRepoImpl(SQLAlchemyRepo, ChatRepo):
    @exception_mapper
    async def add_chat(self, chat: entities.Chat) -> None:
        chat_model = self._mapper.load(chat, models.Chat)
        self._session.add(chat_model)

        try:
            await self._session.flush((chat_model,))
        except IntegrityError as err:
            self._parse_error(err, chat)

    def _parse_error(self, err: DBAPIError, chat: entities.Chat) -> NoReturn:
        match err.__cause__.__cause__.constraint_name:  # type: ignore
            case "pk_chats":
                raise ChatIdAlreadyExists(chat.id) from err
            case "uq_chats_tg_id":
                raise ChatTgIdAlreadyExists(chat.tg_id) from err
            case _:
                raise RepoError from err
