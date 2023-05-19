import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.bitch_chat import dto
from src.application.bitch_chat.interfaces import BitchChatReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBitchesChatsByChatId(Query[list[dto.BitchChat]]):
    chat_id: UUID


class GetBitchesChatsByChatIdHandler(
    QueryHandler[GetBitchesChatsByChatId, list[dto.BitchChat]]
):
    def __init__(self, bitch_reader: BitchChatReader) -> None:
        self._bitch_reader = bitch_reader

    async def __call__(self, query: GetBitchesChatsByChatId) -> list[dto.BitchChat]:
        bitches_chats = await self._bitch_reader.get_by_chat_id(
            query.chat_id,
        )
        logger.debug(
            "Get bitches chats by chat id",
            extra={
                "chat_id": query.chat_id,
                "bitches_chats": bitches_chats,
            },
        )
        return bitches_chats
