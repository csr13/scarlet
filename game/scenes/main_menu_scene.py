"""~+~+[csr]+~+~"""

import sys

sys.path.append("..")

from collections import OrderedDict

from pygame.locals import K_ESCAPE, K_RETURN, K_1, K_2

from .base_scene import Scene
from utils.text_utils import Text


class MainMenu(Scene):
    def __init__(self, game, **kwargs):
        super().__init__(game)
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.text_refs = OrderedDict()
        self.dirty_rects = []
        self.options = OrderedDict(
            [
                (self.first_level.__doc__, self.first_level),
                (self.credits.__doc__, self.credits),
            ]
        )

    def display_main_menu_options(self):
        i = 0
        for num, key in enumerate(self.options.keys(), start=0):
            kwargs = {"size": 30, "color": "green"}
            text = Text(key, (250, 250 + i), **kwargs)
            text.draw(self.screen)
            self.dirty_rects.append(text)
            self.text_refs[num] = text
            i += 80

    def display_menu_banner(self):
        kwargs = {"color": "red", "size": 69}
        text = Text("Scarlet", (225, 69), **kwargs)
        text.draw(self.screen)
        self.dirty_rects.append(text)

    def option_animation(self, option: Text):
        position = (option.x, option.y)
        selection = self.pygame.Surface(option.img.get_size())
        selection.fill((0, 0, 255))
        selection_blit = self.screen.blit(selection, position)
        self.dirty_rects.append(selection_blit)

    def start(self):

        running = True
        while running:
            self.screen.fill(self.base_background_color)
            for event in self.pygame.event.get():
                self.pygame.event.pump()
                key = self.pygame.key.get_pressed()

                if key[K_ESCAPE]:
                    running = False
                elif key[K_RETURN]:
                    self.first_level()
                elif key[K_1]:
                    text_ref = self.text_refs[0]
                    self.option_animation(text_ref)
                    self.first_level()
                elif key[K_2]:
                    text_ref = self.text_refs[1]
                    self.option_animation(text_ref)
                    self.credits()

            self.display_menu_banner()
            self.display_main_menu_options()

            self.pygame.display.update(self.dirty_rects)
            self.dirty_rects = []
            self.clock.tick(10)
        self.pygame.quit()

    def credits(self):
        """2) See Credits."""
        self.set_title_display("Scarlet | Credits")
        self.dirty_rects = []
        running = True
        while running:

            self.screen.fill(self.base_background_color)
            for event in self.pygame.event.get():
                self.pygame.event.pump()
                key = self.pygame.key.get_pressed()
                if key[K_ESCAPE]:
                    running = False
                elif key[K_RETURN]:
                    running = False

                self.pygame.display.update(self.dirty_rects)
                self.dirty_rects = []
            self.clock.tick(10)

    def first_level(self):
        """1) Start Game."""
        running = False
        while running:
            for event in self.pygame.event.get():
                self.pygame.event.pump()
                key = self.pygame.key.get_pressed()
                if key[K_ESCAPE]:
                    running = False
            self.clock.tick(1500)
