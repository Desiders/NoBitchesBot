import logging
from dataclasses import dataclass

from src.application.common.query import Query, QueryHandler
from src.application.maybe_bitch_message.interfaces import MaybeBitchMessageReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetMaybeBitchesMessagesCount(Query[int]):
    pass


class GetMaybeBitchesMessagesCountHandler(
    QueryHandler[GetMaybeBitchesMessagesCount, int]
):
    def __init__(self, maybe_bitch_message_reader: MaybeBitchMessageReader) -> None:
        self._maybe_bitch_message_reader = maybe_bitch_message_reader

    async def __call__(self, query: GetMaybeBitchesMessagesCount) -> int:
        maybe_bitches_messages_count = (
            await self._maybe_bitch_message_reader.get_maybe_bitches_messages_count()
        )
        logger.debug(
            "Get maybe bitches messages count",
            extra={
                "maybe_bitches_messages_count": maybe_bitches_messages_count,
            },
        )
        return maybe_bitches_messages_count
