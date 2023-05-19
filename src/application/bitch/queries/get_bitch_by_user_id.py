import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.bitch import dto
from src.application.bitch.interfaces import BitchReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBitchByUserId(Query[dto.Bitch]):
    user_id: UUID


class GetBitchByUserIdHandler(QueryHandler[GetBitchByUserId, dto.Bitch]):
    def __init__(self, bitch_reader: BitchReader) -> None:
        self._bitch_reader = bitch_reader

    async def __call__(self, query: GetBitchByUserId) -> dto.Bitch:
        bitch = await self._bitch_reader.get_by_user_id(
            query.user_id,
        )
        logger.debug(
            "Get bitch by user id",
            extra={
                "user_id": query.user_id,
                "bitch": bitch,
            },
        )
        return bitch
