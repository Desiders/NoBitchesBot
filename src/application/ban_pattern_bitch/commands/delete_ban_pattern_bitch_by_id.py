import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.ban_pattern_bitch.interfaces import BanPatternBitchRepo
from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DeleteBanPatternBitchById(Command[None]):
    ban_pattern_bitch_id: UUID


class DeleteBanPatternBitchByIdHandler(CommandHandler[DeleteBanPatternBitchById, None]):
    def __init__(
        self,
        ban_pattern_bitch_repo: BanPatternBitchRepo,
        uow: UnitOfWork,
        mapper: Mapper,
    ) -> None:
        self._ban_pattern_bitch_repo = ban_pattern_bitch_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: DeleteBanPatternBitchById) -> None:
        await self._ban_pattern_bitch_repo.delete_by_id(command.ban_pattern_bitch_id)
        await self._uow.commit()

        logger.info(
            "Deleted ban pattern bitch by id",
            extra={"ban_pattern_bitch_id": command.ban_pattern_bitch_id},
        )

        return None
