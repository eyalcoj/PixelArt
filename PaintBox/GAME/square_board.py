import tkinter as tk

from PaintBox.GAME.constants import *
from PaintBox.GAME.pic_provider import Pic_Provider
from PaintBox.GAME.square import Square


class Square_Board:
    def __init__(self, root: tk, pic_provider: Pic_Provider):
        self.squares = None
        self.size_square = None
        self.pic_provider = pic_provider
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH_AND_HEIGHT, height=CANVAS_WIDTH_AND_HEIGHT)
        self.crate_pic()
        self.canvas.pack()

    def crate_pic(self):
        self.size_square = CANVAS_WIDTH_AND_HEIGHT / len(self.pic_provider.get_the_pic())
        self.squares = []
        self.__crate_squares()

    def __crate_squares(self):
        for rows in range(len(self.pic_provider.get_the_pic())):
            for cols in range(len(self.pic_provider.get_the_pic()[rows])):
                self.squares.append(
                    Square(rows, cols, self.pic_provider.get_the_pic()[rows][cols], self.canvas, self.size_square,
                           self.pic_provider))
                self.squares[rows * len(self.pic_provider.get_the_pic()) + cols].default_rect()

    def __reset_squares(self):
        for rows in range(len(self.pic_provider.get_the_pic())):
            for cols in range(len(self.pic_provider.get_the_pic()[rows])):
                self.squares[rows * len(self.pic_provider.get_the_pic()) + cols].default_rect()

    def get_square(self, rows: int, cols: int):
        return self.squares[cols * len(self.pic_provider.get_the_pic()) + rows]

    def clear_grid(self):
        self.canvas.delete('all')
        self.__reset_squares()

    def set_all_color_square(self):
        for rows in range(len(self.pic_provider.get_the_pic())):
            for cols in range(len(self.pic_provider.get_the_pic()[rows])):
                self.squares[rows * len(self.pic_provider.get_the_pic()) + cols].set_square_default_number()
