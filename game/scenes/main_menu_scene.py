"""~+~+[csr]+~+~"""

import sys

sys.path.append("..")

from collections import OrderedDict

from pygame.locals import K_ESCAPE, K_RETURN

from .base_scene import Scene
from utils.text_utils import Text


class MainMenu(Scene):
    def __init__(self, pygame, display, screen, clock, game, **kwargs):
        super().__init__(pygame, display, screen, clock)
        self.game = game
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.options = OrderedDict(
            [
                (self.first_level.__doc__, self.first_level),
                (self.credits.__doc__, self.credits),
            ]
        )

    def display_main_menu_options(self):
        i = 0
        for k, v in self.options.items():
            text = Text(k, (250, 250 + i), **{"size": 30, "color": "green"})
            text.render()
            text.draw(self.screen)
            i += 80

    def display_menu_banner(self):
        text = Text("Scarlet", (225, 69), **{"color": "red", "size": 69})
        text.render()
        text.draw(self.screen)

    def start(self):
        self.display_menu_banner()
        self.display_main_menu_options()
        running = True
        while running:
            for event in self.pygame.event.get():
                self.pygame.event.pump()
                key = self.pygame.key.get_pressed()
                if key[K_ESCAPE]:
                    running = False
                elif key[K_RETURN]:
                    self.first_level()
            self.pygame.display.flip()
            self.clock.tick(1500)
        self.pygame.quit()

    def credits(self):
        """2) See Credits."""
        running = False
        while running:
            for event in self.pygame.event.get():
                self.pygame.event.pump()
                key = self.pygame.key.get_pressed()
                if key[K_ESCAPE]:
                    running = False
                elif key[K_RETURN]:
                    running = False
            self.pygame.display.flip()
            self.clock.tick(1500)

    def first_level(self):
        """1) Start Game."""
        running = False
        while running:
            for event in self.pygame.event.get():
                self.pygame.event.pump()
                key = self.pygame.key.get_pressed()
                if key[K_ESCAPE]:
                    running = False
            self.pygame.display.flip()
            self.clock.tick(1500)
        self.pygame.quit()
