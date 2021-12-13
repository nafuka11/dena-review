from enum import Enum, auto


class CellState(Enum):
    PLAYER = auto()
    OPPONENT = auto()
    EMPTY = auto()
