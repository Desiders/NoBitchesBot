from abc import ABC
from typing import Generic, TypeVar

CRes = TypeVar("CRes")


class Command(ABC, Generic[CRes]):
    pass


C = TypeVar("C", bound=Command)


class CommandHandler(ABC, Generic[C, CRes]):
    async def __call__(self, command: C) -> CRes:
        raise NotImplementedError
