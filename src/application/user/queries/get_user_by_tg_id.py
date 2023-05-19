import logging
from dataclasses import dataclass

from src.application.common.query import Query, QueryHandler
from src.application.user import dto
from src.application.user.interfaces import UserReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetUserByTgId(Query[dto.User]):
    tg_id: int


class GetUserByTgIdHandler(QueryHandler[GetUserByTgId, dto.User]):
    def __init__(self, user_reader: UserReader) -> None:
        self._user_reader = user_reader

    async def __call__(self, query: GetUserByTgId) -> dto.User:
        user = await self._user_reader.get_by_tg_id(query.tg_id)
        logger.debug("Get user by tg id", extra={"tg_id": query.tg_id, "user": user})
        return user
