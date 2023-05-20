import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.ban_pattern_bitch import dto
from src.application.ban_pattern_bitch.interfaces import BanPatternBitchReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBanPatternsBitchesByBanPatternId(Query[list[dto.BanPatternBitch]]):
    ban_pattern_id: UUID


class GetBanPatternsBitchesByBanPatternIdHandler(
    QueryHandler[GetBanPatternsBitchesByBanPatternId, list[dto.BanPatternBitch]]
):
    def __init__(self, ban_pattern_bitch_reader: BanPatternBitchReader) -> None:
        self._ban_pattern_bitch_reader = ban_pattern_bitch_reader

    async def __call__(
        self, query: GetBanPatternsBitchesByBanPatternId
    ) -> list[dto.BanPatternBitch]:
        ban_patterns_bitches = (
            await self._ban_pattern_bitch_reader.get_by_ban_pattern_id(
                query.ban_pattern_id,
            )
        )
        logger.debug(
            "Get ban patterns bitchs by ban pattern id",
            extra={
                "ban_pattern_id": query.ban_pattern_id,
                "ban_patterns_bitches": ban_patterns_bitches,
            },
        )
        return ban_patterns_bitches
