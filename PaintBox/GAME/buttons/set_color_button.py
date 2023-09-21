import tkinter as tk

from PaintBox.GAME.square_board import Square_Board


class Set_Color_Button:
    def __init__(self, root: tk, square_board: Square_Board):
        self.root = root
        self.color_button = tk.Button(root, text='Set All Color', command=square_board.set_all_color_square)
        self.color_button.pack(side='left')

    def switch_pic(self, square_board: Square_Board):
        self.color_button = tk.Button(self.root, text='Set All Color', command=square_board.set_all_color_square)
