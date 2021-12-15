from logic.cell import CellState
from logic.point import Point


class Board:
    def __init__(self, size: Point, connect_length: int) -> None:
        self.size = size
        self.connect_length = connect_length
        self.init_cells()

    def init_cells(self) -> None:
        self.cells = [[CellState.EMPTY] * self.size.x for _ in range(self.size.y)]

    def put_cell(self, x: int, cell: CellState) -> int:
        for y in reversed(range(self.size.y)):
            if self.can_put_cell(Point(x, y)):
                self.cells[y][x] = cell
                return Point(x, y)
        return Point(-1, -1)

    def can_put_cell(self, pos: Point) -> bool:
        if self.cells[pos.y][pos.x] == CellState.EMPTY:
            return True
        return False

    def is_connected(self, pos: Point) -> bool:
        if self._is_connected_vertical(pos):
            return True
        if self._is_connected_horizontal(pos):
            return True
        if self._is_connected_right_diagonal(pos):
            return True
        if self._is_connected_left_diagonal(pos):
            return True
        return False

    def has_any_empty_cell(self) -> bool:
        for y in range(self.size.y):
            can_put_cell = any(
                [self.can_put_cell(Point(x, y)) for x in range(self.size.x)]
            )
            if can_put_cell:
                return True
        return False

    def _is_connected_vertical(self, pos: Point) -> bool:
        return self._is_connected_line(pos, Point(0, 1))

    def _is_connected_horizontal(self, pos: Point) -> bool:
        return self._is_connected_line(pos, Point(1, 0))

    def _is_connected_right_diagonal(self, pos: Point) -> bool:
        return self._is_connected_line(pos, Point(-1, 1))

    def _is_connected_left_diagonal(self, pos: Point) -> bool:
        return self._is_connected_line(pos, Point(1, 1))

    def _is_connected_line(self, pos: Point, delta: Point) -> bool:
        count = 1
        now_pos = Point(pos.x + delta.x, pos.y + delta.y)
        while 0 <= now_pos.x < self.size.x and 0 <= now_pos.y < self.size.y:
            if self.cells[now_pos.y][now_pos.x] != self.cells[pos.y][pos.x]:
                break
            count += 1
            now_pos.x += delta.x
            now_pos.y += delta.y
        now_pos = Point(pos.x - delta.x, pos.y - delta.y)
        while 0 <= now_pos.x < self.size.x and 0 <= now_pos.y < self.size.y:
            if self.cells[now_pos.y][now_pos.x] != self.cells[pos.y][pos.x]:
                break
            count += 1
            now_pos.x -= delta.x
            now_pos.y -= delta.y
        if count >= self.connect_length:
            return True
        return False
