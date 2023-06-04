from dataclasses import dataclass
from uuid import UUID

from src.application.common.exceptions import ApplicationException


@dataclass(eq=False)
class ChatIdAlreadyExists(ApplicationException):
    chat_id: UUID

    @property
    def message(self) -> str:
        return f'A chat with "{self.chat_id}" chat_id already exists'


@dataclass(eq=False)
class ChatTgIdAlreadyExists(ApplicationException):
    chat_tg_id: int

    @property
    def message(self) -> str:
        return f'A chat with "{self.chat_tg_id}" tg_id already exists'


@dataclass(eq=False)
class ChatIdNotExist(ApplicationException):
    chat_id: UUID

    @property
    def message(self) -> str:
        return f'A chat with "{self.chat_id}" chat_id doesn\'t exist'


@dataclass(eq=False)
class ChatTgIdNotExist(ApplicationException):
    chat_tg_id: int

    @property
    def message(self) -> str:
        return f'A chat with "{self.chat_tg_id}" tg_id doesn\'t exist'
