import logging
from dataclasses import dataclass

from src.application.ban_pattern_bitch.interfaces import BanPatternBitchReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBanPatternsBitchesCount(Query[int]):
    pass


class GetBanPatternsBitchesCountHandler(QueryHandler[GetBanPatternsBitchesCount, int]):
    def __init__(self, ban_pattern_bitch_reader: BanPatternBitchReader) -> None:
        self._ban_pattern_bitch_reader = ban_pattern_bitch_reader

    async def __call__(self, query: GetBanPatternsBitchesCount) -> int:
        ban_pattern_bitches_count = (
            await self._ban_pattern_bitch_reader.get_ban_pattern_bitches_count()
        )
        logger.debug(
            "Get ban patterns bitches count",
            extra={
                "ban_pattern_bitches_count": ban_pattern_bitches_count,
            },
        )
        return ban_pattern_bitches_count
