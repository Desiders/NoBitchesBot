import logging
from dataclasses import dataclass
from uuid import UUID

from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.application.user import dto
from src.application.user.interfaces import UserRepo
from src.domain.user import entities

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class CreateUser(Command[dto.User]):
    id: UUID
    tg_id: int
    first_name: str
    last_name: str | None = None
    username: str | None = None
    about: str | None = None


class CreateUserHandler(CommandHandler[CreateUser, dto.User]):
    def __init__(self, user_repo: UserRepo, uow: UnitOfWork, mapper: Mapper) -> None:
        self._user_repo = user_repo
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, command: CreateUser) -> dto.User:
        user = entities.User(
            command.id,
            command.tg_id,
            command.first_name,
            command.last_name,
            command.username,
            command.about,
        )

        await self._user_repo.add_user(user)
        await self._uow.commit()

        logger.info("User created", extra={"user": user})

        user_dto = self._mapper.load(user, dto.User)
        return user_dto
