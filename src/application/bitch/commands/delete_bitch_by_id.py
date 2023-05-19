import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.bitch.interfaces import BitchRepo
from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DeleteBitchById(Command[None]):
    bitch_id: UUID


class DeleteBitchByIdHandler(CommandHandler[DeleteBitchById, None]):
    def __init__(
        self,
        bitch_repo: BitchRepo,
        uow: UnitOfWork,
        mapper: Mapper,
    ) -> None:
        self._bitch_repo = bitch_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: DeleteBitchById) -> None:
        await self._bitch_repo.delete_by_id(command.bitch_id)
        await self._uow.commit()

        logger.info(
            "Deleted bitch by id",
            extra={"bitch_id": command.bitch_id},
        )

        return None
