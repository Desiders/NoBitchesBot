from dataclasses import dataclass

from src.infrastructure.db.config import Config as DatabaseConfig
from src.infrastructure.log.config import Config as LoggingConfig


@dataclass
class Bot:
    api_id: int
    api_hash: str
    session_name: str
    lang_code: None | str = None
    phone_number: None | str = None
    password: None | str = None
    workdir: None | str = None


@dataclass
class Config:
    bot: Bot
    database: DatabaseConfig
    logging: LoggingConfig
