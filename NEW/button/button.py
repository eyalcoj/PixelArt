from PyQt5.QtWidgets import QPushButton, QWidget


class Button:
    def __init__(self, window: QWidget, initially_button_x_cords: int,
                 initially_button_y_cords: int,
                 width_button: int, height_button: int, text: str):
        self.__button = QPushButton(text, window)
        self.__button.setGeometry(initially_button_x_cords, initially_button_y_cords, width_button,
                                  height_button)
        self.__button.clicked.connect(self.on_button_click)

    def get_button(self):
        return self.__button

    def set_fixed_size(self, button_size_x: int, button_size_y: int):
        return self.__button.setFixedSize(button_size_x, button_size_y)

    def remove_button(self):
        self.__button.setVisible(False)

    def return_button(self):
        self.__button.setVisible(True)

    def on_button_click(self):
        pass
