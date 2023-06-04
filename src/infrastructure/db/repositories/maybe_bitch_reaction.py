from uuid import UUID

from sqlalchemy import delete, func, select
from sqlalchemy.exc import IntegrityError
from src.application.maybe_bitch_reaction import dto
from src.application.maybe_bitch_reaction.exceptions import (
    MaybeBitchReactionBitchIdNotExist,
    MaybeBitchReactionIdAlreadyExists,
    MaybeBitchReactionIdNotExist,
)
from src.application.maybe_bitch_reaction.interfaces import (
    MaybeBitchReactionReader,
    MaybeBitchReactionRepo,
)
from src.domain.maybe_bitch_reaction import entities
from src.infrastructure.db import models
from src.infrastructure.db.exception_mapper import exception_mapper
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class MaybeBitchReactionReaderImpl(SQLAlchemyRepo, MaybeBitchReactionReader):
    @exception_mapper
    async def get_by_id(self, maybe_bitch_reaction_id: UUID) -> dto.MaybeBitchReaction:
        maybe_bitch_reaction = await self._session.scalar(
            select(models.MaybeBitchReaction).where(
                models.MaybeBitchReaction.id == maybe_bitch_reaction_id,
            )
        )
        if maybe_bitch_reaction is None:
            raise MaybeBitchReactionIdNotExist(maybe_bitch_reaction_id)

        return self._mapper.load(maybe_bitch_reaction, dto.MaybeBitchReaction)

    @exception_mapper
    async def get_by_maybe_bitch_id(
        self, maybe_bitch_id: UUID
    ) -> dto.MaybeBitchReaction:
        maybe_bitch_reaction = await self._session.scalar(
            select(models.MaybeBitchReaction).where(
                models.MaybeBitchReaction.maybe_bitch_id == maybe_bitch_id,
            )
        )
        if maybe_bitch_reaction is None:
            raise MaybeBitchReactionBitchIdNotExist(maybe_bitch_id)

        return self._mapper.load(maybe_bitch_reaction, dto.MaybeBitchReaction)

    @exception_mapper
    async def get_by_message_id(self, message_id: UUID) -> list[dto.MaybeBitchReaction]:
        result = await self._session.scalars(
            select(models.MaybeBitchReaction).where(
                models.MaybeBitchReaction.message_id == message_id
            )
        )
        maybe_bitches_reactions = result.all()

        return self._mapper.load(maybe_bitches_reactions, list[dto.MaybeBitchReaction])

    @exception_mapper
    async def get_maybe_bitches_reactions(self) -> list[dto.MaybeBitchReaction]:
        result = await self._session.scalars(select(models.MaybeBitchReaction))
        maybe_bitches_reactions = result.all()

        return self._mapper.load(maybe_bitches_reactions, list[dto.MaybeBitchReaction])

    @exception_mapper
    async def get_maybe_bitches_reactions_count(self) -> int:
        return (
            await self._session.scalar(select(func.count(models.MaybeBitchReaction.id)))
            or 0
        )


class MaybeBitchReactionRepoImpl(SQLAlchemyRepo, MaybeBitchReactionRepo):
    @exception_mapper
    async def add_maybe_bitch_reaction(
        self, maybe_bitch_reaction: entities.MaybeBitchReaction
    ) -> None:
        maybe_bitch_reaction_model = self._mapper.load(
            maybe_bitch_reaction, models.MaybeBitchReaction
        )
        self._session.add(maybe_bitch_reaction_model)

        try:
            await self._session.flush((maybe_bitch_reaction_model,))
        except IntegrityError as err:
            raise MaybeBitchReactionIdAlreadyExists(maybe_bitch_reaction.id) from err

    @exception_mapper
    async def delete_by_id(
        self,
        maybe_bitch_reaction_id: UUID,
    ) -> None:
        await self._session.execute(
            delete(models.MaybeBitchReaction).where(
                models.MaybeBitchReaction.id == maybe_bitch_reaction_id
            )
        )

        return None
