from PyQt5.QtWidgets import QWidget

from NEW.button.button import Button
from NEW.constants import Constants
from NEW.user_data import User_Data


class Color_Chooser_Button(Button):
    def __init__(self, window: QWidget, initially_button_x_cords: int, initially_button_y_cords: int, width_button: int,
                 height_button: int, number: int, user_data: User_Data):
        super().__init__(window, initially_button_x_cords, initially_button_y_cords, width_button, height_button,
                         f"{number}")
        self.__user_data = user_data
        self.__number = number
        self.get_button().setStyleSheet(
            f'background-color: {Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_number_color_pic().get(self.__number)}; color: black;')

    def on_button_click(self):
        self.__user_data.set_number(self.__number)
