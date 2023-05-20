import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.ban_pattern.interfaces import BanPatternRepo
from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DeleteBanPatternById(Command[None]):
    ban_pattern_id: UUID


class DeleteBanPatternByIdHandler(CommandHandler[DeleteBanPatternById, None]):
    def __init__(
        self,
        ban_pattern_repo: BanPatternRepo,
        uow: UnitOfWork,
        mapper: Mapper,
    ) -> None:
        self._ban_pattern_repo = ban_pattern_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: DeleteBanPatternById) -> None:
        await self._ban_pattern_repo.delete_by_id(command.ban_pattern_id)
        await self._uow.commit()

        logger.info(
            "Deleted ban pattern by id",
            extra={"ban_pattern_id": command.ban_pattern_id},
        )

        return None
