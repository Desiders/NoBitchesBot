import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.query import Query, QueryHandler
from src.application.user import dto
from src.application.user.interfaces import UserReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetUserById(Query[dto.User]):
    user_id: UUID


class GetUserByIdHandler(QueryHandler[GetUserById, dto.User]):
    def __init__(self, user_reader: UserReader) -> None:
        self._user_reader = user_reader

    async def __call__(self, query: GetUserById) -> dto.User:
        user = await self._user_reader.get_by_id(query.user_id)
        logger.debug("Get user by id", extra={"user_id": query.user_id, "user": user})
        return user
