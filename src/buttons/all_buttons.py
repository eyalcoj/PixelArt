from src.buttons.color_chooser_row import Color_Chooser_Row
from src.buttons.drawing_board import Drawing_Board
from src.buttons.special_row import Special_Row


class All_Buttons:
    def __init__(self, all_buttons: tuple):
        # drawing_board, color_chooser_row, special_row
        self.__drawing_board: Drawing_Board = all_buttons[0]
        self.__color_chooser_row: Color_Chooser_Row = all_buttons[1]
        self.__special_row: Special_Row = all_buttons[2]

    def get_drawing_board(self):
        return self.__drawing_board

    def get_color_chooser_row(self):
        return self.__color_chooser_row

    def get_special_row(self):
        return self.__special_row

    def remove_buttons(self):
        self.__drawing_board.remove_table()
        self.__color_chooser_row.remove_color_chooser_row()
        self.__special_row.remove_special_row()

    def add_buttons(self):
        self.__drawing_board.add_table()
        self.__color_chooser_row.add_color_chooser_row()
        self.__special_row.add_special_row()
