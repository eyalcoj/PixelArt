from PyQt5.QtWidgets import QWidget

from NEW.button.types.switch_pic_button import Switch_Pic_Button
from NEW.constants import Constants
from NEW.user_data import User_Data


class Switch_Pic_Row:
    def __init__(self, window: QWidget, user_data: User_Data, buttons: list):
        self.__user_data = user_data
        self.__buttons = buttons
        self.__crate_row(window)

    def __crate_row(self, window: QWidget):
        self.buttons = []
        for cel in range(1, Constants.SWITCH_PIC_BUTTON_AMOUNT + 1):
            self.buttons.append(
                Switch_Pic_Button(window, Constants.SWITCH_PIC_BUTTON_WIDTH * (cel - 1) + (Constants.WIDTH_WINDOW -
                                                                                           Constants.SWITCH_PIC_BUTTON_AMOUNT * Constants.SWITCH_PIC_BUTTON_WIDTH) / 2,
                                  Constants.HEIGHT_WINDOW - Constants.SWITCH_PIC_BUTTON_HEIGHT,
                                  Constants.SPECIAL_BUTTON_WIDTH, Constants.SPECIAL_BUTTON_HEIGHT, f"pic {cel}", cel,
                                  self.__user_data, self.__buttons))

