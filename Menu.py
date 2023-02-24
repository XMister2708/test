import const

import pygame
import pygame_widgets

import start

import Choose_game
import Settings


class Start(start.Window_Activation):
    def __init__(self):
        super(Start, self).__init__()
        const.draw_background(self, 'Menu', width=const.mw, height=const.mh)

        for text in const.TEXTS['Menu']:
            self.all_sprites.append(const.draw_text(
                self, *text[0], text[1], font=80
            ))

        for btn in const.BUTTONS['Menu']:
            self.all_sprites.append(const.draw_button(
                self, *btn[0], message=btn[1], picture=btn[2], font=60
            ))

    def work(self):
        btns = const.BUTTONS['Menu']
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    const.terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if const.check_click(btns[0], event):
                        self.dead()
                        Choose_game.Window().work()
                        return
                    elif const.check_click(btns[1], event):
                        self.dead()
                        Settings.Window().work()
                        return
                    elif const.check_click(btns[2], event):
                        const.terminate()

            pygame_widgets.update(events)
            pygame.display.flip()
