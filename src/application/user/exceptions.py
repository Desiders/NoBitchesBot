from dataclasses import dataclass
from uuid import UUID

from src.application.common.exceptions import ApplicationException


@dataclass(eq=False)
class UserIdAlreadyExists(ApplicationException):
    user_id: UUID

    @property
    def message(self) -> str:
        return f'A user with "{self.user_id}" user_id already exists'


@dataclass(eq=False)
class UserTgIdAlreadyExists(ApplicationException):
    user_tg_id: UUID

    @property
    def message(self) -> str:
        return f'A user with "{self.user_tg_id}" tg_id already exists'


@dataclass(eq=False)
class UserIdNotExist(ApplicationException):
    user_id: UUID

    @property
    def message(self) -> str:
        return f'A user with "{self.user_id}" user_id doesn\'t exist'


@dataclass(eq=False)
class UserTgIdNotExist(ApplicationException):
    user_tg_id: UUID

    @property
    def message(self) -> str:
        return f'A user with "{self.user_tg_id}" tg_id doesn\'t exist'
