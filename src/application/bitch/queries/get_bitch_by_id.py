import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.bitch import dto
from src.application.bitch.interfaces import BitchReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBitchById(Query[dto.Bitch]):
    bitch_id: UUID


class GetBitchByIdHandler(QueryHandler[GetBitchById, dto.Bitch]):
    def __init__(self, bitch_reader: BitchReader) -> None:
        self._bitch_reader = bitch_reader

    async def __call__(self, query: GetBitchById) -> dto.Bitch:
        bitch = await self._bitch_reader.get_by_id(
            query.bitch_id,
        )
        logger.debug(
            "Get bitch by id",
            extra={
                "bitch_id": query.bitch_id,
                "bitch": bitch,
            },
        )
        return bitch
