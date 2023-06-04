from typing import NoReturn
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.exc import DBAPIError, IntegrityError
from src.application.common.exceptions import RepoError
from src.application.user import dto
from src.application.user.exceptions import (
    UserIdAlreadyExists,
    UserIdNotExist,
    UserTgIdAlreadyExists,
    UserTgIdNotExist,
)
from src.application.user.interfaces import UserReader, UserRepo
from src.domain.user import entities
from src.infrastructure.db import models
from src.infrastructure.db.exception_mapper import exception_mapper
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class UserReaderImpl(SQLAlchemyRepo, UserReader):
    @exception_mapper
    async def get_by_id(self, user_id: UUID) -> dto.User:
        user = await self._session.scalar(
            select(models.User).where(
                models.User.id == user_id,
            )
        )
        if user is None:
            raise UserIdNotExist(user_id)

        return self._mapper.load(user, dto.User)

    @exception_mapper
    async def get_by_tg_id(self, tg_id: int) -> dto.User:
        user = await self._session.scalar(
            select(models.User).where(
                models.User.tg_id == tg_id,
            )
        )
        if user is None:
            raise UserTgIdNotExist(tg_id)

        return self._mapper.load(user, dto.User)

    @exception_mapper
    async def get_users(self) -> list[dto.User]:
        result = await self._session.scalars(select(models.User))
        users = result.all()

        return self._mapper.load(users, list[dto.User])

    @exception_mapper
    async def get_users_count(self) -> int:
        return await self._session.scalar(select(func.count(models.User.id))) or 0


class UserRepoImpl(SQLAlchemyRepo, UserRepo):
    @exception_mapper
    async def add_user(self, user: entities.User) -> None:
        user_model = self._mapper.load(user, models.User)
        self._session.add(user_model)

        try:
            await self._session.flush((user_model,))
        except IntegrityError as err:
            self._parse_error(err, user)

    def _parse_error(self, err: DBAPIError, user: entities.User) -> NoReturn:
        match err.__cause__.__cause__.constraint_name:  # type: ignore
            case "pk_users":
                raise UserIdAlreadyExists(user.id) from err
            case "uq_users_tg_id":
                raise UserTgIdAlreadyExists(user.tg_id) from err
            case _:
                raise RepoError from err
