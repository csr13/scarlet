"""~+~+[csr]+~+~"""

import os
import random

import pygame
from pygame.locals import *


IMAGES = os.path.join("assets", "images")


class Skarlet(pygame.sprite.Sprite):
    """
    ~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+
    <{+}> Mess with the best, die like the rest. <{+}>
    ~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+
    """
    
    DIMENSIONS = (696, 696,)

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(os.path.join(IMAGES, "skarlet.png"))
        self.rect = self.img.get_rect()
        self.alive = True
        self.life_points = 300
        self.speed = 20
        self.keys = {
            K_RIGHT: (self.speed, 0), 
            K_LEFT: (-self.speed, 0), 
            K_DOWN: (0, self.speed),
            K_UP: (0, -self.speed), 
        }
        self.rect[0], self.rect[1] = (696 // 2, 660)
    
    def get_position(self) -> tuple:
        return self.rect[0], self.rect[1]
    
    def check_screen_boundaries(self) -> None:
        x, y = self.get_position()
        if x <= 0:
            self.rect[0] = 1
        if x >= 660:
            self.rect[0] = 660
        if y >= 660:
            self.rect[1] = 660
        if y <= 0:
            self.rect[1] = 1
    
    def state(self, key: int) -> bool:
        for move, vector in self.keys.items():
            if key[move]:
                self.rect.move_ip(vector)
        self.check_screen_boundaries()
        return True


class Star(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
    def update(self):
        return 


class Comet(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        return 


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        return


