from .base_scene import Scene


class IntroductionScene(Scene):
    def __init__(self, game, **kwargs):
        super().__init__(game)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def _blit(self):
        self.screen.fill(self.base_background_color)

    def start(self):
        tick = 0
        while tick <= 10:
            self._blit()
            self.pygame.display.flip()
            self.clock.tick(1500)
            tick += 1
        return True
