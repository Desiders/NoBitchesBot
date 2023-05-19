import logging
from dataclasses import dataclass

from src.application.bitch.interfaces import BitchReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBitchesCount(Query[int]):
    pass


class GetBitchesCountHandler(QueryHandler[GetBitchesCount, int]):
    def __init__(self, bitch_reader: BitchReader) -> None:
        self._bitch_reader = bitch_reader

    async def __call__(self, query: GetBitchesCount) -> int:
        bitches_count = await self._bitch_reader.get_bitches_count()
        logger.debug(
            "Get bitches count",
            extra={
                "bitches_count": bitches_count,
            },
        )
        return bitches_count
