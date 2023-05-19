import logging
from dataclasses import dataclass

from src.application.bitch_chat.interfaces import BitchChatReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBitchesChatsCount(Query[int]):
    pass


class GetBitchesChatsCountHandler(QueryHandler[GetBitchesChatsCount, int]):
    def __init__(self, bitch_chat_reader: BitchChatReader) -> None:
        self._bitch_chat_reader = bitch_chat_reader

    async def __call__(self, query: GetBitchesChatsCount) -> int:
        bitches_chats_count = await self._bitch_chat_reader.get_bitches_chats_count()
        logger.debug(
            "Get bitches chats count",
            extra={
                "bitches_chats_count": bitches_chats_count,
            },
        )
        return bitches_chats_count
