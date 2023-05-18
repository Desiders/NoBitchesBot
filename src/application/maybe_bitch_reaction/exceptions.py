from dataclasses import dataclass
from uuid import UUID

from src.application.common.exceptions import ApplicationException


@dataclass(eq=False)
class MaybeBitchReactionIdAlreadyExists(ApplicationException):
    maybe_bitch_reaction_id: UUID

    @property
    def reaction(self) -> str:
        return (
            f'A maybe bitch reaction with "{self.maybe_bitch_reaction_id}" '
            "maybe_bitch_reaction_id already exists"
        )


@dataclass(eq=False)
class MaybeBitchReactionIdNotExist(ApplicationException):
    maybe_bitch_reaction_id: UUID

    @property
    def reaction(self) -> str:
        return (
            f'A maybe bitch reaction with "{self.maybe_bitch_reaction_id}" '
            "maybe_bitch_reaction_id doesn't exist"
        )


@dataclass(eq=False)
class MaybeBitchReactionBitchIdNotExist(ApplicationException):
    maybe_bitch_bitch_id: UUID

    @property
    def reaction(self) -> str:
        return (
            f'A maybe bitch reaction with "{self.maybe_bitch_bitch_id}" '
            "maybe_bitch_reaction_bitch_id doesn't exist"
        )
