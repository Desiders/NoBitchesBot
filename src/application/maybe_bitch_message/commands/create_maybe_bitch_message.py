import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.application.maybe_bitch_message import dto
from src.application.maybe_bitch_message.interfaces import MaybeBitchMessageRepo
from src.domain.maybe_bitch_message import entities

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class CreateMaybeBitchMessage(Command[dto.MaybeBitchMessage]):
    id: UUID
    maybe_bitch_id: UUID
    message_id: int
    message: str | None = None
    caption: str | None = None


class CreateMaybeBitchMessageHandler(
    CommandHandler[CreateMaybeBitchMessage, dto.MaybeBitchMessage]
):
    def __init__(
        self,
        maybe_bitch_message_repo: MaybeBitchMessageRepo,
        uow: UnitOfWork,
        mapper: Mapper,
    ) -> None:
        self._maybe_bitch_message_repo = maybe_bitch_message_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: CreateMaybeBitchMessage) -> dto.MaybeBitchMessage:
        maybe_bitch_message = entities.MaybeBitchMessage(
            command.id,
            command.maybe_bitch_id,
            command.message_id,
            command.message,
            command.caption,
        )

        await self._maybe_bitch_message_repo.add_maybe_bitch_message(
            maybe_bitch_message
        )
        await self._uow.commit()

        logger.info(
            "Maybe bitch message created",
            extra={"maybe_bitch_message": maybe_bitch_message},
        )

        maybe_bitch_message_dto = self._mapper.load(
            maybe_bitch_message, dto.MaybeBitchMessage
        )
        return maybe_bitch_message_dto
