import pygame
import logging

from classes.objects.apple import Apple
from classes.objects.snek import Snek

from config import MINIMUM_WIDTH, MINIMUM_HEIGHT


def play_Snek(screen, FPS):  # TODO update params, global options
    """Gives control of passed screen for Snek game.

    Args:
        screen (pygame.Surface): pygame surface, intended main window
    """
    pygame.display.set_caption("Snek")
    clock = pygame.time.Clock()
    # game objects
    snek = Snek()
    apple = Apple()
    # buttons

    # text

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

        # TODO maintain minimum window size
        # TODO add flags to larger resize for bigger game scale
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
            direction = None
            if event.key == pygame.K_LEFT:
                direction = "left"
            if event.key == pygame.K_RIGHT:
                direction = "right"
            if event.key == pygame.K_UP:
                direction = "up"
            if event.key == pygame.K_DOWN:
                direction = "down"

            snek.update_direction(direction)


def _game_logic(snek: Snek, apple: Apple, screen: pygame.Surface):
    # see if Snek is intersecting Apple
    snek.move()
    if pygame.sprite.collide_rect(snek, apple):
        snek.grow()
        apple.update()

    # add collision detection for snek and wall
    if (
        snek.rect.x < 0
        or snek.rect.x > screen.get_width() - snek.rect.width
        or snek.rect.y < 0
        or snek.rect.y > screen.get_height() - snek.rect.height
    ):
        pygame.quit()
        quit()


def _draw(snek: Snek, apple: Apple, screen: pygame.Surface):
    screen.fill("black")
    apple.draw(screen)
    snek.draw(screen)
    pygame.display.flip()
