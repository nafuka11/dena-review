from cui.display import (
    display_board,
    display_input_message,
    display_turn_info,
    display_winner_message,
)
from logic.connect_four import ConnectFour


class Game:
    def __init__(self) -> None:
        self.connect_four = ConnectFour()
        self.is_player_turn = True

    def run(self) -> None:
        while True:
            x = self._process_turn()
            if self.connect_four.is_connected(x):
                display_board(self.connect_four.board)
                display_winner_message(self.is_player_turn)
                break
            self.is_player_turn = not self.is_player_turn

    def _process_turn(self) -> int:
        display_board(self.connect_four.board)
        display_turn_info(self.is_player_turn)
        x = self._process_user_input()
        self._put_cell(x)
        return x

    def _process_user_input(self) -> int:
        print()
        while True:
            display_input_message(1, self.connect_four.board.size.x)
            try:
                x = int(input())
                if self.connect_four.can_put_cell(x - 1):
                    return x - 1
            except ValueError:
                pass

    def _put_cell(self, x: int) -> None:
        if self.is_player_turn:
            self.connect_four.put_player_cell(x)
        else:
            self.connect_four.put_opponent_cell(x)
