from PyQt5.QtWidgets import QWidget

from src.button.types.color_chooser_button import Color_Chooser_Button
from src.constants import Constants
from src.user_data import User_Data


class Color_Chooser_Row:
    def __init__(self, window: QWidget, user_data: User_Data):
        self.buttons = None
        self.__user_data = user_data
        self.crate_row(window)

    def crate_row(self, window: QWidget):
        self.buttons = []
        for cel in range(len(Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_number_color_pic())):
            self.buttons.append(
                Color_Chooser_Button(window, Constants.COLOR_BUTTON_SIZE * cel + (
                        Constants.WIDTH_WINDOW - Constants.COLOR_BUTTON_SIZE * len(
                    Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_number_color_pic())) / 2,
                                     Constants.PICS_DATA.get(
                                         self.__user_data.get_current_pic()).get_drawing_bard_height(),
                                     Constants.COLOR_BUTTON_SIZE, Constants.COLOR_BUTTON_SIZE,
                                     (cel + 1),
                                     self.__user_data))

    def remove_color_chooser_row(self):
        for cel in range(len(self.buttons)):
            self.buttons[cel].remove_button()

    def add_color_chooser_row(self):
        for cel in range(len(self.buttons)):
            self.buttons[cel].return_button()
