import logging
from dataclasses import dataclass

from src.application.bitch_chat import dto
from src.application.bitch_chat.interfaces import BitchChatReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetBitchesChats(Query[list[dto.BitchChat]]):
    pass


class GetBitchesChatsHandler(QueryHandler[GetBitchesChats, list[dto.BitchChat]]):
    def __init__(self, bitch_chat_reader: BitchChatReader) -> None:
        self._bitch_chat_reader = bitch_chat_reader

    async def __call__(self, query: GetBitchesChats) -> list[dto.BitchChat]:
        bitches_chats = await self._bitch_chat_reader.get_bitches_chats()
        logger.debug(
            "Get bitches chats",
            extra={
                "bitches_chats": bitches_chats,
            },
        )
        return bitches_chats
