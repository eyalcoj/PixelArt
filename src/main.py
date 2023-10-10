import sys

from PyQt5.QtWidgets import QApplication, QWidget

from src.buttons.all_buttons import All_Buttons
from src.buttons.switch_pic_row import Switch_Pic_Row
from src.constants import Constants
from src.setup import setup_change_buttons
from src.user_data import User_Data


class run:
    def __init__(self, title: str):
        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle(title)
        window.setGeometry(Constants.INITIALLY_WINDOW_X_CORDS,
                           Constants.INITIALLY_WINDOW_Y_CORDS,
                           Constants.WIDTH_WINDOW,
                           Constants.HEIGHT_WINDOW)
        user_data = User_Data()
        self.buttons = []
        for i in range(3):
            user_data.set_current_pic(i + 1)
            self.buttons.append(All_Buttons(setup_change_buttons(window, user_data)))
            self.buttons[i].remove_buttons()
        self.buttons[user_data.get_current_pic() - 1].add_buttons()
        print(len(self.buttons))
        switch_pic_row = Switch_Pic_Row(window, user_data, self.buttons)
        window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    app_instance = run("The best Pixel art (Ben & Eyal)")
