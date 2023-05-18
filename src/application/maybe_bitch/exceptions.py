from dataclasses import dataclass
from uuid import UUID

from src.application.common.exceptions import ApplicationException


@dataclass(eq=False)
class MaybeBitchIdAlreadyExists(ApplicationException):
    maybe_bitch_id: UUID

    @property
    def message(self) -> str:
        return (
            f'A maybe bitch with "{self.maybe_bitch_id}" maybe_bitch_id already exists'
        )


@dataclass(eq=False)
class MaybeBitchIdNotExist(ApplicationException):
    maybe_bitch_id: UUID

    @property
    def message(self) -> str:
        return (
            f'A maybe bitch with "{self.maybe_bitch_id}" maybe_bitch_id doesn\'t exist'
        )


@dataclass(eq=False)
class MaybeBitchUserIdNotExist(ApplicationException):
    maybe_bitch_user_id: UUID

    @property
    def message(self) -> str:
        return f'A maybe bitch with "{self.maybe_bitch_user_id}" user_id doesn\'t exist'
