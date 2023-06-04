from dataclasses import dataclass
from uuid import UUID

from src.application.common.exceptions import ApplicationException


@dataclass(eq=False)
class BanPatternBitchIdAlreadyExists(ApplicationException):
    ban_pattern_bitch_id: UUID

    @property
    def message(self) -> str:
        return (
            f'A ban pattern bitch with "{self.ban_pattern_bitch_id}" '
            "ban_pattern_bitch_id already exists"
        )


@dataclass(eq=False)
class BanPatternBitchIdNotExist(ApplicationException):
    ban_pattern_bitch_id: UUID

    @property
    def message(self) -> str:
        return (
            f'A ban pattern bitch with "{self.ban_pattern_bitch_id}" '
            "ban_pattern_bitch_id doesn't exist"
        )
