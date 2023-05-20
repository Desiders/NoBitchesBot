import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.ban_pattern_bitch import dto
from src.application.ban_pattern_bitch.interfaces import BanPatternBitchReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBanPatternBitchById(Query[dto.BanPatternBitch]):
    ban_pattern_bitch_id: UUID


class GetBanPatternBitchByIdHandler(
    QueryHandler[GetBanPatternBitchById, dto.BanPatternBitch]
):
    def __init__(self, ban_pattern_bitch_reader: BanPatternBitchReader) -> None:
        self._ban_pattern_bitch_reader = ban_pattern_bitch_reader

    async def __call__(self, query: GetBanPatternBitchById) -> dto.BanPatternBitch:
        ban_pattern_bitch = await self._ban_pattern_bitch_reader.get_by_id(
            query.ban_pattern_bitch_id,
        )
        logger.debug(
            "Get ban pattern bitch by id",
            extra={
                "ban_pattern_bitch_id": query.ban_pattern_bitch_id,
                "ban_pattern_bitch": ban_pattern_bitch,
            },
        )
        return ban_pattern_bitch
