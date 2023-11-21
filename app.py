import pygame

from classes.objects.apple import Apple
from classes.objects.snek import Snek

import scenes

from config import MINIMUM_WIDTH, MINIMUM_HEIGHT, FPS

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

# Initialize sounds and Pygame
pygame.init()
# Set up the window
screen = pygame.display.set_mode((MINIMUM_WIDTH, MINIMUM_HEIGHT))
pygame.display.set_caption("Snek")


# Run the game loop
running = True
while running:
    scenes.main_menu(screen)


# Quit Pygame
pygame.quit()
quit()
