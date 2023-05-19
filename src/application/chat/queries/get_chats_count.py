import logging
from dataclasses import dataclass

from src.application.chat.interfaces import ChatReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetChatsCount(Query[int]):
    pass


class GetChatsCountHandler(QueryHandler[GetChatsCount, int]):
    def __init__(self, chat_reader: ChatReader) -> None:
        self._chat_reader = chat_reader

    async def __call__(self, query: GetChatsCount) -> int:
        chats_count = await self._chat_reader.get_chats_count()
        logger.debug("Get chats count", extra={"chats_count": chats_count})
        return chats_count
