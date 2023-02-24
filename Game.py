from random import choice
import math
from tkinter import *

import pygame
import pygame_widgets

import const
import Menu
import start

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

FPS = 60
V = 55


class Game(start.Window_Activation):
    def __init__(self, n_lvl, mode):
        super(Game, self).__init__()

        self.n_lvl = n_lvl
        self.mode = mode
        if self.mode:
            self.n_balls = 29
        self.pause = False
        self.s = 0
        self.all_sprites = []
        self.frog = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.color_frog = []

        if self.n_lvl == 1:
            const.draw_background(self, 'lvl1', width=monitor_width, height=monitor_height)
            x = const.mw * 5 / 6
            y = const.mh * 4 / 5
        elif self.n_lvl == 2:
            const.draw_background(self, 'lvl2', width=monitor_width, height=monitor_height)
            x = const.mw * 25 / 36
            y = const.mh / 9
        elif self.n_lvl == 3:
            const.draw_background(self, 'lvl3', width=monitor_width, height=monitor_height)
            x = const.mw * 35 / 144
            y = const.mh * 4 / 5

        sprite = Balls(const.VECTORS[f'lvl{self.n_lvl}'])
        self.balls.add(sprite)
        self.color_frog.append(sprite.color)
        sprite = Frog(choice(self.balls.sprites()).color, x, y)
        self.frog.add(sprite)

    def work(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    const.terminate()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.dead()
                        Menu.Start().work()
                        return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(f'{event.pos},')
                    # don't work
                    # if event.key == pygame.K_ESCAPE:
                    #     self.pause = not self.pause
                    #     if self.pause:
                    #         if Pause(self).work() is None:
                    #             pass
            if not self.pause:
                if self.balls.sprites()[0].ind < len(const.VECTORS[f'lvl{self.n_lvl}']):
                    # const.draw_background(
                    #     self, f'lvl{self.n_lvl}', width=monitor_width, height=monitor_height
                    # )
                    self.balls.update()
                    self.balls.draw(self.screen)
                    self.frog.draw(self.screen)
                    self.frog.update()  # choice(self.balls.sprites()).color
                    # sprite = Balls(const.VECTORS[f'lvl{self.n_lvl}'])
                    # self.balls.add(sprite)
                    self.s += max(self.balls.sprites()[-1].v_x, self.balls.sprites()[0].v_y)
                    if self.s >= 42 and self.n_balls != 0:
                        sprite = Balls(const.VECTORS[f'lvl{self.n_lvl}'])
                        self.balls.add(sprite)
                        self.color_frog.append(sprite.color)
                        self.n_balls -= 1
                        self.s = 0
                elif len(self.balls.sprites()) == 0:
                    self.all_sprites.append(
                        const.draw_text(
                            self, int(const.mw * 3 / 8), int(const.mh / 3 * 1.25),
                            int(const.mw / 3 * 0.8), int(const.mh / 11), 'Вы выиграли', font=80
                        ))
                else:
                    self.all_sprites.append(
                        const.draw_text(
                            self, int(const.mw * 3 / 8), int(const.mh / 3 * 1.25),
                            int(const.mw / 3 * 0.8), int(const.mh / 11),
                            'Вы проиграли', font=80
                        ))
                self.clock.tick(FPS)
            pygame.display.update()

            pygame_widgets.update(events)
            pygame.display.flip()



class Frog(pygame.sprite.Sprite):
    image = {
        'red': const.load_image("../picture/Frog_red.png"),
        'yellow': const.load_image("../picture/Frog_yellow.png"),
        'blue': const.load_image("../picture/Frog_blue.png"),
        'green': const.load_image("../picture/Frog_green.png"),
    }

    def __init__(self, color, *args):
        pygame.sprite.Sprite.__init__(self)
        self.image = Frog.image[color]
        self.x, self.y = args
        self.color = color
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self, color=None):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        if color is not None:
            self.color = color
        self.image = pygame.transform.rotate(Frog.image[self.color], int(angle))
        self.rect = self.image.get_rect(center=(self.x, self.y))


class Balls(pygame.sprite.Sprite):
    balls = {
        'blue': pygame.transform.scale(const.load_image("../picture/Blue.png"), (55, 55)),
        'red': pygame.transform.scale(const.load_image("../picture/Red.png"), (45, 45)),
        'yellow': pygame.transform.scale(const.load_image("../picture/Yellow.png"), (55, 55)),
        'green': pygame.transform.scale(const.load_image("../picture/Green.png"), (55, 55))
    }

    def __init__(self, vectors, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.vectors = vectors
        self.color = choice(['blue', 'red', 'yellow', 'green'])
        self.image = Balls.balls[self.color]
        self.x, self.y = self.vectors[0]
        self.x1, self.y1 = self.vectors[1]
        self.ind = 1
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.time = max(abs(self.x1 - self.x), abs(self.y1 - self.y)) / V
        self.v_x = round((self.x1 - self.x) / self.time / FPS)
        self.v_y = round((self.y1 - self.y) / self.time / FPS)

    def update(self):
        if abs(self.v_x) <= abs(self.x1 - self.x) and abs(self.v_y) <= abs(self.y1 - self.y):
            self.x += self.v_x
            self.y += self.v_y
            self.time -= 1
            self.rect = self.rect.move(self.v_x, self.v_y)
        else:
            self.ind += 1
            if self.ind < len(self.vectors):
                self.x = self.x1
                self.y = self.y1
                self.x1, self.y1 = self.vectors[self.ind]
                self.time = max(abs(self.x1 - self.x), abs(self.y1 - self.y)) / V
                if self.x1 - self.x != 0:
                    self.v_x = round((self.x1 - self.x) / self.time / FPS)
                else:
                    self.v_x = 0
                if self.y1 - self.y != 0:
                    self.v_y = round((self.y1 - self.y) / self.time / FPS)
                else:
                    self.v_y = 0
                self.update()

# Don't work
# I don't understand why
# when return is triggered, the program simply stops, although it should continue to work

# class Pause:
#     def __init__(self, other):
#         self.other = other
#         const.draw_background(
#             self.other, 'pause', x=int(const.mw / 2), y=int(const.mh / 3),
#             width=int(const.mw * 5 / 9),
#             height=int(const.mh * 0.8)
#         )
#         for btn in const.BUTTONS['pause']:
#             self.other.all_sprites.append(const.draw_button(
#                 self.other, *btn[0], message=btn[1], picture=btn[2], font=40
#             ))
#
#     def work(self):
#         btns = const.BUTTONS['pause']
#         while True:
#             events = pygame.event.get()
#             for event in events:
#                 if event.type == pygame.QUIT:
#                     const.terminate()
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if const.check_click(btns[0], event):
#                         self.other.dead()
#                         return None
#                     elif const.check_click(btns[1], event):
#                         self.other.dead()
#                         Settings.Window()
#                         return
#                     elif const.check_click(btns[2], event):
#                         self.other.dead()
#                         Menu.Start().work()
#                         return
#             pygame_widgets.update(events)
#             pygame.display.flip()
