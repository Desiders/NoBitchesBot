import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.query import Query, QueryHandler
from src.application.maybe_bitch import dto
from src.application.maybe_bitch.interfaces import MaybeBitchReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetMaybeBitchById(Query[dto.MaybeBitch]):
    maybe_bitch_id: UUID


class GetMaybeBitchByIdHandler(QueryHandler[GetMaybeBitchById, dto.MaybeBitch]):
    def __init__(self, maybe_bitch_reader: MaybeBitchReader) -> None:
        self._maybe_bitch_reader = maybe_bitch_reader

    async def __call__(self, query: GetMaybeBitchById) -> dto.MaybeBitch:
        maybe_bitch = await self._maybe_bitch_reader.get_by_id(
            query.maybe_bitch_id,
        )
        logger.debug(
            "Get maybe bitch by id",
            extra={
                "maybe_bitch_id": query.maybe_bitch_id,
                "maybe_bitch": maybe_bitch,
            },
        )
        return maybe_bitch
