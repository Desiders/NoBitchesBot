import logging

from pyrogram.client import Client

from src.infrastructure.config_loader import load_config_from_env
from src.infrastructure.log.main import configure_logging

logger = logging.getLogger(__name__)


def main():
    config = load_config_from_env()

    configure_logging(config.logging)

    logging.getLogger("pyrogram").setLevel(max(logging.WARNING, logging.root.level))

    client = Client(
        name=config.bot.session_name,
        api_id=config.bot.api_id,
        api_hash=config.bot.api_hash,
        lang_code=config.bot.lang_code,  # type: ignore
        phone_number=config.bot.phone_number,  # type: ignore
        password=config.bot.password,  # type: ignore
        workdir=config.bot.workdir,  # type: ignore
    )

    logger.info("Bot starting...")
    client.run()
    logger.warning("Bot stopped")


main()
