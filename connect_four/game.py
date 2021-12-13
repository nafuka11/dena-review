from connect_four import const
from connect_four.board import Board
from connect_four.cell import CellState
from connect_four.point import Point


class ConnectFour:
    def __init__(self) -> None:
        self.board = Board(const.BOARD_SIZE, const.CONNECT_LENGTH)

    def put_player_cell(self, x: int) -> None:
        self.board.put_cell(x, CellState.PLAYER)

    def put_opponent_cell(self, x: int) -> None:
        self.board.put_cell(x, CellState.OPPONENT)

    def can_put_cell(self, x: int) -> bool:
        if self.board.can_put_cell(Point(x, 0)):
            return True
        return False
