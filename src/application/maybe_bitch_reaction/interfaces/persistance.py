from typing import Protocol
from uuid import UUID

from src.application.maybe_bitch_reaction import dto
from src.domain.maybe_bitch_reaction import entities


class MaybeBitchReactionReader(Protocol):
    async def get_by_id(self, maybe_bitch_reaction_id: UUID) -> dto.MaybeBitchReaction:
        raise NotImplementedError

    async def get_by_maybe_bitch_id(
        self, maybe_bitch_id: UUID
    ) -> dto.MaybeBitchReaction:
        raise NotImplementedError

    async def get_by_message_id(self, message_id: UUID) -> list[dto.MaybeBitchReaction]:
        raise NotImplementedError

    async def get_maybe_bitches_reactions(self) -> list[dto.MaybeBitchReaction]:
        raise NotImplementedError

    async def get_maybe_bitches_reactions_count(self) -> int:
        raise NotImplementedError


class MaybeBitchReactionRepo(Protocol):
    async def add_maybe_bitch_reaction(
        self, maybe_bitch_reaction: entities.MaybeBitchReaction
    ) -> None:
        raise NotImplementedError

    async def delete_by_id(
        self,
        maybe_bitch_reaction_id: UUID,
    ) -> None:
        raise NotImplementedError
