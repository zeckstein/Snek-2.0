import pygame


# TODO test this class
class Text:
    def __init__(self, text, font_size, font_color, x, y, font_name=None):
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.x = x
        self.y = y
        self.font_name = font_name
        self.font = (
            pygame.font.SysFont(font_name, font_size)
            if font_name
            else pygame.font.Font(None, font_size)
        )
        self.rendered_text = self.font.render(self.text, True, self.font_color)

    def draw(self, surface):
        surface.blit(self.rendered_text, (self.x, self.y))

    def update_text(self, new_text):
        self.text = new_text
        self.rendered_text = self.font.render(self.text, True, self.font_color)

    def update_font_size(self, new_font_size):
        self.font_size = new_font_size
        self.font = (
            pygame.font.SysFont(self.font_name, new_font_size)
            if self.font_name
            else pygame.font.Font(None, new_font_size)
        )
        self.rendered_text = self.font.render(self.text, True, self.font_color)

    def update_font_color(self, new_font_color):
        self.font_color = new_font_color
        self.rendered_text = self.font.render(self.text, True, self.font_color)

    def update_font_name(self, new_font_name):
        self.font_name = new_font_name
        self.font = pygame.font.SysFont(new_font_name, self.font_size)
        self.rendered_text = self.font.render(self.text, True, self.font_color)

    def update_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
