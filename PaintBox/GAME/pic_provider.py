from PaintBox.GAME.constants import *


class Pic_Provider:

    def __init__(self):
        self.current_select_number = 0
        self.all_colors = [COLORS_PIC1, COLORS_PIC2]
        self.all_pics = [PIC1, PIC2]

    def set_the_pic(self, current_select_number):
        self.current_select_number = current_select_number

    def get_the_pic(self):
        return self.all_pics[self.current_select_number]

    def get_the_colors(self):
        return self.all_colors[self.current_select_number]
