"""~+~+[csr]+~+~"""

import pygame
from pygame.locals import *

from characters import (
    Comet,
    Enemy,
    Skarlet,
    Star
)


class Game(object):

    DIMENSIONS = (696, 696)

    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(10, 100)
        pygame.display.set_caption("<{+}> Find yourself <{+}>")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.DIMENSIONS, RESIZABLE)
        self.skarlet = Skarlet()

    def main(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                pygame.event.pump()
                key = pygame.key.get_pressed()    
                if key[K_ESCAPE]:
                    running = False
                self.skarlet.state(key)
            self.screen.fill((22, 5, 190,))
            self.screen.blit(self.skarlet.img, self.skarlet.rect)
            pygame.display.update()
            self.clock.tick(696)
        pygame.quit()
    

if __name__ == "__main__":
    Game().main()

    
    


    

    



    



