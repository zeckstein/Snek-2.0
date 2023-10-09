import pygame
from utils import load_image
from config import MINIMUM_WIDTH, MINIMUM_HEIGHT, INCREMENT

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)
"""IMPLEMENT SPRITE GROUPS, 
This just tests displaying ad moving the head
MAYBE try to get resizable scale working also
"""


class Snek(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # number of body segments / ALSO == score basically
        self.size = 1
        # initial direction RIGHT
        self.vx = INCREMENT
        self.vy = 0

        # TODO add body ad tail images and parts
        self.head_image = load_image("head")

        # TODO TEMPORARY
        self.rect = self.head_image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update_direction(self, direction):
        """
        TODO Needs to be updated to velocity based on scale, and velocity by clock tick
        limit to 1 increment per clock tick NO DIAGONALS
        """
        if direction == "left":
            self.vx = -INCREMENT
            self.vy = 0
        if direction == "right":
            self.vx = INCREMENT
            self.vy = 0
        if direction == "up":
            self.vx = 0
            self.vy = -INCREMENT
        if direction == "down":
            self.vx = 0
            self.vy = INCREMENT

        logging.debug("snek direction: %s", direction)

    def move(self):
        """needs to contain rotation and movement of body and tail"""
        self.rect.x += self.vx
        self.rect.y += self.vy

    def grow(self):
        self.size += 1
        logging.debug("snek size: %s", self.size)

    def draw(self, surface):
        """
        TODO Still needs to draw body (number of segments) and tail,
        all facing the correct direction.
        """
        surface.blit(self.head_image, (self.rect.x, self.rect.y))
