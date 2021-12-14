from logic.board import Board
from logic.cell import CellState

CELL_CHARACTER = {CellState.PLAYER: "O", CellState.OPPONENT: "X", CellState.EMPTY: "."}

PLAYER_NAME = {True: "Player1", False: "Player2"}

ESC_CLEAR_SCREEN = "\033[2J"
ESC_CURSOR_UP = "\033[1A"
ESC_CLEAR_LINE = "\033[2K"


def display_board(board: Board) -> None:
    _clear_screen()
    print("+" + "-" * (board.size.x * 2 - 1) + "+")
    for y in range(board.size.y):
        print("|", end="")
        print(
            " ".join([CELL_CHARACTER[board.cells[y][x]] for x in range(board.size.x)]),
            end="",
        )
        print("|", end="")
        print()
    print("+" + "-" * (board.size.x * 2 - 1) + "+")
    print(" " + " ".join([str(x) for x in range(1, board.size.x + 1)]))


def display_turn_info(is_player_turn: bool) -> None:
    print()
    print(f"TURN: {PLAYER_NAME[is_player_turn]}", end="")
    if is_player_turn:
        print(f"({CELL_CHARACTER[CellState.PLAYER]})")
    else:
        print(f"({CELL_CHARACTER[CellState.OPPONENT]})")


def display_input_message(min_value: int, max_value: int) -> None:
    _clear_line()
    print(f"Please input index({min_value}-{max_value}): ", end="")


def display_winner_message(is_player_turn: bool) -> None:
    print()
    print(f"{PLAYER_NAME[is_player_turn]} wins!")


def display_draw_message() -> None:
    print()
    print("Draw!")


def _clear_screen() -> None:
    print(ESC_CLEAR_SCREEN)


def _clear_line() -> None:
    print(f"{ESC_CURSOR_UP}{ESC_CLEAR_LINE}", end="")
