"""~+~+[csr]+~+~"""

import pygame
from pygame.locals import *

from characters import (
    Comet,
    Enemy,
    Laser,
    Skarlet,
    Star
)

class Game(object):

    DIMENSIONS = (696, 696)

    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(10, 100)
        pygame.display.set_caption("Deep in the heart of nowhere")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.DIMENSIONS, RESIZABLE)
        self.skarlet = Skarlet()
        self.stars = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

    def _update(self) -> None:
        for star in self.stars:
            star.update()

    def _draw(self) -> None:
        for star in self.stars:
            star.draw(self.screen)
    
    def _blit(self, color: tuple=(0, 0, 130)) -> None:
        self.screen.fill(color)
        self.screen.blit(self.skarlet.image, self.skarlet.rect)
    
    def _replicate(self):
        Star().factory(self.stars)

    def main(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                pygame.event.pump()
                key = pygame.key.get_pressed()    
                if key[K_ESCAPE]:
                    running = False
                self.skarlet.state(key)
            self._replicate()
            self._blit() 
            self._update()
            self._draw()
            pygame.display.update()
            self.clock.tick(696)
        pygame.quit()
    

if __name__ == "__main__":
    Game().main()

    
    


    

    



    



