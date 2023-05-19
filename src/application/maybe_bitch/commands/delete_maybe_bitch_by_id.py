import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.application.maybe_bitch.interfaces import MaybeBitchRepo

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DeleteMaybeBitchById(Command[None]):
    maybe_bitch_id: UUID


class DeleteMaybeBitchByIdHandler(CommandHandler[DeleteMaybeBitchById, None]):
    def __init__(
        self,
        maybe_bitch_repo: MaybeBitchRepo,
        uow: UnitOfWork,
        mapper: Mapper,
    ) -> None:
        self._maybe_bitch_repo = maybe_bitch_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: DeleteMaybeBitchById) -> None:
        await self._maybe_bitch_repo.delete_by_id(command.maybe_bitch_id)
        await self._uow.commit()

        logger.info(
            "Deleted maybe bitch by id",
            extra={"maybe_bitch_id": command.maybe_bitch_id},
        )

        return None
