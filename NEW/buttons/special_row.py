from PyQt5.QtWidgets import QWidget

from NEW.buttons.drawing_board import Drawing_Board
from NEW.button.types.special_buttons import Clear_All_Button, Color_All_Button
from NEW.constants import Constants
from NEW.user_data import User_Data


class Special_Row:
    def __init__(self, window: QWidget, drawing_board: Drawing_Board, user_data: User_Data):
        self.__user_data = user_data
        self.__clear_all_button = Clear_All_Button(drawing_board, window,
                                                   (
                                                           Constants.WIDTH_WINDOW - Constants.SPECIAL_BUTTON_WIDTH * 2)
                                                   / 2 + Constants.SPECIAL_BUTTON_WIDTH,
                                                   Constants.PICS_DATA.get(
                                                       self.__user_data.get_current_pic()).get_drawing_bard_height() +
                                                   Constants.SPECIAL_BUTTON_HEIGHT,
                                                   Constants.SPECIAL_BUTTON_WIDTH,
                                                   Constants.SPECIAL_BUTTON_HEIGHT,
                                                   "Clear")
        self.__color_all_button = Color_All_Button(drawing_board, window,
                                                   (Constants.WIDTH_WINDOW - Constants.SPECIAL_BUTTON_WIDTH * 2) / 2,
                                                   Constants.PICS_DATA.get(
                                                       self.__user_data.get_current_pic()).get_drawing_bard_height() +
                                                   Constants.SPECIAL_BUTTON_HEIGHT,
                                                   Constants.SPECIAL_BUTTON_WIDTH,
                                                   Constants.SPECIAL_BUTTON_HEIGHT,
                                                   "color")

    def remove_special_row(self):
        self.__clear_all_button.remove_button()
        self.__color_all_button.remove_button()

    def add_special_row(self):
        self.__clear_all_button.return_button()
        self.__color_all_button.return_button()

