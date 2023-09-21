import tkinter as tk

from PaintBox.GAME.buttons import setup_buttons
from PaintBox.GAME.events import Events
from PaintBox.GAME.pic_provider import Pic_Provider
from PaintBox.GAME.square_board import Square_Board

if __name__ == '__main__':
    root = tk.Tk()
    root.title("test")

    pic_provider = Pic_Provider()
    square_board = Square_Board(root, pic_provider)
    events = Events(pic_provider, square_board)
    setup_buttons.setup(root, square_board, pic_provider)

    root.mainloop()
