import pygame

import Menu
import const


class Window_Activation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((const.mw, const.mh))
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption("PyZuma")

        self.all_sprites = []

    def dead(self):
        for element in self.all_sprites:
            element._hidden = True
        self.all_sprites = []


if __name__ == '__main__':
    app = Menu.Start()
    app.work()
