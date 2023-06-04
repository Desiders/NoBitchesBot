from uuid import UUID

from sqlalchemy import delete, func, select
from sqlalchemy.exc import IntegrityError
from src.application.maybe_bitch_message import dto
from src.application.maybe_bitch_message.exceptions import (
    MaybeBitchMessageBitchIdNotExist,
    MaybeBitchMessageIdAlreadyExists,
    MaybeBitchMessageIdNotExist,
)
from src.application.maybe_bitch_message.interfaces import (
    MaybeBitchMessageReader,
    MaybeBitchMessageRepo,
)
from src.domain.maybe_bitch_message import entities
from src.infrastructure.db import models
from src.infrastructure.db.exception_mapper import exception_mapper
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class MaybeBitchMessageReaderImpl(SQLAlchemyRepo, MaybeBitchMessageReader):
    @exception_mapper
    async def get_by_id(self, maybe_bitch_message_id: UUID) -> dto.MaybeBitchMessage:
        maybe_bitch_message = await self._session.scalar(
            select(models.MaybeBitchMessage).where(
                models.MaybeBitchMessage.id == maybe_bitch_message_id,
            )
        )
        if maybe_bitch_message is None:
            raise MaybeBitchMessageIdNotExist(maybe_bitch_message_id)

        return self._mapper.load(maybe_bitch_message, dto.MaybeBitchMessage)

    @exception_mapper
    async def get_by_maybe_bitch_id(
        self, maybe_bitch_id: UUID
    ) -> dto.MaybeBitchMessage:
        maybe_bitch_message = await self._session.scalar(
            select(models.MaybeBitchMessage).where(
                models.MaybeBitchMessage.maybe_bitch_id == maybe_bitch_id,
            )
        )
        if maybe_bitch_message is None:
            raise MaybeBitchMessageBitchIdNotExist(maybe_bitch_id)

        return self._mapper.load(maybe_bitch_message, dto.MaybeBitchMessage)

    @exception_mapper
    async def get_maybe_bitches_messages(self) -> list[dto.MaybeBitchMessage]:
        result = await self._session.scalars(select(models.MaybeBitchMessage))
        maybe_bitches_messages = result.all()

        return self._mapper.load(maybe_bitches_messages, list[dto.MaybeBitchMessage])

    @exception_mapper
    async def get_maybe_bitches_messages_count(self) -> int:
        return (
            await self._session.scalar(select(func.count(models.MaybeBitchMessage.id)))
            or 0
        )


class MaybeBitchMessageRepoImpl(SQLAlchemyRepo, MaybeBitchMessageRepo):
    @exception_mapper
    async def add_maybe_bitch_message(
        self, maybe_bitch_message: entities.MaybeBitchMessage
    ) -> None:
        maybe_bitch_message_model = self._mapper.load(
            maybe_bitch_message, models.MaybeBitchMessage
        )
        self._session.add(maybe_bitch_message_model)

        try:
            await self._session.flush((maybe_bitch_message_model,))
        except IntegrityError as err:
            raise MaybeBitchMessageIdAlreadyExists(maybe_bitch_message.id) from err

    @exception_mapper
    async def delete_by_id(
        self,
        maybe_bitch_message_id: UUID,
    ) -> None:
        await self._session.execute(
            delete(models.MaybeBitchMessage).where(
                models.MaybeBitchMessage.id == maybe_bitch_message_id
            )
        )

        return None
