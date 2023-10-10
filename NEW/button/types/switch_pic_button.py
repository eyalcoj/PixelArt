from PyQt5.QtWidgets import QWidget

from NEW.button.button import Button
from NEW.user_data import User_Data


class Switch_Pic_Button(Button):
    def __init__(self, window: QWidget, initially_button_x_cords: int,
                 initially_button_y_cords: int, width_button: int, height_button: int, text: str, pic_number: int,
                 user_data: User_Data, buttons: list):
        super().__init__(window, initially_button_x_cords, initially_button_y_cords, width_button, height_button, text)
        self.__buttons = buttons
        self.__window = window
        self.__user_data = user_data
        self.__pic_number = pic_number

    def on_button_click(self):
        self.__user_data.set_current_pic(self.__pic_number)
        for i in range(0, 3):
            self.__buttons[i].remove_buttons()
        self.__buttons[self.__pic_number - 1].add_buttons()
