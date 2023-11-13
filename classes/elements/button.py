import pygame
from typing import Callable, Optional
from config import Color

# TODO think about length based on text length?


class Button:
    def __init__(
        self,
        text: str,
        width: int,
        height: int,
        x: int,
        y: int,
        alignment: str = "center",
        font_size: int = 30,
        bg_color: Color = Color.WHITE,
        text_color: Color = Color.BLACK,
        hover_color: Color = Color.LIGHT_GRAY,
        click_color: Color = Color.GRAY,
        callback: Optional[Callable[[], None]] = None,
    ):
        self.alignment = alignment
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.bg_color = bg_color.value
        self.text_color = text_color.value
        self.hover_color = hover_color.value
        self.click_color = click_color.value
        self.callback = callback
        self.clicked = False
        self.hovered = False

        self._set_position(x, y)

    def _set_position(self, x, y):
        if self.alignment == "left":
            self.rect.x = x
            self.rect.y = y
        elif self.alignment == "center":
            self.rect.center = (x, y)
        elif self.alignment == "right":
            self.rect.right = x
            self.rect.y = y

    def update_position(self, new_x, new_y):
        self._set_position(new_x, new_y)

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
                if self.callback:
                    self.callback()
                self.clicked = False
        elif event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hovered = True
            else:
                self.hovered = False
                self.clicked = False
