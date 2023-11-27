import pygame
from utils import Color
import time


class TextInput:
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        min_width: int = 140,
        size: int = 32,
        background_color: Color = Color.WHITE,
        text_color: Color = Color.BLACK,
        border_color: Color = Color.BLACK,  # Add border color parameter
        border_active_color: Color = Color.BLUE,  # Add border active color parameter
        border_width: int = 1,  # Add border width parameter
        hover_color: Color = Color.GRAY,  # Add hover color parameter
    ):
        self.min_width = min_width
        self.cur_width = min_width
        self.rect = pygame.Rect(x, y, self.cur_width, size)  # Tie height to font size
        self.font = pygame.font.Font(None, size)
        self.text = ""
        self.background_color = background_color.value
        self.text_color = text_color.value
        self.border_color = border_color.value  # Store border color
        self.border_active_color = (
            border_active_color.value
        )  # Store border active color
        self.border_width = border_width  # Store border width
        self.hover_color = hover_color.value  # Store hover color
        self.active = False
        self.hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        if self.active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    # TODO update to delete multiple characters if backspace is held down
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

        self._on_hover(event)

    def _on_hover(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hovered = True
            else:
                self.hovered = False

    def draw(self, screen):
        # update width based on text length #TODO EXAMINE BECAUSE MESSY NAMING RESPONSIBILITIES
        text_surface, text_rect = self._text_length_based_resize()

        # draw text area
        pygame.draw.rect(screen, self.background_color, self.rect)

        # draw border
        if self.hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect, self.border_width)
        elif self.active:
            # change between border color and border active color every .5 seconds without swapping prop values
            if time.time() % 1 > 0.5:
                pygame.draw.rect(
                    screen, self.border_active_color, self.rect, self.border_width
                )
            else:
                pygame.draw.rect(
                    screen, self.border_color, self.rect, self.border_width
                )
        else:
            pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)

        # draw text
        screen.blit(text_surface, text_rect)

    def _text_length_based_resize(self):
        # #TODO update as option for left, center, or right
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(
            left=self.rect.left + self.border_width, centery=self.rect.centery
        )  # Left align text with space for border width, center vertically
        # update width based on text length
        self.cur_width = max(self.min_width, text_rect.width + (self.border_width * 2))

        return text_surface, text_rect
