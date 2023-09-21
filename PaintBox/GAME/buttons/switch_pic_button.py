import tkinter as tk

from PaintBox.GAME.pic_provider import Pic_Provider
from PaintBox.GAME.square_board import Square_Board


class Switch_Pic_Button:
    def __init__(self, root: tk, pic_provider: Pic_Provider):
        self.pic1 = tk.Button(root, text='PIC 1', command=pic_provider.set_the_pic(0))
        self.pic2 = tk.Button(root, text='PIC 2', command=pic_provider.set_the_pic(1))
        self.pic3 = tk.Button(root, text='PIC 3', command=pic_provider.set_the_pic(2))

        self.pic3.pack(side='right')
        self.pic2.pack(side='right')
        self.pic1.pack(side='right')
