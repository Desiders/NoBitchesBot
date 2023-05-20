import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.ban_pattern import dto
from src.application.ban_pattern.interfaces import BanPatternReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBanPatternById(Query[dto.BanPattern]):
    ban_pattern_id: UUID


class GetBanPatternByIdHandler(QueryHandler[GetBanPatternById, dto.BanPattern]):
    def __init__(self, ban_pattern_reader: BanPatternReader) -> None:
        self._ban_pattern_reader = ban_pattern_reader

    async def __call__(self, query: GetBanPatternById) -> dto.BanPattern:
        ban_pattern = await self._ban_pattern_reader.get_by_id(
            query.ban_pattern_id,
        )
        logger.debug(
            "Get ban pattern by id",
            extra={
                "ban_pattern_id": query.ban_pattern_id,
                "ban_pattern": ban_pattern,
            },
        )
        return ban_pattern
