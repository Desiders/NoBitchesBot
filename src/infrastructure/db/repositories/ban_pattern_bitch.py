from uuid import UUID

from sqlalchemy import delete, func, select
from sqlalchemy.exc import IntegrityError
from src.application.ban_pattern_bitch import dto
from src.application.ban_pattern_bitch.exceptions import (
    BanPatternBitchIdAlreadyExists,
    BanPatternBitchIdNotExist,
)
from src.application.ban_pattern_bitch.interfaces import (
    BanPatternBitchReader,
    BanPatternBitchRepo,
)
from src.domain.ban_pattern_bitch import entities
from src.infrastructure.db import models
from src.infrastructure.db.exception_mapper import exception_mapper
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class BanPatternBitchReaderImpl(SQLAlchemyRepo, BanPatternBitchReader):
    @exception_mapper
    async def get_by_id(self, ban_pattern_bitch_id: UUID) -> dto.BanPatternBitch:
        ban_pattern_bitch = await self._session.scalar(
            select(models.BanPatternBitch).where(
                models.BanPatternBitch.id == ban_pattern_bitch_id,
            )
        )
        if ban_pattern_bitch is None:
            raise BanPatternBitchIdNotExist(ban_pattern_bitch_id)

        return self._mapper.load(ban_pattern_bitch, dto.BanPatternBitch)

    @exception_mapper
    async def get_by_ban_pattern_id(
        self, ban_pattern_id: UUID
    ) -> list[dto.BanPatternBitch]:
        result = await self._session.scalars(
            select(models.BanPatternBitch).where(
                models.BanPatternBitch.ban_pattern_id == ban_pattern_id,
            )
        )
        ban_patterns_bitches = result.all()

        return self._mapper.load(ban_patterns_bitches, list[dto.BanPatternBitch])

    @exception_mapper
    async def get_by_bitch_id(self, bitch_id: UUID) -> list[dto.BanPatternBitch]:
        result = await self._session.scalars(
            select(models.BanPatternBitch).where(
                models.BanPatternBitch.bitch_id == bitch_id,
            )
        )
        ban_patterns_bitches = result.all()

        return self._mapper.load(ban_patterns_bitches, list[dto.BanPatternBitch])

    @exception_mapper
    async def get_ban_pattern_bitches(self) -> list[dto.BanPatternBitch]:
        result = await self._session.scalars(select(models.BanPatternBitch))
        ban_patterns_bitches = result.all()

        return self._mapper.load(ban_patterns_bitches, list[dto.BanPatternBitch])

    @exception_mapper
    async def get_ban_pattern_bitches_count(self) -> int:
        return (
            await self._session.scalar(select(func.count(models.BanPatternBitch.id)))
            or 0
        )


class BanPatternBitchRepoImpl(SQLAlchemyRepo, BanPatternBitchRepo):
    @exception_mapper
    async def add_ban_pattern_bitch(
        self, ban_pattern_bitch: entities.BanPatternBitch
    ) -> None:
        ban_pattern_bitch_model = self._mapper.load(
            ban_pattern_bitch, models.BanPatternBitch
        )
        self._session.add(ban_pattern_bitch_model)

        try:
            await self._session.flush((ban_pattern_bitch_model,))
        except IntegrityError as err:
            raise BanPatternBitchIdAlreadyExists(ban_pattern_bitch.id) from err

    @exception_mapper
    async def delete_by_id(
        self,
        ban_pattern_bitch_id: UUID,
    ) -> None:
        await self._session.execute(
            delete(models.BanPatternBitch).where(
                models.BanPatternBitch.id == ban_pattern_bitch_id
            )
        )

        return None
