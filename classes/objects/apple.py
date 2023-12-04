import random
from typing import List, Tuple
import pygame
from utils import load_image

import logging

class Apple(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, scale: int):
        pygame.sprite.Sprite.__init__(self)
        # TODO make alpha version of apple sprite png
        self.scale = scale
        self.image = pygame.transform.scale(load_image("apple"), (self.scale, self.scale))
        self.rect = self.image.get_rect()
        # place to the right of dead center
        self.rect.center = (
            (screen.get_width() / 2) + self.scale * 2,
            screen.get_height() / 2,
        )


    def update(self, screen: pygame.Surface, blocked_coords: List[Tuple[int, int]]) -> None:
        """update the apple position
        #TODO check for snek collision OR open spaces? get passed the available spots?

        Args:
            screen (pygame.Surface): the game screen
            blocked_coords (List[Tuple[int, int]]): a list of (x, y) tuples representing blocked coordinates
        """
        width = screen.get_width()
        height = screen.get_height()
        board_coords = [(x, y) for x in range(0, width, self.scale) for y in range(0, height, self.scale)]
        logging.debug(f"Board coords: {board_coords}")
        logging.debug(f"Blocked coords: {blocked_coords}")
        valid_coords = [coord for coord in board_coords if coord not in blocked_coords]
        logging.debug(f"Valid coords: {valid_coords}")
        
        self.rect.x, self.rect.y = random.choice(valid_coords)
        logging.debug(f"Apple coords: {self.rect.x, self.rect.y}")

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)
