"""~+~+[csr]+~+~"""

import os
import random

import pygame
from pygame.locals import *


IMAGES = os.path.join("assets", "images")


class Skarlet(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(os.path.join(IMAGES, "skarlet.png"))
        self.rect = self.img.get_rect()
        self.alive = True
        self.life_points = 300
        self.speed = 20

    def state(self, key):
        if key[K_UP]:
             pass 
        if key[K_DOWN]:
            pass 
        if key[K_RIGHT]:
            pass
        if key[K_LEFT]:
            pass
        return true 

    def update(self):
        pass 


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


