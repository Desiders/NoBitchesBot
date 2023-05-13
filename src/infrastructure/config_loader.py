import os
from pathlib import Path

from src.bot.config import Bot as BotConfig
from src.bot.config import Config

from .db.config import Config as DatabaseConfig
from .log.config import Config as LoggingConfig


def load_config_from_env() -> Config:
    """
    Load config from environment variables

    :raises ValueError: if bot api id or bot api hash isn't set
    :return: Config
    """
    api_id: str | int | None = os.getenv("BOT_API_ID")
    if not api_id:
        raise ValueError("Bot api id isn't set")

    api_hash = os.getenv("BOT_API_HASH")
    if not api_hash:
        raise ValueError("Bot api hash isn't set")

    bot = BotConfig(
        api_id=int(api_id),
        api_hash=api_hash,
        session_name=os.getenv("BOT_SESSION_NAME") or "no_bitches",
        lang_code=os.getenv("BOT_LANG_CODE") or "en",
        phone_number=os.getenv("BOT_PHONE_NUMBER"),
        password=os.getenv("BOT_PASSWORD"),
        workdir=os.getenv("BOT_WORKDIR"),
    )

    port: str | int | None = os.getenv("POSTGRES_PORT")
    if not port:
        port = 5432

    database = DatabaseConfig(
        host=os.getenv("POSTGRES_HOST") or "localhost",
        port=int(port),
        user=os.getenv("POSTGRES_USER") or "",
        password=os.getenv("POSTGRES_PASSWORD") or "",
        database=os.getenv("POSTGRES_DB") or "",
    )

    path: Path | str | None = os.getenv("LOGGING_PATH")
    if path:
        path = Path(path)
    else:
        path = None

    logging = LoggingConfig(
        render_json_logs=bool(os.getenv("LOGGING_RENDER_JSON_LOGS")),
        path=path,
        level=os.getenv("LOGGING_LEVEL") or "DEBUG",
    )

    return Config(
        bot=bot,
        database=database,
        logging=logging,
    )
