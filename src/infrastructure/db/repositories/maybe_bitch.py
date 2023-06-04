from uuid import UUID

from sqlalchemy import delete, func, select
from sqlalchemy.exc import IntegrityError
from src.application.maybe_bitch import dto
from src.application.maybe_bitch.exceptions import (
    MaybeBitchIdAlreadyExists,
    MaybeBitchIdNotExist,
    MaybeBitchUserIdNotExist,
)
from src.application.maybe_bitch.interfaces import MaybeBitchReader, MaybeBitchRepo
from src.domain.maybe_bitch import entities
from src.infrastructure.db import models
from src.infrastructure.db.exception_mapper import exception_mapper
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class MaybeBitchReaderImpl(SQLAlchemyRepo, MaybeBitchReader):
    @exception_mapper
    async def get_by_id(self, maybe_bitch_id: UUID) -> dto.MaybeBitch:
        maybe_bitch = await self._session.scalar(
            select(models.MaybeBitch).where(
                models.MaybeBitch.id == maybe_bitch_id,
            )
        )
        if maybe_bitch is None:
            raise MaybeBitchIdNotExist(maybe_bitch_id)

        return self._mapper.load(maybe_bitch, dto.MaybeBitch)

    @exception_mapper
    async def get_by_user_id(self, user_id: UUID) -> dto.MaybeBitch:
        maybe_bitch = await self._session.scalar(
            select(models.MaybeBitch).where(
                models.MaybeBitch.user_id == user_id,
            )
        )
        if maybe_bitch is None:
            raise MaybeBitchUserIdNotExist(user_id)

        return self._mapper.load(maybe_bitch, dto.MaybeBitch)

    @exception_mapper
    async def get_maybe_bitches(self) -> list[dto.MaybeBitch]:
        result = await self._session.scalars(select(models.MaybeBitch))
        maybe_bitches = result.all()

        return self._mapper.load(maybe_bitches, list[dto.MaybeBitch])

    @exception_mapper
    async def get_maybe_bitches_count(self) -> int:
        return await self._session.scalar(select(func.count(models.MaybeBitch.id))) or 0


class MaybeBitchRepoImpl(SQLAlchemyRepo, MaybeBitchRepo):
    @exception_mapper
    async def add_maybe_bitch(self, maybe_bitch: entities.MaybeBitch) -> None:
        maybe_bitch_model = self._mapper.load(maybe_bitch, models.MaybeBitch)
        self._session.add(maybe_bitch_model)

        try:
            await self._session.flush((maybe_bitch_model,))
        except IntegrityError as err:
            raise MaybeBitchIdAlreadyExists(maybe_bitch.id) from err

    @exception_mapper
    async def delete_by_id(
        self,
        maybe_bitch_id: UUID,
    ) -> None:
        await self._session.execute(
            delete(models.MaybeBitch).where(models.MaybeBitch.id == maybe_bitch_id)
        )

        return None
