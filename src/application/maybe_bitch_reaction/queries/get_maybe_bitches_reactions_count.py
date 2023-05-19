import logging
from dataclasses import dataclass

from src.application.common.query import Query, QueryHandler
from src.application.maybe_bitch_reaction.interfaces import MaybeBitchReactionReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetMaybeBitchesReactionsCount(Query[int]):
    pass


class GetMaybeBitchesReactionsCountHandler(
    QueryHandler[GetMaybeBitchesReactionsCount, int]
):
    def __init__(self, maybe_bitch_reaction_reader: MaybeBitchReactionReader) -> None:
        self._maybe_bitch_reaction_reader = maybe_bitch_reaction_reader

    async def __call__(self, query: GetMaybeBitchesReactionsCount) -> int:
        maybe_bitches_reactions_count = (
            await self._maybe_bitch_reaction_reader.get_maybe_bitches_reactions_count()
        )
        logger.debug(
            "Get maybe bitches reactions count",
            extra={
                "maybe_bitches_reactions_count": maybe_bitches_reactions_count,
            },
        )
        return maybe_bitches_reactions_count
