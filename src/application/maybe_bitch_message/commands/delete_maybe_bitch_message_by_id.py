import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.application.maybe_bitch_message.interfaces import MaybeBitchMessageRepo

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DeleteMaybeBitchMessageById(Command[None]):
    maybe_bitch_message_id: UUID


class DeleteMaybeBitchMessageByIdHandler(
    CommandHandler[DeleteMaybeBitchMessageById, None]
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

    async def __call__(self, command: DeleteMaybeBitchMessageById) -> None:
        await self._maybe_bitch_message_repo.delete_by_id(
            command.maybe_bitch_message_id
        )
        await self._uow.commit()

        logger.info(
            "Deleted maybe bitch message by id",
            extra={"maybe_bitch_message_id": command.maybe_bitch_message_id},
        )

        return None
