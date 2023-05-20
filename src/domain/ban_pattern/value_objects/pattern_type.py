from enum import Enum

from src.domain.common.value_objects.base import ValueObject


class PatternType(ValueObject, Enum):
    REGEX = 1
    EQUALS = 2
    IN = 3
