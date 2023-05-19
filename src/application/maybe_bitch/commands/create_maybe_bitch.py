import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.application.maybe_bitch import dto
from src.application.maybe_bitch.interfaces import MaybeBitchRepo
from src.domain.maybe_bitch import entities

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class CreateMaybeBitch(Command[dto.MaybeBitch]):
    id: UUID
    user_id: UUID


class CreateMaybeBitchHandler(CommandHandler[CreateMaybeBitch, dto.MaybeBitch]):
    def __init__(
        self,
        maybe_bitch_repo: MaybeBitchRepo,
        uow: UnitOfWork,
        mapper: Mapper,
    ) -> None:
        self._maybe_bitch_repo = maybe_bitch_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: CreateMaybeBitch) -> dto.MaybeBitch:
        maybe_bitch = entities.MaybeBitch(
            command.id,
            command.user_id,
        )

        await self._maybe_bitch_repo.add_maybe_bitch(maybe_bitch)
        await self._uow.commit()

        logger.info(
            "Maybe bitch created",
            extra={"maybe_bitch": maybe_bitch},
        )

        maybe_bitch_dto = self._mapper.load(maybe_bitch, dto.MaybeBitch)
        return maybe_bitch_dto
