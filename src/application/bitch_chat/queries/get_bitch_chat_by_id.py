import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.bitch_chat import dto
from src.application.bitch_chat.interfaces import BitchChatReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBitchChatById(Query[dto.BitchChat]):
    bitch_chat_id: UUID


class GetBitchChatByIdHandler(QueryHandler[GetBitchChatById, dto.BitchChat]):
    def __init__(self, bitch_chat_reader: BitchChatReader) -> None:
        self._bitch_chat_reader = bitch_chat_reader

    async def __call__(self, query: GetBitchChatById) -> dto.BitchChat:
        bitch_chat = await self._bitch_chat_reader.get_by_id(
            query.bitch_chat_id,
        )
        logger.debug(
            "Get bitch chat by id",
            extra={
                "bitch_chat_id": query.bitch_chat_id,
                "bitch_chat": bitch_chat,
            },
        )
        return bitch_chat
