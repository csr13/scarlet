from pygame import Color, font


class Text(object):
    def __init__(self, value, xy, **extra):
        self.value = value
        self.x, self.y = xy

        if "font" in extra:
            self.font = extra.get("font")
        else:
            self.font = "ubuntumono"

        if "size" in extra:
            self.size = extra.get("size")
        else:
            self.size = 69

        if "color" in extra:
            self.color = Color(extra.get("color"))
        else:
            self.color = Color("black")

        self.set_font()
        self.render()

    def set_font(self):
        self.font = font.SysFont(self.font, self.size)

    def render(self):
        self.img = self.font.render(self.value, 2, self.color)
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.img, self.rect)
