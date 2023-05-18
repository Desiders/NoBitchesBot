from dataclasses import dataclass
from uuid import UUID

from src.application.common.exceptions import ApplicationException


@dataclass(eq=False)
class MaybeBitchMessageIdAlreadyExists(ApplicationException):
    maybe_bitch_message_id: UUID

    @property
    def message(self) -> str:
        return (
            f'A maybe bitch message with "{self.maybe_bitch_message_id}" '
            "maybe_bitch_message_id already exists"
        )


@dataclass(eq=False)
class MaybeBitchMessageIdNotExist(ApplicationException):
    maybe_bitch_message_id: UUID

    @property
    def message(self) -> str:
        return (
            f'A maybe bitch message with "{self.maybe_bitch_message_id}" '
            "maybe_bitch_message_id doesn't exist"
        )


@dataclass(eq=False)
class MaybeBitchMessageBitchIdNotExist(ApplicationException):
    maybe_bitch_bitch_id: UUID

    @property
    def message(self) -> str:
        return (
            f'A maybe bitch message with "{self.maybe_bitch_bitch_id}" '
            "maybe_bitch_message_bitch_id doesn't exist"
        )


@dataclass(eq=False)
class MaybeBitchMessageMessageIdNotExist(ApplicationException):
    maybe_bitch_message_message_id: UUID

    @property
    def message(self) -> str:
        return (
            f'A maybe bitch message with "{self.maybe_bitch_message_message_id}" '
            "maybe_bitch_message_message_id doesn't exist"
        )
