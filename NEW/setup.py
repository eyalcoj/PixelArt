from PyQt5.QtWidgets import QWidget

from NEW.buttons.color_chooser_row import Color_Chooser_Row
from NEW.buttons.drawing_board import Drawing_Board
from NEW.buttons.special_row import Special_Row
from NEW.buttons.switch_pic_row import Switch_Pic_Row
from NEW.user_data import User_Data


def setup_change_buttons(window: QWidget, user_data: User_Data):
    drawing_board = Drawing_Board(window, user_data)
    color_chooser_row = Color_Chooser_Row(window, user_data)
    special_row = Special_Row(window, drawing_board, user_data)
    return drawing_board, color_chooser_row, special_row

