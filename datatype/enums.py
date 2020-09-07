from enum import IntEnum


class DartMultiplier(IntEnum):
    MISS = 0
    SINGLE = 1
    DOUBLE = 2
    TREBLE = 3


class MatchStatus(IntEnum):
    INVALID = 0
    WAITING = 1
    IN_PROGRESS = 2
    FINISHED = 3
