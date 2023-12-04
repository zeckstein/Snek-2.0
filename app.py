import sys
import pygame
import scenes

from options import Options

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

# Initialize sounds and Pygame
pygame.init()
# Set up the window
options = Options()
screen = pygame.display.set_mode((options.screen_width, options.screen_height))
pygame.display.set_caption("Snek")


# Run the game loop
running = True
while running:
    scenes.main_menu(screen)


# Quit Pygame
pygame.quit()
sys.exit()
