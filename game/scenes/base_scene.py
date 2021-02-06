class Scene(object):
    def __init__(self, pygame, display, screen, clock):
        self.pygame = pygame
        self.display = display
        self.clock = clock
        self.screen = screen

    def _update_group(self, group, screen):
        list(map(lambda this: this.update(), group))

    def _draw_group(self, group, screen):
        list(map(lambda thing: thing.draw(screen), group))
