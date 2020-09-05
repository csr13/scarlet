"""~+~+[csr]+~+~"""

import os
import random

import pygame
from pygame.locals import *


IMAGES = os.path.join("assets", "images")

class Laser(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        return 
