import logging
from dataclasses import dataclass

from src.application.common.query import Query, QueryHandler
from src.application.maybe_bitch_reaction import dto
from src.application.maybe_bitch_reaction.interfaces import MaybeBitchReactionReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetMaybeBitchesReactions(Query[list[dto.MaybeBitchReaction]]):
    pass


class GetMaybeBitchesReactionsHandler(
    QueryHandler[GetMaybeBitchesReactions, list[dto.MaybeBitchReaction]]
):
    def __init__(self, maybe_bitch_reaction_reader: MaybeBitchReactionReader) -> None:
        self._maybe_bitch_reaction_reader = maybe_bitch_reaction_reader

    async def __call__(
        self, query: GetMaybeBitchesReactions
    ) -> list[dto.MaybeBitchReaction]:
        maybe_bitches_reactions = (
            await self._maybe_bitch_reaction_reader.get_maybe_bitches_reactions()
        )
        logger.debug(
            "Get maybe bitches reactions",
            extra={
                "maybe_bitches_reactions": maybe_bitches_reactions,
            },
        )
        return maybe_bitches_reactions
