from PyQt5.QtWidgets import QWidget

from src.button.types.board_button import Board_Button
from src.constants import Constants
from src.user_data import User_Data


class Drawing_Board:
    def __init__(self, window: QWidget, user_data: User_Data):
        self.__buttons = None
        self.__user_data = user_data
        self.__crate_table(window)

    def __crate_table(self, window: QWidget):
        self.__buttons = []
        for row in range(Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_pix_height_pic()):
            self.__buttons.append([])
            for col in range(Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_pix_width_pic()):
                print(Constants.PICS_DATA.get(
                        self.__user_data.get_current_pic()).get_button_size())
                self.__buttons[row].append(
                    Board_Button(window, Constants.PICS_DATA.get(
                        self.__user_data.get_current_pic()).get_button_size() * row + Constants.PICS_DATA.get(
                        self.__user_data.get_current_pic()).get_drawing_bard_start_x(),
                                 Constants.PICS_DATA.get(
                                     self.__user_data.get_current_pic()).get_button_size() * col + Constants.PICS_DATA.get(
                                     self.__user_data.get_current_pic()).get_drawing_bard_start_y(),
                                 Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_button_size(),
                                 Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_button_size(),
                                 Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_the_pic()[col][row],
                                 self.__user_data))

    def remove_table(self):
        for row in range(len(self.__buttons)):
            for col in range(len(self.__buttons[row])):
                self.__buttons[row][col].remove_button()

    def add_table(self):
        for row in range(len(self.__buttons)):
            for col in range(len(self.__buttons[row])):
                self.__buttons[row][col].return_button()

    def set_to_default(self):
        for row in range(Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_pix_height_pic()):
            for col in range(Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_pix_width_pic()):
                self.__buttons[row][col].set_to_default()

    def set_to_color(self):
        for row in range(Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_pix_height_pic()):
            for col in range(Constants.PICS_DATA.get(self.__user_data.get_current_pic()).get_pix_width_pic()):
                self.__buttons[row][col].set_to_color()
