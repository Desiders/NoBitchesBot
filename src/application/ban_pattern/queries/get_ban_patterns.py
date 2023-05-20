import logging
from dataclasses import dataclass

from src.application.ban_pattern import dto
from src.application.ban_pattern.interfaces import BanPatternReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBanPatterns(Query[list[dto.BanPattern]]):
    pass


class GetBanPatternsHandler(QueryHandler[GetBanPatterns, list[dto.BanPattern]]):
    def __init__(self, ban_pattern_reader: BanPatternReader) -> None:
        self._ban_pattern_reader = ban_pattern_reader

    async def __call__(self, query: GetBanPatterns) -> list[dto.BanPattern]:
        ban_patterns = await self._ban_pattern_reader.get_ban_patterns()
        logger.debug(
            "Get ban patterns",
            extra={
                "ban_patterns": ban_patterns,
            },
        )
        return ban_patterns
