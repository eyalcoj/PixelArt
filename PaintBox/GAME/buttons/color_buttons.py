import tkinter as tk

from PaintBox.GAME import utils
from PaintBox.GAME.pic_provider import Pic_Provider
from PaintBox.GAME.square_board import Square_Board


class Color_Buttons:
    def __init__(self, root: tk, square_board: Square_Board, pic_provider: Pic_Provider):
        self.number_color_buttons = []
        self.color_buttons = []
        self.root = root

        self.start_color(square_board, pic_provider)

    def start_color(self, square_board: Square_Board, pic_provider: Pic_Provider):
        for i in range(len(pic_provider.get_the_colors()) - 1):
            self.number_color_buttons.append(i + 1)

        for number in self.number_color_buttons:
            self.color_buttons.append(
                tk.Button(self.root, text=number, fg='gray', bg=utils.get_color(number, pic_provider.get_the_colors()),
                          command=lambda c=number: square_board.change_number(c)))

        for button in self.color_buttons:
            button.pack(side='left')


def switch_pic(self, square_board: Square_Board, pic_provider: Pic_Provider):
    self.number_color_buttons.clear()
    self.color_buttons.clear()
    self.start_color(square_board, pic_provider)
