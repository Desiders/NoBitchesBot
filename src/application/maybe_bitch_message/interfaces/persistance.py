from typing import Protocol
from uuid import UUID

from src.application.maybe_bitch_message import dto
from src.domain.maybe_bitch_message import entities


class MaybeBitchMessageReader(Protocol):
    async def get_by_id(self, maybe_bitch_message_id: UUID) -> dto.MaybeBitchMessage:
        raise NotImplementedError

    async def get_by_maybe_bitch_id(
        self, maybe_bitch_id: UUID
    ) -> dto.MaybeBitchMessage:
        raise NotImplementedError

    async def get_by_message_id(self, message_id: UUID) -> dto.MaybeBitchMessage:
        raise NotImplementedError

    async def get_maybe_bitches_messages(self) -> list[dto.MaybeBitchMessage]:
        raise NotImplementedError

    async def get_maybe_bitches_messages_count(self) -> int:
        raise NotImplementedError


class MaybeBitchMessageRepo(Protocol):
    async def add_maybe_bitch_message(
        self, maybe_bitch_message: entities.MaybeBitchMessage
    ) -> None:
        raise NotImplementedError

    async def delete_by_id(
        self,
        maybe_bitch_message_id: UUID,
    ) -> None:
        raise NotImplementedError
