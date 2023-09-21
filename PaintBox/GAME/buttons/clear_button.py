import tkinter as tk

from PaintBox.GAME.square_board import Square_Board


class Clear_Button:
    def __init__(self, root: tk, square_board: Square_Board):
        self.root = root
        self.clear_button = tk.Button(root, text='Clear Grid', command=square_board.clear_grid)
        self.clear_button.pack(side='left')

    def switch_pic(self, square_board: Square_Board):
        self.clear_button = tk.Button(self.root, text='Clear Grid', command=square_board.clear_grid)

