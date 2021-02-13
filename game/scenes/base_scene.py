"""~+~+~[csr]~+~+~"""


class Scene(object):
    def __init__(self, game):
        self.pygame = game.pygame
        self.display = game.pygame.display
        self.clock = game.clock
        self.screen = game.screen
        self.game = game
        self.base_background_color = (0, 0, 0)

    def set_title_display(self, value):
        self.display.set_caption(value)

    def set_tone(self):
        pass

    def _update_group(self, group, screen):
        list(map(lambda this: this.update(), group))

    def _draw_group(self, group, screen):
        list(map(lambda thing: thing.draw(screen), group))
