import tkinter as tk

from PaintBox.GAME.buttons.clear_button import Clear_Button
from PaintBox.GAME.buttons.color_buttons import Color_Buttons
from PaintBox.GAME.buttons.set_color_button import Set_Color_Button
from PaintBox.GAME.buttons.switch_pic_button import Switch_Pic_Button
from PaintBox.GAME.pic_provider import Pic_Provider
from PaintBox.GAME.square_board import Square_Board


def setup(root: tk, square_board: Square_Board, pic_provider: Pic_Provider):
    Clear_Button(root, square_board)
    Color_Buttons(root, square_board, pic_provider)
    Set_Color_Button(root, square_board)
    Switch_Pic_Button(root, pic_provider)

    # return color_buttons, clear_buttons, set_color_button, switch_pic_button
