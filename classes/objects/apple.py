import random
import pygame
from utils import load_image

# TODO check config and screen stuff
from config import INCREMENT


class Apple(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("apple")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen.get_width(), INCREMENT)
        self.rect.y = random.randrange(0, screen.get_height(), INCREMENT)

    def update(self, screen: pygame.Surface) -> None:
        """update the apple position 
        #TODO check for snek collision OR open spaces? get passed the available spots?

        Args:
            screen (pygame.Surface): the game screen
        """
        self.rect.x = random.randrange(0, screen.get_width(), INCREMENT)
        self.rect.y = random.randrange(0, screen.get_height(), INCREMENT)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, (self.rect.x, self.rect.y))
