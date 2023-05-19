import logging
from dataclasses import dataclass

from src.application.chat import dto
from src.application.chat.interfaces import ChatReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetChatByTgId(Query[dto.Chat]):
    tg_id: int


class GetChatByTgIdHandler(QueryHandler[GetChatByTgId, dto.Chat]):
    def __init__(self, chat_reader: ChatReader) -> None:
        self._chat_reader = chat_reader

    async def __call__(self, query: GetChatByTgId) -> dto.Chat:
        chat = await self._chat_reader.get_by_tg_id(query.tg_id)
        logger.debug("Get chat by tg id", extra={"tg_id": query.tg_id, "chat": chat})
        return chat
