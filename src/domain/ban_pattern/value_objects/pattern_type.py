from enum import Enum

from src.domain.common.value_objects.base import ValueObject


class PatternType(ValueObject, Enum):
    # Check if text of the message matches regex pattern
    TEXT_MESSAGE_REGEX = 1
    # Check if text of the message equals to pattern
    TEXT_MESSAG_EQUALS = 2
    # Check if text of the message contains pattern
    IN_TEXT_MESSAG = 3
    # Check if about profile matches regex pattern
    ABOUT_PROFILE_REGEX = 4
    # Check if about profile equals to pattern
    ABOUT_PROFILE_EQUALS = 5
    # Check if about profile contains pattern
    IN_ABOUT_PROFILE = 6
