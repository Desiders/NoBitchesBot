import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.application.maybe_bitch_reaction.interfaces import MaybeBitchReactionRepo

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DeleteMaybeBitchReactionById(Command[None]):
    maybe_bitch_reaction_id: UUID


class DeleteMaybeBitchReactionByIdHandler(
    CommandHandler[DeleteMaybeBitchReactionById, None]
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

    async def __call__(self, command: DeleteMaybeBitchReactionById) -> None:
        await self._maybe_bitch_reaction_repo.delete_by_id(
            command.maybe_bitch_reaction_id
        )
        await self._uow.commit()

        logger.info(
            "Deleted maybe bitch reaction",
            extra={"maybe_bitch_reaction_id": command.maybe_bitch_reaction_id},
        )

        return None
