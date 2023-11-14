import pygame
import logging

from classes.objects.apple import Apple
from classes.objects.snek import Snek
import scenes

from config import MINIMUM_WIDTH, MINIMUM_HEIGHT, FPS


def play_Snek(screen: pygame.Surface, FPS: int):  # TODO update params, global options
    """Gives control of passed screen for Snek game.

    Args:
        screen (pygame.Surface): pygame surface, intended main window
    """
    pygame.display.set_caption("Snek - PLAY")
    clock = pygame.time.Clock()
    # game objects
    snek = Snek(screen)
    apple = Apple(screen)
    # buttons

    # text

    # score
    score = 0

    while True:
        # game objects
        clock.tick(FPS)
        _handle_input(snek, screen)
        _game_logic(snek, apple, screen)
        _draw(snek, apple, screen)
    pygame.quit()
    quit()


def _handle_input(snek: Snek, screen: pygame.Surface):
    """Handles pygame events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            pygame.quit()
            quit()

        # TODO maintain minimum window size, update to follow option settings (MAKE NOT RESIZEABLE?)
        if event.type == pygame.VIDEORESIZE:
            logging.debug("resize event: %s", event)
            if screen.get_width() < MINIMUM_WIDTH:
                screen = pygame.display.set_mode(
                    (MINIMUM_WIDTH, screen.get_height()), pygame.RESIZABLE
                )
                logging.debug("width below min")
            if screen.get_height() < MINIMUM_HEIGHT:
                screen = pygame.display.set_mode(
                    (screen.get_width(), MINIMUM_HEIGHT), pygame.RESIZABLE
                )
                logging.debug("height below min")

        # START OF KEYED INPUTS DURING GAME
        if event.type == pygame.KEYDOWN:
            snek.handle_event(event.key)


def _game_logic(snek: Snek, apple: Apple, screen: pygame.Surface):
    # see if Snek is intersecting Apple
    snek.update()
    if pygame.sprite.collide_rect(snek.head, apple):
        snek.grow()
        apple.update(screen)

    # add collision detection for if snek.head.rect.center is outside screen.get_width() and screen.get_height()
    # TODO does this belong in the snek class?
    if (
        snek.head.rect.centerx < 0
        or snek.head.rect.centerx > screen.get_width()
        or snek.head.rect.centery < 0
        or snek.head.rect.centery > screen.get_height()
    ):
        scenes.main_menu(screen, FPS)


def _draw(snek: Snek, apple: Apple, screen: pygame.Surface):
    screen.fill("black")
    apple.draw(screen)
    snek.draw(screen)
    pygame.display.flip()
