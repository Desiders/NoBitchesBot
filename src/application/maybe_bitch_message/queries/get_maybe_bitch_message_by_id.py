import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.query import Query, QueryHandler
from src.application.maybe_bitch_message import dto
from src.application.maybe_bitch_message.interfaces import MaybeBitchMessageReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetMaybeBitchMessageById(Query[dto.MaybeBitchMessage]):
    maybe_bitch_message_id: UUID


class GetMaybeBitchMessageByIdHandler(
    QueryHandler[GetMaybeBitchMessageById, dto.MaybeBitchMessage]
):
    def __init__(self, maybe_bitch_message_reader: MaybeBitchMessageReader) -> None:
        self._maybe_bitch_message_reader = maybe_bitch_message_reader

    async def __call__(self, query: GetMaybeBitchMessageById) -> dto.MaybeBitchMessage:
        maybe_bitch_message = await self._maybe_bitch_message_reader.get_by_id(
            query.maybe_bitch_message_id,
        )
        logger.debug(
            "Get maybe bitch message by id",
            extra={
                "maybe_bitch_message_id": query.maybe_bitch_message_id,
                "maybe_bitch_message": maybe_bitch_message,
            },
        )
        return maybe_bitch_message
