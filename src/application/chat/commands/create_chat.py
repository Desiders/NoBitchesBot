import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.chat import dto
from src.application.chat.interfaces import ChatRepo
from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.domain.chat import entities

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class CreateChat(Command[dto.Chat]):
    id: UUID
    tg_id: int
    title: str | None
    username: str | None


class CreateChatHandler(CommandHandler[CreateChat, dto.Chat]):
    def __init__(self, chat_repo: ChatRepo, uow: UnitOfWork, mapper: Mapper) -> None:
        self._chat_repo = chat_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: CreateChat) -> dto.Chat:
        chat = entities.Chat(
            command.id,
            command.tg_id,
            command.title,
            command.username,
        )

        await self._chat_repo.add_chat(chat)
        await self._uow.commit()

        logger.info("Chat created", extra={"chat": chat})

        chat_dto = self._mapper.load(chat, dto.Chat)
        return chat_dto
