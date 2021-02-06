from .base_scene import Scene


class IntroductionScene(Scene):
    def __init__(self, pygame, display, screen, clock, game, **kwargs):
        super().__init__(pygame, display, screen, clock)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def _blit(self, color=(0, 0, 69)):
        self.screen.fill(color)

    def start(self):
        tick = 0
        while tick <= 10:
            self._blit()
            self.pygame.display.flip()
            self.clock.tick(1500)
            tick += 1
        return True
