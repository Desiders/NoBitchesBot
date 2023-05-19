import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.bitch_chat import dto
from src.application.bitch_chat.interfaces import BitchChatReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBitchesChatsByBitchId(Query[list[dto.BitchChat]]):
    bitch_id: UUID


class GetBitchesChatsByBitchIdHandler(
    QueryHandler[GetBitchesChatsByBitchId, list[dto.BitchChat]]
):
    def __init__(self, bitch_reader: BitchChatReader) -> None:
        self._bitch_reader = bitch_reader

    async def __call__(self, query: GetBitchesChatsByBitchId) -> list[dto.BitchChat]:
        bitches_chats = await self._bitch_reader.get_by_bitch_id(
            query.bitch_id,
        )
        logger.debug(
            "Get bitches chats by user id",
            extra={
                "bitch_id": query.bitch_id,
                "bitches_chats": bitches_chats,
            },
        )
        return bitches_chats
