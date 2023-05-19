import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.query import Query, QueryHandler
from src.application.maybe_bitch_reaction import dto
from src.application.maybe_bitch_reaction.interfaces import MaybeBitchReactionReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetMaybeBitchesReactionsByMessageId(Query[list[dto.MaybeBitchReaction]]):
    message_id: UUID


class GetMaybeBitchesReactionsByMessageIdHandler(
    QueryHandler[GetMaybeBitchesReactionsByMessageId, list[dto.MaybeBitchReaction]]
):
    def __init__(self, maybe_bitch_reaction_reader: MaybeBitchReactionReader) -> None:
        self._maybe_bitch_reaction_reader = maybe_bitch_reaction_reader

    async def __call__(
        self, query: GetMaybeBitchesReactionsByMessageId
    ) -> list[dto.MaybeBitchReaction]:
        maybe_bitches_reactions = (
            await self._maybe_bitch_reaction_reader.get_by_message_id(
                query.message_id,
            )
        )
        logger.debug(
            "Get maybe bitches reactions by message id",
            extra={
                "message_id": query.message_id,
                "maybe_bitches_reactions": maybe_bitches_reactions,
            },
        )
        return maybe_bitches_reactions
