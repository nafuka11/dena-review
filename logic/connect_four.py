from logic import const
from logic.board import Board
from logic.cell import CellState
from logic.point import Point


class ConnectFour:
    def __init__(self) -> None:
        self.board = Board(const.BOARD_SIZE, const.CONNECT_LENGTH)

    def put_player_cell(self, x: int) -> None:
        self.board.put_cell(x, CellState.PLAYER)

    def put_opponent_cell(self, x: int) -> None:
        self.board.put_cell(x, CellState.OPPONENT)

    def can_put_cell(self, x: int) -> bool:
        if not self._is_valid_range_x(x):
            return False
        if self.board.can_put_cell(Point(x, 0)):
            return True
        return False

    def is_connected(self, x: int) -> bool:
        filled_y = [
            y
            for y in reversed(range(self.board.size.y))
            if not self.board.can_put_cell(Point(x, y))
        ]
        if not filled_y:
            return False
        y = min(filled_y)
        if self.board.is_connected(Point(x, y)):
            return True
        return False


    def _is_valid_range_x(self, x: int) -> bool:
        if 0 <= x < self.board.size.x:
            return True
        return False
