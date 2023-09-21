from PaintBox.GAME import utils
from PaintBox.GAME.pic_provider import Pic_Provider


class Square:
    def __init__(self, cel: int, row: int, number: int, canvas, size_square: int, pic_provider: Pic_Provider):
        self.pic_provider = pic_provider
        self.size_square = size_square
        self.cel = cel
        self.row = row
        self.number = number
        self.canvas = canvas

    def set_color_rect(self, number: float):
        if number == self.number:
            self.__colored_rec(self.number)
            self.__numbered_rec(self.number)

    def set_square_default_number(self):
        self.__colored_rec(self.number)
        self.__numbered_rec(self.number)

    def default_rect(self):
        self.__colored_rec(0)
        self.__numbered_rec(self.number)

    def __colored_rec(self, number: int):
        self.canvas.create_rectangle(
            self.row * self.size_square, self.cel * self.size_square, (self.row + 1) * self.size_square,
            (self.cel + 1) * self.size_square,
            fill=utils.get_color(number, self.pic_provider.get_the_colors())
        )

    def __numbered_rec(self, number):
        self.canvas.create_text(self.row * self.size_square + self.size_square / 2,
                                self.cel * self.size_square + self.size_square / 2,
                                text=f"{number}", fill="gray")
