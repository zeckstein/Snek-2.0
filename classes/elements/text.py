import pygame
from utils import Color


class Text:
    def __init__(
        self,
        text: str,
        font_size: int,
        font_color: Color = Color.WHITE,
        x: int = 0,
        y: int = 0,
        alignment: str = "center",
        font_name: str = None,
    ):
        self.text = text
        self.font_size = font_size
        self.font_color = font_color.value
        self.alignment = alignment
        self.font_name = font_name
        self.font = pygame.font.SysFont(font_name, font_size)
        self.rendered_text = self.font.render(self.text, True, self.font_color)
        self._set_position(x, y)

    def _set_position(self, x, y):
        text_width, text_height = self.font.size(self.text)
        if self.alignment == "left":
            self.position = (x, y)
        elif self.alignment == "center":
            self.position = (x - text_width // 2, y - text_height // 2)
        elif self.alignment == "right":
            self.position = (x - text_width, y - text_height // 2)

    def update_position(self, new_x, new_y):
        self._set_position(new_x, new_y)

    def draw(self, surface):
        surface.blit(self.rendered_text, self.position)

    # TODO  review these methods
    def update_text(self, new_text):
        self.text = new_text
        self.rendered_text = self.font.render(self.text, True, self.font_color)
        self.update_position(self.position[0], self.position[1])

    def update_font_size(self, new_font_size):
        self.font_size = new_font_size
        self.font = pygame.font.SysFont(self.font_name, new_font_size)
        self.rendered_text = self.font.render(self.text, True, self.font_color)
        self.update_position(self.position[0], self.position[1])

    def update_font_color(self, new_font_color):
        self.font_color = new_font_color
        self.rendered_text = self.font.render(self.text, True, self.font_color)

    def update_font_name(self, new_font_name):
        self.font_name = new_font_name
        self.font = pygame.font.SysFont(new_font_name, self.font_size)
        self.rendered_text = self.font.render(self.text, True, self.font_color)
        self.update_position(self.position[0], self.position[1])
