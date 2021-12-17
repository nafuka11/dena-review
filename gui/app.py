import tkinter as tk
from tkinter import ttk

from logic import CellState, ConnectFour, Point

CELL_SIZE = Point(40, 40)
CELL_PADDING_SIZE = Point(5, 5)
HEADER_HEIGHT = 20
FOOTER_HEIGHT = 40


class Application(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.create_widgets()

    def create_widgets(self) -> None:
        game = ConnectFour()
        window_size = Point(
            CELL_SIZE.x * game.size.x,
            CELL_SIZE.y * game.size.y + HEADER_HEIGHT + FOOTER_HEIGHT,
        )
        self.minsize(width=window_size.x, height=window_size.y)
        self.maxsize(width=window_size.x, height=window_size.y)

        self.title("Connect four")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.container = ContainerFrame(self, window_size, game)


class ContainerFrame(ttk.Frame):
    PLAYER_NAME = {True: "Red", False: "Yellow"}

    def __init__(self, master: tk.Tk, window_size: Point, game: ConnectFour) -> None:
        super().__init__(master)
        self.window_size = window_size
        self.game = game
        self.init_game()
        self.create_widgets()

    def init_game(self) -> None:
        self.game_end = False
        self.is_player_turn = True
        self.turn = 1
        self.game = ConnectFour()

    def reset_game(self) -> None:
        self.init_game()
        self.redraw_header()
        self.redraw_board()
        self.master.update()

    def create_widgets(self) -> None:
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(column=0, row=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.create_header()
        self.create_board()
        self.create_reset_button()

    def create_header(self) -> None:
        size = Point(self.window_size.x, HEADER_HEIGHT)
        self.header = HeaderFrame(
            self, size, self.turn, self.PLAYER_NAME[self.is_player_turn]
        )
        self.header.grid(row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def create_board(self) -> None:
        self.board = BoardFrame(self, self.game)
        self.board.canvas.bind("<Button-1>", self.handle_click_event)
        self.board.grid(row=1)

    def create_reset_button(self) -> None:
        self.reset_button = ttk.Button(self, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=2)
        self.rowconfigure(2, weight=1)

    def redraw_header(self) -> None:
        self.header.update_widgets(self.turn, self.PLAYER_NAME[self.is_player_turn])

    def redraw_board(self) -> None:
        self.board.redraw_widgets(self.game)

    def handle_click_event(self, event: tk.Event) -> None:
        if self.game_end:
            return
        x = event.x // CELL_SIZE.x
        if not self.game.can_put_cell(x):
            return
        self.put_cell(x)

    def put_cell(self, x: int) -> None:
        if self.is_player_turn:
            pos = self.game.put_player_cell(x)
        else:
            pos = self.game.put_opponent_cell(x)
        self.board.draw_cell(pos, self.game, False)
        self.judge_win_or_draw(x)
        if not self.game_end:
            self.proceed_next_turn()

    def judge_win_or_draw(self, x: int) -> None:
        if self.game.judge_win(x):
            self.board.display_win_message(self.PLAYER_NAME[self.is_player_turn])
            self.game_end = True
        elif self.game.judge_draw():
            self.board.display_draw_message()
            self.game_end = True

    def proceed_next_turn(self) -> None:
        self.is_player_turn = not self.is_player_turn
        self.turn += 1
        self.redraw_header()


class HeaderFrame(ttk.Frame):
    def __init__(
        self, master: ContainerFrame, size: Point, turn: int, player: str
    ) -> None:
        super().__init__(master, width=size.x, height=size.y)
        self._create_widgets(turn, player)

    def _create_widgets(self, turn: int, player: str) -> None:
        self.turn_label = ttk.Label(self)
        self.turn_label.place(relx=0.2, rely=0)

        self.player_label = ttk.Label(self)
        self.player_label.place(relx=0.6, rely=0)

        self.update_widgets(turn, player)

    def update_widgets(self, turn: int, player: str) -> None:
        self.turn_label.config(text=f"Turn: {turn}")
        self.player_label.config(text=f"Player: {player}")


class BoardFrame(ttk.Frame):
    TAG_CELL = "cell"
    TAG_MESSAGE = "message"

    COLOR_BACKGROUND = "#286FCD"
    COLOR_CELL = {
        CellState.EMPTY: "#1A48A2",
        CellState.PLAYER: "#DB3548",
        CellState.OPPONENT: "#FAD138",
    }
    COLOR_MESSAGE = "#FFFFFF"
    FONT_MESSAGE = ("", 42, "bold")

    def __init__(self, master: ContainerFrame, game: ConnectFour) -> None:
        super().__init__(master)
        self._create_widgets(game)

    def _create_widgets(self, game: ConnectFour) -> None:
        self.canvas = tk.Canvas(
            self, background=self.COLOR_BACKGROUND, highlightthickness=0
        )
        self.draw_cells(game)
        self.canvas.config(
            width=CELL_SIZE.x * game.size.x,
            height=CELL_SIZE.y * game.size.y,
        )
        self.canvas.grid(row=1)

    def redraw_widgets(self, game: ConnectFour) -> None:
        self.canvas.delete(self.TAG_CELL, self.TAG_MESSAGE)
        self.draw_cells(game)

    def draw_cells(self, game: ConnectFour) -> None:
        need_create = len(self.canvas.find_withtag(self.TAG_CELL)) == 0
        for y in range(game.size.y):
            for x in range(game.size.x):
                self.draw_cell(Point(x, y), game, need_create)

    def draw_cell(self, pos: Point, game: ConnectFour, need_create: bool) -> None:
        start_x = CELL_SIZE.x * pos.x + CELL_PADDING_SIZE.x
        start_y = CELL_SIZE.y * pos.y + CELL_PADDING_SIZE.y
        end_x = CELL_SIZE.x * (pos.x + 1) - CELL_PADDING_SIZE.x
        end_y = CELL_SIZE.y * (pos.y + 1) - CELL_PADDING_SIZE.y
        cell = game.get_cell(pos.x, pos.y)
        if need_create:
            self.canvas.create_oval(
                start_x,
                start_y,
                end_x,
                end_y,
                fill=self.COLOR_CELL[cell],
                tags=(self.TAG_CELL, f"{pos.x}-{pos.y}"),
            )
        else:
            oval = self.canvas.find_withtag(f"{pos.x}-{pos.y}")
            self.canvas.itemconfig(oval, fill=self.COLOR_CELL[cell])

    def display_win_message(self, winner: str) -> None:
        self._display_message(f"{winner} wins!")

    def display_draw_message(self) -> None:
        self._display_message("Draw!")

    def _display_message(self, message: str) -> None:
        pos_x = self.canvas.winfo_width() // 2
        pos_y = self.canvas.winfo_height() // 2
        self.canvas.create_text(
            pos_x,
            pos_y,
            text=message,
            font=self.FONT_MESSAGE,
            fill=self.COLOR_MESSAGE,
            tags=self.TAG_MESSAGE,
        )
