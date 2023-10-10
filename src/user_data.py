class User_Data:
    def __init__(self):
        self.__number = -1
        self.__current_pic = 1

    def get_number(self):
        return self.__number

    def set_number(self, number: int):
        self.__number = number

    def get_current_pic(self):
        return self.__current_pic

    def set_current_pic(self, current_pic: int):
        self.__current_pic = current_pic

