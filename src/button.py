import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QColor
from functools import partial

class ColorChooserTableDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Chooser Table Demo')
        self.setGeometry(100, 100, 600, 600)  # Adjust the window size

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.tableWidget = QTableWidget(5, 5, self)  # Create a 5x5 table
        layout.addWidget(self.tableWidget)

        color_chooser_layout = QHBoxLayout()

        # List of preset colors
        preset_colors = [
            QColor('red'),
            QColor('green'),
            QColor('blue'),
            QColor('yellow'),
            QColor('orange'),
            QColor('purple'),
            QColor('pink'),
            QColor('brown'),
            QColor('gray'),
        ]

        self.color_buttons = []
        self.selected_number = None  # To keep track of the selected number

        for idx, color in enumerate(preset_colors, start=1):
            color_button = QPushButton(str(idx))
            color_button.setStyleSheet(f"background-color: {color.name()};")
            color_button.clicked.connect(partial(self.onColorButtonClick, idx, color))  # Pass both number and color
            color_chooser_layout.addWidget(color_button)
            self.color_buttons.append(color_button)

        layout.addLayout(color_chooser_layout)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)

        cell_size = 100  # Increase the cell size for the larger table

        for row in range(5):
            self.tableWidget.setRowHeight(row, cell_size)
            for col in range(5):
                self.tableWidget.setColumnWidth(col, cell_size)
                button_text = str(row * 5 + col + 1)  # Generate numeric text
                button = QPushButton(button_text)
                button.clicked.connect(partial(self.onTableButtonClick, button))
                button.setFixedSize(cell_size, cell_size)
                self.tableWidget.setCellWidget(row, col, button)

    def onTableButtonClick(self, button):
        if self.selected_number is not None:
            button_text = button.text()
            if int(button_text) == self.selected_number:
                # Change the background color of the clicked button using the selected color
                button.setStyleSheet(f"background-color: {self.selected_color.name()};")

    def onColorButtonClick(self, number, color):
        self.selected_number = number  # Update the selected number
        self.selected_color = color

def main():
    app = QApplication(sys.argv)
    window = ColorChooserTableDemo()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
