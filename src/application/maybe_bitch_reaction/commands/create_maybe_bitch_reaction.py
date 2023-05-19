import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.application.maybe_bitch_reaction import dto
from src.application.maybe_bitch_reaction.interfaces import MaybeBitchReactionRepo
from src.domain.maybe_bitch_reaction import entities

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class CreateMaybeBitchReaction(Command[dto.MaybeBitchReaction]):
    id: UUID
    maybe_bitch_id: UUID
    message_id: int
    emoji: str | None
    custom_emoji_id: str | None


class CreateMaybeBitchReactionHandler(
    CommandHandler[CreateMaybeBitchReaction, dto.MaybeBitchReaction]
):
    def __init__(
        self,
        maybe_bitch_reaction_repo: MaybeBitchReactionRepo,
        uow: UnitOfWork,
        mapper: Mapper,
    ) -> None:
        self._maybe_bitch_reaction_repo = maybe_bitch_reaction_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(
        self, command: CreateMaybeBitchReaction
    ) -> dto.MaybeBitchReaction:
        maybe_bitch_reaction = entities.MaybeBitchReaction(
            command.id,
            command.maybe_bitch_id,
            command.message_id,
            command.emoji,
            command.custom_emoji_id,
        )

        await self._maybe_bitch_reaction_repo.add_maybe_bitch_reaction(
            maybe_bitch_reaction
        )
        await self._uow.commit()

        logger.info(
            "Get maybe bitch reaction created",
            extra={"maybe_bitch_reaction": maybe_bitch_reaction},
        )

        maybe_bitch_reaction_dto = self._mapper.load(
            maybe_bitch_reaction, dto.MaybeBitchReaction
        )
        return maybe_bitch_reaction_dto
