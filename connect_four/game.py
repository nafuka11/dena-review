from connect_four import const
from connect_four.board import Board
from connect_four.cell import CellState


class ConnectFour:
    def __init__(self) -> None:
        self.board = Board(const.BOARD_SIZE)

    def put_player_cell(self, x: int) -> None:
        self.board.put_cell(x, CellState.PLAYER)

    def put_opponent_cell(self, x: int) -> None:
        self.board.put_cell(x, CellState.OPPONENT)
