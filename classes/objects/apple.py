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

    def update(self, screen: pygame.Surface):
        # TODO get current playing field size instead of min
        self.rect.x = random.randrange(0, screen.get_width(), INCREMENT)
        self.rect.y = random.randrange(0, screen.get_height(), INCREMENT)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
