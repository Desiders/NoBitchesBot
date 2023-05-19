import logging
from dataclasses import dataclass

from src.application.common.query import Query, QueryHandler
from src.application.user import dto
from src.application.user.interfaces import UserReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetUsers(Query[list[dto.User]]):
    pass


class GetUsersHandler(QueryHandler[GetUsers, list[dto.User]]):
    def __init__(self, user_reader: UserReader) -> None:
        self._user_reader = user_reader

    async def __call__(self, query: GetUsers) -> list[dto.User]:
        users = await self._user_reader.get_users()
        logger.debug("Get users", extra={"users": users})
        return users
