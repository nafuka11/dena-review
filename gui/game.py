import tkinter as tk

from gui.app import WINDOW_SIZE, Application


class GUIGame:
    def run(self) -> None:
        root = tk.Tk()
        root.minsize(width=WINDOW_SIZE.x, height=WINDOW_SIZE.y)
        root.maxsize(width=WINDOW_SIZE.x, height=WINDOW_SIZE.y)
        root.title("Connect four")
        app = Application(master=root)
        app.mainloop()
