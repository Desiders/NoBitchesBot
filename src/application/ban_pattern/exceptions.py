from dataclasses import dataclass
from uuid import UUID

from src.application.common.exceptions import ApplicationException


@dataclass(eq=False)
class BanPatternIdAlreadyExists(ApplicationException):
    ban_pattern_id: UUID

    @property
    def message(self) -> str:
        return (
            f'A ban pattern with "{self.ban_pattern_id}" ban_pattern_id already exists'
        )


@dataclass(eq=False)
class BanPatternIdNotExist(ApplicationException):
    ban_pattern_id: UUID

    @property
    def message(self) -> str:
        return (
            f'A ban pattern with "{self.ban_pattern_id}" ban_pattern_id doesn\'t exist'
        )
