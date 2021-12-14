from typing import List

import pytest

from logic.cell import CellState
from logic.connect_four import ConnectFour


class TestConnectFour:
    CELL_CHARACTER = {
        "O": CellState.PLAYER,
        "X": CellState.OPPONENT,
        ".": CellState.EMPTY,
    }

    def generate_cells_from_lines(self, lines: List[str]) -> List[List[CellState]]:
        cells = []
        for line in lines:
            cells.append([self.CELL_CHARACTER[cell] for cell in line])
        return cells

    def test_put_player_cell(self) -> None:
        connect_four = ConnectFour()
        connect_four.put_player_cell(0)
        board_str = [
            ".......",
            ".......",
            ".......",
            ".......",
            ".......",
            "O......",
        ]
        expected = self.generate_cells_from_lines(board_str)
        assert connect_four.board.cells == expected

    def test_put_opponent_cell(self) -> None:
        connect_four = ConnectFour()
        connect_four.put_opponent_cell(0)
        board_str = [
            ".......",
            ".......",
            ".......",
            ".......",
            ".......",
            "X......",
        ]
        expected = self.generate_cells_from_lines(board_str)
        assert connect_four.board.cells == expected

    @pytest.mark.parametrize("x", [0, 1, 2, 3, 4, 5, 6])
    def test_can_put_cell_valid_range(self, x: int) -> None:
        connect_four = ConnectFour()
        assert connect_four.can_put_cell(x)

    @pytest.mark.parametrize(
        "x, expected",
        [
            (0, False),
            (1, True),
            (2, True),
            (3, True),
            (4, True),
            (5, True),
            (6, True),
        ],
    )
    def test_can_put_cell_filled_row(self, x: int, expected: bool) -> None:
        connect_four = ConnectFour()
        board_str = [
            "O......",
            "XO.....",
            "OXX....",
            "XOOX...",
            "OXXOO..",
            "XOOXXO.",
        ]
        connect_four.board.cells = self.generate_cells_from_lines(board_str)
        assert connect_four.can_put_cell(x) == expected

    @pytest.mark.parametrize("x", [-1, 7])
    def test_can_put_cell_invalid_range(self, x: int) -> None:
        connect_four = ConnectFour()
        assert not connect_four.can_put_cell(x)

    @pytest.mark.parametrize(
        "x, expected",
        [
            (0, True),
            (1, True),
            (2, True),
            (3, True),
            (4, False),
            (5, False),
            (6, False),
        ],
    )
    def test_is_connected_horizontal(self, x: int, expected: bool) -> None:
        connect_four = ConnectFour()
        board_str = [
            ".......",
            ".......",
            ".......",
            ".......",
            ".......",
            "OOOO...",
        ]
        connect_four.board.cells = self.generate_cells_from_lines(board_str)
        assert connect_four.is_connected(x) == expected

    @pytest.mark.parametrize(
        "x, expected",
        [
            (0, True),
            (1, False),
            (2, False),
            (3, False),
            (4, False),
            (5, False),
            (6, False),
        ],
    )
    def test_is_connected_vertical(self, x: int, expected: bool) -> None:
        connect_four = ConnectFour()
        board_str = [
            ".......",
            ".......",
            "O......",
            "O......",
            "O......",
            "O......",
        ]
        connect_four.board.cells = self.generate_cells_from_lines(board_str)
        assert connect_four.is_connected(x) == expected

    @pytest.mark.parametrize(
        "x, expected",
        [
            (0, True),
            (1, True),
            (2, True),
            (3, True),
            (4, False),
            (5, False),
            (6, False),
        ],
    )
    def test_is_connected_right_diagonal(self, x: int, expected: bool) -> None:
        connect_four = ConnectFour()
        board_str = [
            ".......",
            ".......",
            "...O...",
            "..O....",
            ".O.....",
            "O......",
        ]
        connect_four.board.cells = self.generate_cells_from_lines(board_str)
        assert connect_four.is_connected(x) == expected

    @pytest.mark.parametrize(
        "x, expected",
        [
            (0, False),
            (1, False),
            (2, False),
            (3, True),
            (4, True),
            (5, True),
            (6, True),
        ],
    )
    def test_is_connected_left_diagonal(self, x: int, expected: bool) -> None:
        connect_four = ConnectFour()
        board_str = [
            ".......",
            ".......",
            "...O...",
            "....O..",
            ".....O.",
            "......O",
        ]
        connect_four.board.cells = self.generate_cells_from_lines(board_str)
        assert connect_four.is_connected(x) == expected

    @pytest.mark.parametrize("x", [0, 1, 2, 3, 4, 5, 6])
    def test_is_connected_false_horizontal(self, x: int) -> None:
        connect_four = ConnectFour()
        board_str = [
            ".......",
            ".......",
            ".......",
            ".......",
            ".......",
            "XXX....",
        ]
        connect_four.board.cells = self.generate_cells_from_lines(board_str)
        assert not connect_four.is_connected(x)

    @pytest.mark.parametrize("x", [0, 1, 2, 3, 4, 5, 6])
    def test_is_connected_false_vertical(self, x: int) -> None:
        connect_four = ConnectFour()
        board_str = [
            ".......",
            ".......",
            ".......",
            "X......",
            "X......",
            "X......",
        ]
        connect_four.board.cells = self.generate_cells_from_lines(board_str)
        assert not connect_four.is_connected(x)

    @pytest.mark.parametrize("x", [0, 1, 2, 3, 4, 5, 6])
    def test_is_connected_false_right_diagonal(self, x: int) -> None:
        connect_four = ConnectFour()
        board_str = [
            ".......",
            ".......",
            ".......",
            "..X....",
            ".X.....",
            "X......",
        ]
        connect_four.board.cells = self.generate_cells_from_lines(board_str)
        assert not connect_four.is_connected(x)

    @pytest.mark.parametrize("x", [0, 1, 2, 3, 4, 5, 6])
    def test_is_connected_false_left_diagonal(self, x: int) -> None:
        connect_four = ConnectFour()
        board_str = [
            ".......",
            ".......",
            ".......",
            "....X..",
            ".....X.",
            "......X",
        ]
        connect_four.board.cells = self.generate_cells_from_lines(board_str)
        assert not connect_four.is_connected(x)
