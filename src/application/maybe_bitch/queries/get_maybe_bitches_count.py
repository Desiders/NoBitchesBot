import logging
from dataclasses import dataclass

from src.application.common.query import Query, QueryHandler
from src.application.maybe_bitch.interfaces import MaybeBitchReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetMaybeBitchesCount(Query[int]):
    pass


class GetMaybeBitchesCountHandler(QueryHandler[GetMaybeBitchesCount, int]):
    def __init__(self, maybe_bitch_reader: MaybeBitchReader) -> None:
        self._maybe_bitch_reader = maybe_bitch_reader

    async def __call__(self, query: GetMaybeBitchesCount) -> int:
        maybe_bitches_count = await self._maybe_bitch_reader.get_maybe_bitches_count()
        logger.debug(
            "Get maybe bitches count",
            extra={
                "maybe_bitches_count": maybe_bitches_count,
            },
        )
        return maybe_bitches_count
