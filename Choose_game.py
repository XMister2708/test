import const

import pygame
import pygame_widgets

import Menu
import start
import Game


class Window(start.Window_Activation):
    def __init__(self):
        super(Window, self).__init__()
        self.mode = True
        self.screen.fill((139, 69, 19))

        for btn in const.BUTTONS['Choose_lvl']:
            self.all_sprites.append(const.draw_button(
                self, *btn[0], message=btn[1], picture=btn[2], font=60
            ))

        for text in const.TEXTS['Choose_lvl']:
            self.all_sprites.append(const.draw_text(
                self, *text[0], text[1], font=60
            ))

    def work(self):
        btns = const.BUTTONS['Choose_lvl']
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    const.terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if const.check_click(btns[3], event):
                        self.dead()
                        Menu.Start().work()
                        return
                    if const.check_click(btns[0], event):
                        self.dead()
                        Game.Game(1, self.mode).work()
                        return
                    if const.check_click(btns[1], event):
                        self.dead()
                        Game.Game(2, self.mode).work()
                        return
                    if const.check_click(btns[2], event):
                        self.dead()
                        Game.Game(3, self.mode).work()
                        return
                    if const.check_click(btns[4], event):
                        self.mode = False
                    if const.check_click(btns[5], event):
                        self.mode = True

            pygame_widgets.update(events)
            pygame.display.flip()
