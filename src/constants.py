from src.pic_data import Pic_Data


class Constants:
    # screen
    INITIALLY_WINDOW_X_CORDS = 100
    INITIALLY_WINDOW_Y_CORDS = 100

    WIDTH_WINDOW = 1600
    HEIGHT_WINDOW = 800

    # color raw
    HEIGHT_COLOR_WINDOW = 50

    # special raw
    HEIGHT_SPECIAL_RAW_WINDOW = 50

    # switch pic
    HEIGHT_SPECIAL_SWITCH_PIC = 50

    # button
    COLOR_BUTTON_LOWEST_LIMIT = HEIGHT_WINDOW - HEIGHT_COLOR_WINDOW - HEIGHT_SPECIAL_RAW_WINDOW - HEIGHT_SPECIAL_SWITCH_PIC
    INITIALLY_BUTTON_X_CORDS = 20
    INITIALLY_BUTTON_Y_CORDS = 20

    # special row
    SPECIAL_BUTTON_WIDTH = 100
    SPECIAL_BUTTON_HEIGHT = 50

    # switch pic row
    SWITCH_PIC_BUTTON_AMOUNT = 3
    SWITCH_PIC_BUTTON_WIDTH = 100
    SWITCH_PIC_BUTTON_HEIGHT = 50

    # drawing bard
    __THE_PIC1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 5, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 5, 1, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 1, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 5, 5, 1, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 5, 5, 1, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 5, 5, 5, 5, 1, 4, 4, 4, 1, 5, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 5, 5, 5, 5, 5, 1, 1, 1, 5, 5, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 5, 0, 1, 5, 5, 5, 5, 5, 5, 0, 1, 5, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 5, 5, 1, 1, 5, 1, 5, 5, 1, 5, 1, 1, 5, 5, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 5, 6, 6, 5, 5, 5, 1, 1, 5, 5, 5, 6, 6, 5, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 4, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 0, 0, 0],
        [0, 0, 0, 1, 4, 4, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 0, 0, 0],
        [0, 0, 1, 4, 4, 4, 1, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 5, 5, 5, 1, 0, 0],
        [0, 1, 1, 4, 4, 4, 1, 5, 5, 5, 5, 5, 5, 5, 1, 4, 4, 4, 1, 5, 5, 1, 1, 0],
        [1, 2, 3, 1, 4, 1, 5, 5, 5, 5, 5, 5, 5, 1, 4, 4, 4, 4, 4, 1, 1, 3, 2, 1],
        [1, 2, 3, 3, 1, 1, 5, 5, 5, 5, 5, 5, 5, 1, 4, 4, 4, 4, 1, 1, 3, 3, 2, 1],
        [1, 2, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 2, 1],
        [1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1],
        [0, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 0],
        [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
    ]

    __NUMBER_COLOR_PIC1 = {
        0: "#fefff9",
        1: "#4c2300",
        2: "#bb3405",
        3: "#ff5700",
        4: "#fe0000",
        5: "#feda00",
        6: "#ff0088"
    }

    __THE_PIC2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 4, 4, 5, 0, 0, 0, 5, 5, 5, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 8, 8, 8, 5, 4, 4, 0, 5, 5, 5, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 8, 8, 8, 5, 0, 0, 0, 5, 5, 5, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 8, 8, 5, 5, 7, 7, 7, 5, 5, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 4, 5, 5, 5, 5, 5, 5, 6, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 4, 5, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5, 4, 4, 0, 0, 4, 5, 5, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 5, 5, 5, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 8, 8, 8, 8, 8, 5, 5, 5, 6, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 8, 4, 0, 4, 8, 4, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 8, 8, 8, 4, 0, 4, 8, 8, 8, 4, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0],
        [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0]
    ]

    __NUMBER_COLOR_PIC2 = {
        0: "#fefff9",
        1: "#6abd31",
        2: "#579528",
        3: "#4a8720",
        4: "#000000",
        5: "#fbf235",
        6: "#c6be13",
        7: "#f0a3d9",
        8: "#fdb636"

    }

    __THE_PIC3 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
        [1, 2, 2, 1, 0, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 2, 2, 2, 1, 0, 0],
        [0, 1, 2, 2, 1, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 2, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 3, 3, 3, 0, 3, 3, 0, 3, 3, 0, 3, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 4, 0, 0, 0, 4, 0, 0, 0, 4, 4, 3, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 4, 0, 1, 0, 4, 0, 1, 0, 4, 5, 5, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 4, 0, 0, 0, 4, 0, 0, 0, 4, 5, 5, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 6, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 6, 6, 6, 4, 4, 4, 4, 6, 6, 1, 7, 7, 7, 1, 0, 0, 0],
        [0, 0, 0, 1, 6, 6, 6, 6, 6, 6, 6, 6, 1, 7, 0, 0, 0, 7, 1, 0, 0],
        [0, 0, 0, 1, 3, 6, 6, 6, 6, 6, 0, 1, 7, 0, 0, 7, 7, 0, 7, 1, 0],
        [0, 0, 1, 6, 3, 3, 3, 6, 6, 0, 1, 1, 7, 0, 7, 3, 3, 7, 0, 7, 1],
        [0, 0, 1, 6, 3, 3, 3, 3, 3, 3, 1, 1, 7, 0, 7, 3, 3, 7, 0, 7, 1],
        [0, 0, 1, 7, 1, 0, 7, 0, 7, 0, 1, 1, 7, 0, 7, 3, 3, 7, 0, 7, 1],
        [0, 0, 0, 1, 1, 0, 7, 0, 7, 0, 1, 1, 7, 7, 0, 7, 7, 0, 7, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 3, 1, 1, 1, 1, 3, 1, 7, 0, 0, 7, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 7, 1, 0, 0, 1, 7, 7, 1, 7, 7, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
    ]

    __NUMBER_COLOR_PIC3 = {
        0: "#ffffff",
        1: "#010101",
        2: "#a8aba8",
        3: "#132097",
        4: "#42444c",
        5: "#58340a",
        6: "#ffef4a",
        7: "#f92034"
    }

    PICS_DATA = {
        1: Pic_Data(__THE_PIC1, __NUMBER_COLOR_PIC1, WIDTH_WINDOW, COLOR_BUTTON_LOWEST_LIMIT),
        2: Pic_Data(__THE_PIC2, __NUMBER_COLOR_PIC2, WIDTH_WINDOW, COLOR_BUTTON_LOWEST_LIMIT),
        3: Pic_Data(__THE_PIC3, __NUMBER_COLOR_PIC3, WIDTH_WINDOW, COLOR_BUTTON_LOWEST_LIMIT)
    }


# color buttons
    COLOR_BUTTON_SIZE = 50
