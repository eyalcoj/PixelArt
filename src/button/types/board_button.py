from PyQt5.QtWidgets import QWidget

from src.button.button import Button
from src.constants import Constants
from src.user_data import User_Data


class Board_Button(Button):
    def __init__(self, window: QWidget, initially_button_x_cords: int, initially_button_y_cords: int, width_button: int,
                 height_button: int, number: int, user_data: User_Data):
        super().__init__(window, initially_button_x_cords, initially_button_y_cords, width_button, height_button,
                         f"{number}")
        self.set_to_default()
        self.__user_data = user_data
        self.__number = number

    def on_button_click(self):
        if self.__user_data.get_number() == self.__number:
            self.set_to_color()

    def set_to_default(self):
        self.get_button().setStyleSheet(f'background-color: white; color: #36393e;')

    def set_to_color(self):
        self.get_button().setStyleSheet(
            f'background-color: {Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_number_color_pic().get(self.__number)}; color: #36393e;')
