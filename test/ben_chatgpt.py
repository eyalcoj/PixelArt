import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QColor

class PixelArtGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Pixel Art Game')
        self.central_widget = PixelCanvas()
        self.setCentralWidget(self.central_widget)

class PixelCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pixel_size = 20  # Adjust the size of your pixels here
        self.grid = [[QColor(255, 255, 255) for _ in range(40)] for _ in range(30)]  # 30x40 grid of white pixels

    def paintEvent(self, event):
        painter = QPainter(self)
        for y, row in enumerate(self.grid):
            for x, color in enumerate(row):
                painter.fillRect(x * self.pixel_size, y * self.pixel_size, self.pixel_size, self.pixel_size, color)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = PixelArtGame()
    game.show()
    sys.exit(app.exec_())
