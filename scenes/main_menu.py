import pygame
import logging
from classes.elements.text import Text
from classes.elements.button import Button
from config import Color
import scenes


def main_menu(screen):
    logging.info("Entering main menu")

    # buttons

    # text

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
