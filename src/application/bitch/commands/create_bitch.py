import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.bitch import dto
from src.application.bitch.interfaces import BitchRepo
from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.domain.bitch import entities

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class CreateBitch(Command[dto.Bitch]):
    id: UUID
    user_id: UUID
    reason: str | None


class CreateBitchHandler(CommandHandler[CreateBitch, dto.Bitch]):
    def __init__(
        self,
        bitch_repo: BitchRepo,
        uow: UnitOfWork,
        mapper: Mapper,
    ) -> None:
        self._bitch_repo = bitch_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: CreateBitch) -> dto.Bitch:
        bitch = entities.Bitch(
            command.id,
            command.user_id,
            command.reason,
        )

        await self._bitch_repo.add_bitch(bitch)
        await self._uow.commit()

        logger.info(
            "Bitch created",
            extra={"bitch": bitch},
        )

        bitch_dto = self._mapper.load(bitch, dto.Bitch)
        return bitch_dto
