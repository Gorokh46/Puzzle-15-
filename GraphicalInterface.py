import tkinter as tk
import tkinter.messagebox
from gameLogic import create_solved_board, move_tile, is_solved, get_empty_pos
from random import choice
# =============== ГРАФИЧЕСКИЙ ИНТЕРФЕЙС ===============
class Puzzle15App:
    def __init__(self, root):
        self.root = root
        self.root.title("Головоломка '15'")
        self.board = create_solved_board()
        self.buttons = [[None for _ in range(4)] for _ in range(4)]
        self.create_widgets()
        self.shuffle_board()

    def create_widgets(self):
        for i in range(4):
            for j in range(4):
                btn = tk.Button(
                    self.root,
                    text="",
                    font=("mono", 20, "bold"),
                    width=4,
                    height=2,
                    command=lambda r=i, c=j: self.on_click(r, c)
                )
                btn.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
                self.buttons[i][j] = btn
        # Настройка сетки
        for i in range(4):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def update_ui(self):
        for i in range(4):
            for j in range(4):
                value = self.board[i][j]
                self.buttons[i][j].config(text=str(value) if value != 0 else " ")

    def on_click(self, row, col):
        if move_tile(self.board, row, col):
            self.update_ui()
            if is_solved(self.board):
                tk.messagebox.showinfo("Победа!", "Вы решили головоломку!")

    def shuffle_board(self):
        """Выполняет 1000 случайных допустимых ходов для перемешивания"""
        for _ in range(1000):
            empty_row, empty_col = get_empty_pos(self.board)
            neighbors = []
            if empty_row > 0: neighbors.append((empty_row - 1, empty_col))
            if empty_row < 3: neighbors.append((empty_row + 1, empty_col))
            if empty_col > 0: neighbors.append((empty_row, empty_col - 1))
            if empty_col < 3: neighbors.append((empty_row, empty_col + 1))
            if neighbors:
                r, c = choice(neighbors)
                move_tile(self.board, r, c)
        self.update_ui()

