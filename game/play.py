"""~+~+[csr]+~+~"""

import pygame
from pygame.locals import *

from characters.comet import Comet
from characters.skarlet import Skarlet
from characters.star import Star
from scenes.introduction_scene import IntroductionScene
from scenes.main_menu_scene import MainMenu


class Game(object):

    DIMENSIONS = (696, 696)

    caption = None
    skarlet = None
    enemies = None
    comets = None
    stars = None
    scene = None

    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(10, 100)
        pygame.display.set_caption("Deep in the heart of nowhere")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.DIMENSIONS, RESIZABLE)
        self.scene = IntroductionScene(
            pygame, pygame.display, self.screen, self.clock
        )
        self.skarlet = Skarlet()
        self.stars = pygame.sprite.Group()
        self.comets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

    def set_scene(self, scene):
        scene = scene(pygame, pygame.display, self.screen, self.clock, self)
        self.scene = scene

    def _replicate(self):
        Comet.factory(self.comets)
        Star.factory(self.stars)

    def main(self):
        if self.scene.start():
            self.set_scene(MainMenu)
        self.scene.start()


if __name__ == "__main__":
    Game().main()
