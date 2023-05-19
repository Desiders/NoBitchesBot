import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.query import Query, QueryHandler
from src.application.maybe_bitch_reaction import dto
from src.application.maybe_bitch_reaction.interfaces import MaybeBitchReactionReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetMaybeBitchReactionByMaybeBitchId(Query[dto.MaybeBitchReaction]):
    maybe_bitch_id: UUID


class GetMaybeBitchReactionByMaybeBitchIdHandler(
    QueryHandler[GetMaybeBitchReactionByMaybeBitchId, dto.MaybeBitchReaction]
):
    def __init__(self, maybe_bitch_reaction_reader: MaybeBitchReactionReader) -> None:
        self._maybe_bitch_reaction_reader = maybe_bitch_reaction_reader

    async def __call__(
        self, query: GetMaybeBitchReactionByMaybeBitchId
    ) -> dto.MaybeBitchReaction:
        maybe_bitch_reaction = (
            await self._maybe_bitch_reaction_reader.get_by_maybe_bitch_id(
                query.maybe_bitch_id,
            )
        )
        logger.debug(
            "Get maybe bitch reaction by maybe bitch id",
            extra={
                "maybe_bitch_id": query.maybe_bitch_id,
                "maybe_bitch_reaction": maybe_bitch_reaction,
            },
        )
        return maybe_bitch_reaction
