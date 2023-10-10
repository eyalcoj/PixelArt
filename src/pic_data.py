import math


class Pic_Data:
    def __init__(self, the_pic, number_color_pic, width_window, color_button_lowest_limit):
        self.__the_pic = the_pic
        self.__number_color_pic = number_color_pic
        self.__pix_width_pic = len(the_pic)
        self.__pix_height_pic = len(the_pic[0])

        self.__button_size = math.floor(min(width_window / self.__pix_height_pic,
                                 color_button_lowest_limit / self.__pix_width_pic))

        self.__drawing_bard_width = self.__button_size * self.__pix_height_pic
        self.__drawing_bard_height = self.__button_size * self.__pix_width_pic

        self.__drawing_bard_start_x = math.ceil((width_window - self.__drawing_bard_width)) / 2
        self.__drawing_bard_start_y = 0

    def get_the_pic(self):
        return self.__the_pic

    def get_pix_width_pic(self):
        return self.__pix_width_pic

    def get_pix_height_pic(self):
        return self.__pix_height_pic

    def get_number_color_pic(self):
        return self.__number_color_pic

    def get_button_size(self):
        return self.__button_size

    def get_drawing_bard_width(self):
        return self.__drawing_bard_width

    def get_drawing_bard_height(self):
        return self.__drawing_bard_height

    def get_drawing_bard_start_x(self):
        return self.__drawing_bard_start_x

    def get_drawing_bard_start_y(self):
        return self.__drawing_bard_start_y
