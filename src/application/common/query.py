from abc import ABC
from typing import Generic, TypeVar

QRes = TypeVar("QRes")


class Query(ABC, Generic[QRes]):
    pass


Q = TypeVar("Q", bound=Query)


class QueryHandler(ABC, Generic[Q, QRes]):
    async def __call__(self, query: Q) -> QRes:
        raise NotImplementedError
