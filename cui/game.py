from cui.display import (
    display_board,
    display_draw_message,
    display_input_message,
    display_turn_info,
    display_winner_message,
)
from logic.connect_four import ConnectFour


class CUIGame:
    def __init__(self) -> None:
        self.game = ConnectFour()
        self.is_player_turn = True

    def run(self) -> None:
        while True:
            x = self._process_turn()
            if self.game.judge_win(x):
                display_board(self.game.board)
                display_winner_message(self.is_player_turn)
                break
            if self.game.judge_draw():
                display_board(self.game.board)
                display_draw_message()
                break
            self.is_player_turn = not self.is_player_turn

    def _process_turn(self) -> int:
        display_board(self.game.board)
        display_turn_info(self.is_player_turn)
        x = self._process_user_input()
        self._put_cell(x)
        return x

    def _process_user_input(self) -> int:
        print()
        while True:
            display_input_message(1, self.game.board.size.x)
            try:
                x = int(input())
                if self.game.can_put_cell(x - 1):
                    return x - 1
            except ValueError:
                pass

    def _put_cell(self, x: int) -> None:
        if self.is_player_turn:
            self.game.put_player_cell(x)
        else:
            self.game.put_opponent_cell(x)
