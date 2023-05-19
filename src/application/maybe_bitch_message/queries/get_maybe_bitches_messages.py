import logging
from dataclasses import dataclass

from src.application.common.query import Query, QueryHandler
from src.application.maybe_bitch_message import dto
from src.application.maybe_bitch_message.interfaces import MaybeBitchMessageReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetMaybeBitchesMessages(Query[list[dto.MaybeBitchMessage]]):
    pass


class GetMaybeBitchesMessagesHandler(
    QueryHandler[GetMaybeBitchesMessages, list[dto.MaybeBitchMessage]]
):
    def __init__(self, maybe_bitch_message_reader: MaybeBitchMessageReader) -> None:
        self._maybe_bitch_message_reader = maybe_bitch_message_reader

    async def __call__(
        self, query: GetMaybeBitchesMessages
    ) -> list[dto.MaybeBitchMessage]:
        maybe_bitches_messages = (
            await self._maybe_bitch_message_reader.get_maybe_bitches_messages()
        )
        logger.debug(
            "Get maybe bitches messages",
            extra={
                "maybe_bitches_messages": maybe_bitches_messages,
            },
        )
        return maybe_bitches_messages
