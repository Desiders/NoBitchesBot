import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.ban_pattern_bitch import dto
from src.application.ban_pattern_bitch.interfaces import BanPatternBitchRepo
from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.domain.ban_pattern_bitch import entities

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class CreateBanPatternBitch(Command[dto.BanPatternBitch]):
    id: UUID
    ban_pattern_id: UUID
    bitch_id: UUID


class CreateBanPatternBitchHandler(
    CommandHandler[CreateBanPatternBitch, dto.BanPatternBitch]
):
    def __init__(
        self,
        ban_pattern_bitch_repo: BanPatternBitchRepo,
        uow: UnitOfWork,
        mapper: Mapper,
    ) -> None:
        self._ban_pattern_bitch_repo = ban_pattern_bitch_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: CreateBanPatternBitch) -> dto.BanPatternBitch:
        ban_pattern_bitch = entities.BanPatternBitch(
            command.id,
            command.ban_pattern_id,
            command.bitch_id,
        )

        await self._ban_pattern_bitch_repo.add_ban_pattern_bitch(ban_pattern_bitch)
        await self._uow.commit()

        logger.info(
            "Ban pattern bitch created",
            extra={"ban_pattern_bitch": ban_pattern_bitch},
        )

        ban_pattern_bitch_dto = self._mapper.load(
            ban_pattern_bitch, dto.BanPatternBitch
        )
        return ban_pattern_bitch_dto
