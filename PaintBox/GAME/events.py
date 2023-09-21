from PaintBox.GAME.constants import *
from PaintBox.GAME.pic_provider import Pic_Provider
from PaintBox.GAME.square_board import Square_Board


class Events:
    def __init__(self, pic_provider: Pic_Provider, square_board: Square_Board):
        self.pic_provider = pic_provider
        self.size_square = None
        self.square_board = None
        self.canvas = None
        self.setup(square_board)

    def on_canvas_click(self, event):
        row = event.y // self.size_square
        col = event.x // self.size_square
        self.square_board.get_square(int(col), int(row)).set_color_rect(self.square_board.number)

    def setup(self, square_board: Square_Board):
        self.size_square = CANVAS_WIDTH_AND_HEIGHT / len(self.pic_provider.get_the_pic())
        self.square_board = square_board
        self.canvas = square_board.canvas
        self.canvas.bind('<Button-1>', self.on_canvas_click)

    def switch_pic(self, square_board: Square_Board):
        self.setup(square_board)