import const

import pygame
import pygame_widgets

import start

import Menu


class Window(start.Window_Activation):
    def __init__(self):
        super(Window, self).__init__()
        self.screen.fill((139, 69, 19))

        for btn in const.BUTTONS['Settings']:
            self.all_sprites.append(
                const.draw_button(self, *btn[0], message=btn[1], picture=btn[2], font=60))

    def work(self):
        btns = const.BUTTONS['Settings']
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    const.terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if const.check_click(btns[0], event):
                        self.dead()
                        Menu.Start().work()
                        return

            pygame_widgets.update(events)
            pygame.display.flip()
