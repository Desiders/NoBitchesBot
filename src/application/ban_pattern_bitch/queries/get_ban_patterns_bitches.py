import logging
from dataclasses import dataclass

from src.application.ban_pattern_bitch import dto
from src.application.ban_pattern_bitch.interfaces import BanPatternBitchReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBanPatternBitchs(Query[list[dto.BanPatternBitch]]):
    pass


class GetBanPatternBitchsHandler(
    QueryHandler[GetBanPatternBitchs, list[dto.BanPatternBitch]]
):
    def __init__(self, ban_pattern_bitch_reader: BanPatternBitchReader) -> None:
        self._ban_pattern_bitch_reader = ban_pattern_bitch_reader

    async def __call__(self, query: GetBanPatternBitchs) -> list[dto.BanPatternBitch]:
        ban_pattern_bitches = (
            await self._ban_pattern_bitch_reader.get_ban_pattern_bitches()
        )
        logger.debug(
            "Get ban patterns bitches",
            extra={
                "ban_pattern_bitches": ban_pattern_bitches,
            },
        )
        return ban_pattern_bitches
