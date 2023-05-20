import logging
from dataclasses import dataclass

from src.application.ban_pattern.interfaces import BanPatternReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBanPatternsCount(Query[int]):
    pass


class GetBanPatternsCountHandler(QueryHandler[GetBanPatternsCount, int]):
    def __init__(self, ban_pattern_reader: BanPatternReader) -> None:
        self._ban_pattern_reader = ban_pattern_reader

    async def __call__(self, query: GetBanPatternsCount) -> int:
        ban_patterns_count = await self._ban_pattern_reader.get_ban_patterns_count()
        logger.debug(
            "Get ban patterns count",
            extra={
                "ban_patterns_count": ban_patterns_count,
            },
        )
        return ban_patterns_count
