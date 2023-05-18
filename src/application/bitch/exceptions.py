from dataclasses import dataclass
from uuid import UUID

from src.application.common.exceptions import ApplicationException


@dataclass(eq=False)
class BitchIdAlreadyExists(ApplicationException):
    bitch_id: UUID

    @property
    def message(self) -> str:
        return f'A bitch with "{self.bitch_id}" bitch_id already exists'


@dataclass(eq=False)
class BitchIdNotExist(ApplicationException):
    bitch_id: UUID

    @property
    def message(self) -> str:
        return f'A bitch with "{self.bitch_id}" bitch_id doesn\'t exist'


@dataclass(eq=False)
class BitchUserIdNotExist(ApplicationException):
    bitch_user_id: UUID

    @property
    def message(self) -> str:
        return f'A bitch with "{self.bitch_user_id}" bitch_user_id doesn\'t exist'
