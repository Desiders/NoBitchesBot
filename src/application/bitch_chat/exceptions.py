from dataclasses import dataclass
from uuid import UUID

from src.application.common.exceptions import ApplicationException


@dataclass(eq=False)
class BitchChatIdAlreadyExists(ApplicationException):
    bitch_chat_id: UUID

    @property
    def message(self) -> str:
        return f'A bitch chat with "{self.bitch_chat_id}" bitch_chat_id already exists'


@dataclass(eq=False)
class BitchChatIdNotExist(ApplicationException):
    bitch_chat_id: UUID

    @property
    def message(self) -> str:
        return f'A bitch chat with "{self.bitch_chat_id}" bitch_chat_id doesn\'t exist'
