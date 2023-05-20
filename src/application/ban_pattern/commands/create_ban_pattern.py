import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.ban_pattern import dto
from src.application.ban_pattern.interfaces import BanPatternRepo
from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.domain.ban_pattern import entities
from src.domain.ban_pattern.value_objects import PatternType

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class CreateBanPattern(Command[dto.BanPattern]):
    id: UUID
    pattern_type: PatternType
    pattern: str
    description: str | None


class CreateBanPatternHandler(CommandHandler[CreateBanPattern, dto.BanPattern]):
    def __init__(
        self,
        ban_pattern_repo: BanPatternRepo,
        uow: UnitOfWork,
        mapper: Mapper,
    ) -> None:
        self._ban_pattern_repo = ban_pattern_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: CreateBanPattern) -> dto.BanPattern:
        ban_pattern = entities.BanPattern(
            command.id,
            command.pattern_type,
            command.pattern,
            command.description,
        )

        await self._ban_pattern_repo.add_ban_pattern(ban_pattern)
        await self._uow.commit()

        logger.info(
            "Ban pattern created",
            extra={"ban_pattern": ban_pattern},
        )

        ban_pattern_dto = self._mapper.load(ban_pattern, dto.BanPattern)
        return ban_pattern_dto
