import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.query import Query, QueryHandler
from src.application.maybe_bitch import dto
from src.application.maybe_bitch.interfaces import MaybeBitchReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetMaybeBitchByUserId(Query[dto.MaybeBitch]):
    user_id: UUID


class GetMaybeBitchByUserIdHandler(QueryHandler[GetMaybeBitchByUserId, dto.MaybeBitch]):
    def __init__(self, maybe_bitch_reader: MaybeBitchReader) -> None:
        self._maybe_bitch_reader = maybe_bitch_reader

    async def __call__(self, query: GetMaybeBitchByUserId) -> dto.MaybeBitch:
        maybe_bitch = await self._maybe_bitch_reader.get_by_user_id(
            query.user_id,
        )
        logger.debug(
            "Get maybe bitch by user id",
            extra={
                "user_id": query.user_id,
                "maybe_bitch": maybe_bitch,
            },
        )
        return maybe_bitch
