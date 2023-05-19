import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.bitch_chat.interfaces import BitchChatRepo
from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DeleteBitchChatById(Command[None]):
    bitch_chat_id: UUID


class DeleteBitchChatByIdHandler(CommandHandler[DeleteBitchChatById, None]):
    def __init__(
        self,
        bitch_chat_repo: BitchChatRepo,
        uow: UnitOfWork,
        mapper: Mapper,
    ) -> None:
        self._bitch_chat_repo = bitch_chat_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: DeleteBitchChatById) -> None:
        await self._bitch_chat_repo.delete_by_id(command.bitch_chat_id)
        await self._uow.commit()

        logger.info(
            "Deleted bitch chat by id",
            extra={"bitch_chat_id": command.bitch_chat_id},
        )

        return None
