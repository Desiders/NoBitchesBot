import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.chat import dto
from src.application.chat.interfaces import ChatReader
from src.application.common.query import Query, QueryHandler

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetChatById(Query[dto.Chat]):
    chat_id: UUID


class GetChatByIdHandler(QueryHandler[GetChatById, dto.Chat]):
    def __init__(self, chat_reader: ChatReader) -> None:
        self._chat_reader = chat_reader

    async def __call__(self, query: GetChatById) -> dto.Chat:
        chat = await self._chat_reader.get_by_id(query.chat_id)
        logger.debug("Get chat by id", extra={"chat_id": query.chat_id, "chat": chat})
        return chat
