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


@dataclass(eq=False)
class BitchChatBitchIdNotExist(ApplicationException):
    bitch_chat_bitch_id: UUID

    @property
    def message(self) -> str:
        return f'A bitch chat with "{self.bitch_chat_bitch_id}" bitch_chat_bitch_id doesn\'t exist'


@dataclass(eq=False)
class BitchChatChatIdNotExist(ApplicationException):
    bitch_chat_chat_id: UUID

    @property
    def message(self) -> str:
        return f'A bitch chat with "{self.bitch_chat_chat_id}" bitch_chat_chat_id doesn\'t exist'
