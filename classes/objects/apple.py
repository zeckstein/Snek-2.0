import random
import pygame
from utils import load_image

# TODO check config and screen stuff
from config import MINIMUM_WIDTH as WIDTH, MINIMUM_HEIGHT as HEIGHT, INCREMENT


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("apple")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH, INCREMENT)
        self.rect.y = random.randrange(0, HEIGHT, INCREMENT)

    def update(self):
        # TODO get current playing field size instead of min
        self.rect.x = random.randrange(0, WIDTH, INCREMENT)
        self.rect.y = random.randrange(0, HEIGHT, INCREMENT)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
