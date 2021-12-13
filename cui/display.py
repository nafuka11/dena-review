from logic.board import Board
from logic.cell import CellState

CELL_CHARACTER = {CellState.PLAYER: "o", CellState.OPPONENT: "x", CellState.EMPTY: "."}

PLAYER_NAME = {True: "Player1", False: "Player2"}

ESC_CLEAR_SCREEN = "\033[2J"


def display_board(board: Board) -> None:
    print(ESC_CLEAR_SCREEN)
    for y in range(board.size.y):
        for x in range(board.size.x):
            _display_cell(board.cells[y][x])
        print()
    print("".join([str(x) for x in range(0, board.size.x)]))


def _display_cell(cell: CellState) -> None:
    print(CELL_CHARACTER[cell], end="")


def display_turn_info(is_player_turn: bool) -> None:
    print()
    print(f"TURN: {PLAYER_NAME[is_player_turn]}", end="")
    if is_player_turn:
        print(f"({CELL_CHARACTER[CellState.PLAYER]})")
    else:
        print(f"({CELL_CHARACTER[CellState.OPPONENT]})")


def display_input_message(min_value: int, max_value: int) -> None:
    print(f"Please input index({min_value}-{max_value}): ", end="")


def display_winner_message(is_player_turn: bool) -> None:
    print()
    print(f"{PLAYER_NAME[is_player_turn]} wins!")
