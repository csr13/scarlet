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
        self.image = pygame.image.load(os.path.join(IMAGES, "skarlet.png"))
        self.rect = self.image.get_rect()
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

class Comet(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        return 

class Laser(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        return 

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        return


