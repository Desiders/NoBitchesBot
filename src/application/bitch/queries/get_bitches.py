import logging
from dataclasses import dataclass

from src.application.bitch import dto
from src.application.bitch.interfaces import BitchReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBitches(Query[list[dto.Bitch]]):
    pass


class GetBitchesHandler(QueryHandler[GetBitches, list[dto.Bitch]]):
    def __init__(self, bitch_reader: BitchReader) -> None:
        self._bitch_reader = bitch_reader

    async def __call__(self, query: GetBitches) -> list[dto.Bitch]:
        bitches = await self._bitch_reader.get_bitches()
        logger.debug(
            "Get bitches",
            extra={
                "bitches": bitches,
            },
        )
        return bitches
