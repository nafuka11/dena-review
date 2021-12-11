from connect_four.cell import CellState
from connect_four.point import Point


class Board:
    def __init__(self, size: Point) -> None:
        self.size = size
        self.init_cells()

    def init_cells(self) -> None:
        self.cells = [[CellState.EMPTY] * self.size.x for _ in range(self.size.y)]

    def put_cell(self, x: int, cell: CellState) -> None:
        for y in reversed(range(self.size.y)):
            if self.cells[y][x] == CellState.EMPTY:
                self.cells[y][x] = cell
                return
