from PyQt5.QtWidgets import QWidget

from src.buttons.drawing_board import Drawing_Board
from src.button.button import Button


class Clear_All_Button(Button):
    def __init__(self, drawing_board: Drawing_Board, window: QWidget, initially_button_x_cords: int,
                 initially_button_y_cords: int, width_button: int, height_button: int, text: str):
        super().__init__(window, initially_button_x_cords, initially_button_y_cords, width_button, height_button, text)
        self.__drawing_board = drawing_board

    def on_button_click(self):
        self.__drawing_board.set_to_default()


class Color_All_Button(Button):
    def __init__(self, drawing_board: Drawing_Board, window: QWidget, initially_button_x_cords: int,
                 initially_button_y_cords: int, width_button: int, height_button: int, text: str):
        super().__init__(window, initially_button_x_cords, initially_button_y_cords, width_button, height_button, text)
        self.__drawing_board = drawing_board

    def on_button_click(self):
        self.__drawing_board.set_to_color()
