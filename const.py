import os
import sys
from tkinter import *

import pygame
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox

root = Tk()

mh = root.winfo_screenheight()
mw = root.winfo_screenwidth()

BUTTONS = {
    'Menu': [
        [(int(mw * 5 / 18), int(mh / 3), int(mw * 5 / 24), int(mh / 9)),
         'Играть', '../picture/button.png'],
        [(int(mw * 5 / 18), int(mh * 7 / 15), int(mw * 5 / 24), int(mh / 9)),
         'Настройки', '../picture/button.png'],
        [(int(mw * 5 / 18), int(mh * 3 / 5), int(mw * 5 / 24), int(mh / 9)),
         'Выход', '../picture/button.png'],
    ],
    'Choose_lvl': [
        [(int(mw * 5 / 18), int(mh * 22 / 45), int(mw * 5 / 48), int(mh / 6)),
         '1', '../picture/button.png'],
        [(int(mw * 65 / 144), int(mh * 22 / 45), int(mw * 5 / 48), int(mh / 6)),
         '2', '../picture/button.png'],
        [(int(mw * 5 / 8), int(mh * 22 / 45), int(mw * 5 / 48), int(mh / 6)),
         '3', '../picture/button.png'],
        [(int(mw * 5 / 72), int(mh * 34 / 45), int(mw * 5 / 48), int(mh / 6)),
         'Назад', '../picture/button.png'],
        [(int(mw * 37 / 144), int(mh * 7 / 45), int(mw * 5 / 24), int(mh / 6)),
         'Бесконечный', '../picture/button.png'],
        [(int(mw * 77 / 144), int(mh * 7 / 45), int(mw * 5 / 24), int(mh / 6)),
         'Со временем', '../picture/button.png']
    ],
    "pause": [
        [(int(mw * 3 / 8), int(mh / 6), int(mw / 4), int(mh / 11)),
         'Вернуться в игру', '../picture/button.png'],
        [(int(mw * 3 / 8), int(mh / 4 * 1.15), int(mw / 4), int(mh / 11)),
         'Настройки', '../picture/button.png'],
        [(int(mw * 3 / 8), int(mh / 3 * 1.25), int(mw / 4), int(mh / 11)),
         'В меню', '../picture/button.png']
    ],
    "Settings": [
        [(int(mw * 5 / 72), int(mh * 13 / 18), int(mw * 5 / 48), int(mh / 6)),
         '<-', '../picture/button.png']
    ]
}

BACKGROUNDS = {
    'Menu': "../picture/background_menu.jpg",
    'lvl1': '../picture/denial.jpg',
    'lvl2': "../picture/spiral.jpg",
    'lvl3': "../picture/Riverbed.jpg",
    'pause': "../picture/pause.png"
}

TEXTS = {
    'Menu': [
            [(int(mw * 5 / 18), int(mh / 5), int(mw * 5 / 24), int(mh / 9)), ' pyZuma']
        ],
    'Choose_lvl': [
        [(int(mw * 55 / 144), int(mh / 30), int(mw * 5 / 18), int(mh / 9)), 'Выберите режим'],
        [(int(mw * 3 / 8), int(mh * 16 / 45), int(mw * 41 / 144), int(mh / 9)), 'Выберите уровень '],
    ]
}

VECTORS = {
    'lvl1': [
        (0, 110),
        (1380, 114),
        (1380, 260),
        (172, 270),
        (173, 399),
        (1182, 409),
        (1186, 552),
        (448, 560)
    ],
    'lvl2': [
        (1513, 393),
        (1446, 393),
        (1387, 387),
        (1322, 378),
        (1265, 363),
        (1199, 340),
        (1150, 320),
        (1092, 300),
        (1036, 279),
        (980, 266),
        (917, 254),
        (857, 241),
        (797, 227),
        (731, 214),
        (672, 205),
        (609, 195),
        (556, 185),
        (478, 185),
        (435, 188),
        (371, 199),
        (323, 213),
        (264, 230),
        (232, 251),
        (194, 286),
        (185, 319),
        (166, 362),
        (160, 406),
        (161, 452),
        (176, 490),
        (189, 538),
        (215, 580),
        (243, 622),
        (292, 658),
        (340, 686),
        (386, 703),
        (436, 721),
        (495, 730),
        (562, 733),
        (617, 742),
        (686, 748),
        (750, 751),
        (818, 749),
        (877, 741),
        (940, 729),
        (985, 712),
        (1030, 684),
        (1067, 652),
        (1104, 612),
        (1112, 579),
        (1124, 541),
        (1112, 504),
        (1083, 461),
        (1058, 438),
        (1005, 407),
        (963, 392),
        (898, 375),
        (843, 364),
        (781, 352),
        (724, 340),
        (654, 333),
        (610, 328),
        (542, 333),
        (482, 341),
        (417, 358),
        (378, 375),
        (322, 411),
        (303, 472),
        (327, 534),
        (376, 577),
        (424, 600),
        (466, 610),
        (533, 619),
        (594, 628),
        (669, 634),
        (729, 632),
        (795, 633),
        (852, 618),
        (891, 604)
    ],
    'lvl3': [
        (809, 856),
        (1430, 573),
        (1365, 495),
        (782, 741),
        (715, 662),
        (1320, 389),
        (1115, 143),
        (161, 539),
        (77, 429),
        (685, 166),
        (623, 83),
        (154, 268)
    ]

}


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def draw_background(self, key, width=None, height=None):
    picture = BACKGROUNDS[key]
    if width is None:
        image = load_image(picture)
    else:
        image = pygame.transform.scale(load_image(picture), (width, height))
    self.screen.blit(image, (0, 0))


def draw_button(self, x, y, width, height, message='', picture='', font=60):
    return Button(
        self.screen,
        x,
        y,
        width,
        height,

        text=message,
        fontSize=font,
        textColour=(255, 200, 0),
        image=pygame.transform.scale(load_image(picture), (width, height))
    )


def draw_text(self, x, y, width, height, text='', font=50):
    return TextBox(
        self.screen,
        x,
        y,
        width,
        height,

        fontSize=font,
        borderColour=(255, 200, 0),
        textColour=(255, 200, 0),
        radius=10,
        borderThickness=5,
        placeholderText=text,
        colour=(77, 34, 14),
    )


def terminate():
    pygame.quit()
    sys.exit()


def check_click(btn, event):
    return btn[0][0] <= event.pos[0] <= btn[0][0] + btn[0][2] and \
           btn[0][1] <= event.pos[1] <= btn[0][1] + btn[0][3]


def dead(self):
    for element in self.all_sprites:
        element._hidden = True
    self.all_sprites = []


