import pygame


class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        text,
        font_size=30,
        bg_color=(255, 255, 255),
        text_color=(0, 0, 0),
        hover_color=(200, 200, 200),
        click_color=(150, 150, 150),
        callback=None,
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.bg_color = bg_color
        self.text_color = text_color
        self.hover_color = hover_color
        self.click_color = click_color
        self.callback = callback
        self.clicked = False
        self.hovered = False

    def draw(self, surface):
        color = self.bg_color
        if self.clicked:
            color = self.click_color
        elif self.hovered:
            color = self.hover_color
        pygame.draw.rect(surface, color, self.rect)
        text = self.font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
                self.clicked = False
        elif event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hovered = True
            else:
                self.hovered = False
                self.clicked = False
