from dataclasses import dataclass
from uuid import UUID

from src.domain.common.entities import Entity


@dataclass
class User(Entity):
    id: UUID
    tg_id: int
    first_name: str
    last_name: str | None
    username: str | None
    about: str | None

    @property
    def full_name(self) -> str:
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name
