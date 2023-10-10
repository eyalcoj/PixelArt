import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette

class ColorChangingButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.pressed.connect(self.change_color)

    def change_color(self):
        # Generate a random color
        color = QColor.fromRgbF(
            0.5,  # Red component
            0.7,  # Green component
            0.9   # Blue component
        )

        # Set the button's background color
        palette = QPalette()
        palette.setColor(QPalette.Button, color)
        self.setAutoFillBackground(True)
        self.setPalette(palette)

class ColorChangingButtonExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color Changing Button Example")
        self.setGeometry(100, 100, 400, 200)

        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a ColorChangingButton
        self.color_button = ColorChangingButton("Press me to change color", central_widget)
        self.color_button.setGeometry(50, 50, 300, 100)

def main():
    app = QApplication(sys.argv)
    window = ColorChangingButtonExample()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
