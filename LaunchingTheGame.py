import tkinter as tk
import tkinter.messagebox
from gameLogic import create_solved_board, move_tile, is_solved, get_empty_pos
from GraphicalInterface import Puzzle15App

if __name__ == "__main__":
    root = tk.Tk()
    app = Puzzle15App(root)
    root.mainloop()
