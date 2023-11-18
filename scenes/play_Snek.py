import pygame
import logging
from classes.objects.apple import Apple
from classes.objects.snek import Snek
import scenes
from config import MINIMUM_WIDTH, MINIMUM_HEIGHT, FPS


def play_Snek(screen: pygame.Surface):  # TODO update params, global options
    """Gives control of passed screen for Snek game.

    Args:
        screen (pygame.Surface): pygame surface, intended main window
    """
    logging.info("Entering Snek game")

    pygame.display.set_caption("Snek - PLAY")

    # game objects
    clock = pygame.time.Clock()
    snek = Snek(screen)
    apple = Apple(screen)

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

        # TODO maintain minimum window size, update to follow option settings (MAKE NOT RESIZABLE?)
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
    if snek.update(screen) == False:
        scenes.main_menu(screen)
    if pygame.sprite.collide_rect(snek.head, apple):
        snek.grow()
        apple.update(screen)
        # check if apple is under snek
        # TODO check when there is nospace left for apple

        while pygame.sprite.spritecollideany(apple, snek):
            apple.update(screen)
            logging.debug("apple under snek, watch out for infinity if you can WIN!")


def _draw(snek: Snek, apple: Apple, screen: pygame.Surface):
    screen.fill("black")
    apple.draw(screen)
    snek.draw(screen)
    pygame.display.flip()
