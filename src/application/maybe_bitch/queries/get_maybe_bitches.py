import logging
from dataclasses import dataclass

from src.application.common.query import Query, QueryHandler
from src.application.maybe_bitch import dto
from src.application.maybe_bitch.interfaces import MaybeBitchReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetMaybeBitches(Query[list[dto.MaybeBitch]]):
    pass


class GetMaybeBitchesHandler(QueryHandler[GetMaybeBitches, list[dto.MaybeBitch]]):
    def __init__(self, maybe_bitch_reader: MaybeBitchReader) -> None:
        self._maybe_bitch_reader = maybe_bitch_reader

    async def __call__(self, query: GetMaybeBitches) -> list[dto.MaybeBitch]:
        maybe_bitches = await self._maybe_bitch_reader.get_maybe_bitches()
        logger.debug(
            "Get maybe bitches",
            extra={
                "maybe_bitches": maybe_bitches,
            },
        )
        return maybe_bitches
