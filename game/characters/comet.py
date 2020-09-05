"""~+~+[csr]+~+~"""

import os
import random
import sys 
sys.path.append("..")

import pygame
from pygame.locals import *

from settings import ASSETS_DIR

IMAGES = os.path.join(ASSETS_DIR, "images")


class Comet(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMAGES, "comet.png"))
        self.rect = self.image.get_rect()
        self.rect[0] = random.randint(0,669)
        self.rect[1] = 1
        self.speed = 1 
    
    @staticmethod
    def factory(group: pygame.sprite.Group) -> None:
        if not int(random.random() * 1500):
            group.add(Comet())
        if not int(random.random() * 2000):
            comet = Comet()
            comet.image = pygame.transform.rotozoom(comet.image, 1.3, 1.3)
            group.add(comet)
    
    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect[1] += self.speed
        if self.rect[1] >=696:
            self.kill()
