from uuid import UUID

from sqlalchemy import delete, func, select
from sqlalchemy.exc import IntegrityError
from src.application.ban_pattern import dto
from src.application.ban_pattern.exceptions import (
    BanPatternIdAlreadyExists,
    BanPatternIdNotExist,
)
from src.application.ban_pattern.interfaces import BanPatternReader, BanPatternRepo
from src.domain.ban_pattern import entities
from src.infrastructure.db import models
from src.infrastructure.db.exception_mapper import exception_mapper
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class BanPatternReaderImpl(SQLAlchemyRepo, BanPatternReader):
    @exception_mapper
    async def get_by_id(self, ban_pattern_id: UUID) -> dto.BanPattern:
        ban_pattern = await self._session.scalar(
            select(models.BanPattern).where(
                models.BanPattern.id == ban_pattern_id,
            )
        )
        if ban_pattern is None:
            raise BanPatternIdNotExist(ban_pattern_id)

        return self._mapper.load(ban_pattern, dto.BanPattern)

    @exception_mapper
    async def get_ban_patterns(self) -> list[dto.BanPattern]:
        result = await self._session.scalars(select(models.BanPattern))
        ban_patterns = result.all()

        return self._mapper.load(ban_patterns, list[dto.BanPattern])

    @exception_mapper
    async def get_ban_patterns_count(self) -> int:
        return await self._session.scalar(select(func.count(models.BanPattern.id))) or 0


class BanPatternRepoImpl(SQLAlchemyRepo, BanPatternRepo):
    @exception_mapper
    async def add_ban_pattern(self, ban_pattern: entities.BanPattern) -> None:
        ban_pattern_model = self._mapper.load(ban_pattern, models.BanPattern)
        self._session.add(ban_pattern_model)

        try:
            await self._session.flush((ban_pattern_model,))
        except IntegrityError as err:
            raise BanPatternIdAlreadyExists(ban_pattern.id) from err

    @exception_mapper
    async def delete_by_id(self, ban_pattern_id: UUID) -> None:
        await self._session.execute(
            delete(models.BanPattern).where(models.BanPattern.id == ban_pattern_id)
        )

        return None
