from pathlib import Path
import pygame
import logging
from classes.objects.apple import Apple
from classes.objects.snek import Snek
import scenes
from config import FPS


base_dir = Path(__file__).resolve().parent.parent
# snek game music by tempo
bg_music_snek_slow = pygame.mixer.Sound(
    base_dir
    / "assets/sounds/bg_music/Slower-Tempo-2020-03-22_-_8_Bit_Surf_-_FesliyanStudios.com_-_David_Renda.mp3"
)


def play_Snek(screen: pygame.Surface) -> None:  # TODO update params, global options
    """Gives control of passed screen for Snek game.

    Args:
        screen (pygame.Surface): pygame surface, intended main window
    """
    logging.info("Entering Snek GAME")

    pygame.display.set_caption("Snek - PLAY")

    # game objects
    clock = pygame.time.Clock()
    snek = Snek(screen)
    apple = Apple(screen)

    # text

    # stop all music then play this scene's track
    pygame.mixer.stop()
    bg_music_snek_slow.play(-1)

    # insert a sleep to allow music to start
    intro_sleep = True

    while True:
        # game objects
        clock.tick(FPS)
        _handle_input(screen, snek)
        _game_logic(screen, snek, apple)
        _draw(screen, snek, apple)

        # minor pause for music
        # TODO READY, GO! progressive text
        if intro_sleep:
            pygame.time.delay(500)
            intro_sleep = False
    pygame.quit()
    quit()


def _handle_input(screen: pygame.Surface, snek: Snek) -> None:
    """Handles pygame events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            pygame.quit()
            quit()

        # START OF KEYED INPUTS DURING GAME
        if event.type == pygame.KEYDOWN:
            snek.handle_event(event.key)


def _game_logic(screen: pygame.Surface, snek: Snek, apple: Apple) -> None:
    # see if Snek is intersecting Apple
    chomp = False
    # check if head will touch apple on next move
    if (
        snek.head.rect.x + snek.vx == apple.rect.x
        and snek.head.rect.y + snek.vy == apple.rect.y
    ):
        chomp = True
    if pygame.sprite.collide_rect(snek.head, apple):
        apple.update(screen)
    if snek.update(screen, chomp) == False:
        pygame.mixer.stop()
        scenes.main_menu(screen)

        # check if apple is under snek, TODO update so apple only chooses from open spaces
        # TODO check when there is nospace left for apple

        while pygame.sprite.spritecollideany(apple, snek):
            apple.update(screen)
            logging.debug("apple under snek, watch out for infinity if you can WIN!")


def _draw(screen: pygame.Surface, snek: Snek, apple: Apple) -> None:
    screen.fill("black")
    apple.draw(screen)
    snek.draw(screen)
    pygame.display.flip()
