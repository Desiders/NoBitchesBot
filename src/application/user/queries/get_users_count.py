import logging
from dataclasses import dataclass

from src.application.common.query import Query, QueryHandler
from src.application.user.interfaces import UserReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetUsersCount(Query[int]):
    pass


class GetUsersCountHandler(QueryHandler[GetUsersCount, int]):
    def __init__(self, user_reader: UserReader) -> None:
        self._user_reader = user_reader

    async def __call__(self, query: GetUsersCount) -> int:
        users_count = await self._user_reader.get_users_count()
        logger.debug("Get users count", extra={"users_count": users_count})
        return users_count
