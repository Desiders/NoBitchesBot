from uuid import UUID

from sqlalchemy import delete, func, select
from sqlalchemy.exc import IntegrityError
from src.application.bitch import dto
from src.application.bitch.exceptions import (
    BitchIdAlreadyExists,
    BitchIdNotExist,
    BitchUserIdNotExist,
)
from src.application.bitch.interfaces import BitchReader, BitchRepo
from src.domain.bitch import entities
from src.infrastructure.db import models
from src.infrastructure.db.exception_mapper import exception_mapper
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class BitchReaderImpl(SQLAlchemyRepo, BitchReader):
    @exception_mapper
    async def get_by_id(self, bitch_id: UUID) -> dto.Bitch:
        bitch = await self._session.scalar(
            select(models.Bitch).where(
                models.Bitch.id == bitch_id,
            )
        )
        if bitch is None:
            raise BitchIdNotExist(bitch_id)

        return self._mapper.load(bitch, dto.Bitch)

    @exception_mapper
    async def get_by_user_id(self, user_id: UUID) -> dto.Bitch:
        bitch = await self._session.scalars(
            select(models.Bitch).where(
                models.Bitch.user_id == user_id,
            )
        )
        if bitch is None:
            raise BitchUserIdNotExist(user_id)

        return self._mapper.load(bitch, dto.Bitch)

    @exception_mapper
    async def get_bitches(self) -> list[dto.Bitch]:
        result = await self._session.scalars(select(models.Bitch))
        bitches = result.all()

        return self._mapper.load(bitches, list[dto.Bitch])

    @exception_mapper
    async def get_bitches_count(self) -> int:
        return await self._session.scalar(select(func.count(models.Bitch.id))) or 0


class BitchRepoImpl(SQLAlchemyRepo, BitchRepo):
    @exception_mapper
    async def add_bitch(self, bitch: entities.Bitch) -> None:
        bitch_model = self._mapper.load(bitch, models.Bitch)
        self._session.add(bitch_model)

        try:
            await self._session.flush((bitch_model,))
        except IntegrityError as err:
            raise BitchIdAlreadyExists(bitch.id) from err

    @exception_mapper
    async def delete_by_id(self, bitch_id: UUID) -> None:
        await self._session.execute(
            delete(models.Bitch).where(models.Bitch.id == bitch_id)
        )

        return None
