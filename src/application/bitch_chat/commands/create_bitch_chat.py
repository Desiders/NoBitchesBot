import datetime
import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.bitch_chat import dto
from src.application.bitch_chat.interfaces import BitchChatRepo
from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.domain.bitch_chat import entities

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class CreateBitchChat(Command[dto.BitchChat]):
    id: UUID
    bitch_id: UUID
    chat_id: UUID
    joined_date: datetime.datetime | None
    banned_at: datetime.datetime | None


class CreateBitchChatHandler(CommandHandler[CreateBitchChat, dto.BitchChat]):
    def __init__(
        self,
        bitch_chat_repo: BitchChatRepo,
        uow: UnitOfWork,
        mapper: Mapper,
    ) -> None:
        self._bitch_chat_repo = bitch_chat_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: CreateBitchChat) -> dto.BitchChat:
        bitch_chat = entities.BitchChat(
            command.id,
            command.bitch_id,
            command.chat_id,
            command.joined_date,
            command.banned_at,
        )

        await self._bitch_chat_repo.add_bitch_chat(bitch_chat)
        await self._uow.commit()

        logger.info(
            "Bitch chat created",
            extra={"bitch_chat": bitch_chat},
        )

        bitch_chat_dto = self._mapper.load(bitch_chat, dto.BitchChat)
        return bitch_chat_dto
