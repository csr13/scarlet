"""~+~+[csr]+~+~"""

import os
import random

import pygame
from pygame.locals import *


class Star(pygame.sprite.Sprite):
    """
    ~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~
    <{*}> Stars of the midnight range, shining through the light,
    guide my way tonight. <{*}>
    ~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1,1))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect[0] = random.randint(0, 669)
        self.rect[1] = 0
        self.speed = 1  
    
    @staticmethod
    def factory(group: pygame.sprite.Group) -> None:
        if not int(random.random() * 96):
            group.add(Star())

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

    def update(self) -> None:
        self.rect[1] += self.speed 
        if self.rect[1] >= 696:
            self.kill()

