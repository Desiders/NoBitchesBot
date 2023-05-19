import logging
from dataclasses import dataclass

from src.application.chat import dto
from src.application.chat.interfaces import ChatReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetChats(Query[list[dto.Chat]]):
    pass


class GetChatsHandler(QueryHandler[GetChats, list[dto.Chat]]):
    def __init__(self, chat_reader: ChatReader) -> None:
        self._chat_reader = chat_reader

    async def __call__(self, query: GetChats) -> list[dto.Chat]:
        chats = await self._chat_reader.get_chats()
        logger.debug("Get chats", extra={"chats": chats})
        return chats
