import pygame
import logging
from classes.elements.text import Text
from classes.elements.button import Button
import scenes
from utils import Color
from config import MINIMUM_WIDTH, MINIMUM_HEIGHT, FPS


def main_menu(screen: pygame.Surface):
    logging.info("Entering main menu")

    # text
    game_title = Text("Snek", 50, Color.WHITE, screen.get_width() // 2, 100)
    menu_title = Text("Main Menu", 30, Color.WHITE, screen.get_width() // 2, 200)

    # buttons
    play_button = Button(
        "Play",
        200,
        50,
        screen.get_width() / 2,
        screen.get_height() / 2,
        bg_color=Color.GREEN,
        hover_color=Color.LIGHT_GREEN,
        click_color=Color.DARK_GREEN,
        callback=lambda: scenes.play_Snek(screen),
    )
    quit_button = Button(
        "Quit",
        200,
        50,
        screen.get_width() / 2,
        screen.get_height() / 2 + 100,
        bg_color=Color.RED,
        hover_color=Color.LIGHT_RED,
        click_color=Color.DARK_RED,
        callback=lambda: running.update({"running": False}),
    )
    # place all the things you want drawn here
    drawn_objects_with_handle_event = [play_button, quit_button]
    objects_to_draw = [
        *drawn_objects_with_handle_event,
        game_title,
        menu_title,
    ]

    # stop all music then play this scene's track
    # TODO make this a utils function and in all scenes (just play_Snek for now)
    pygame.mixer.stop()
    bg_music_menu = pygame.mixer.Sound(
        "assets/sounds/2019-01-02_-_8_Bit_Menu_-_David_Renda_-_FesliyanStudios.com.mp3",
    )
    bg_music_menu.play(-1)

    # game loop
    running = True
    while running:
        pygame.display.set_caption("Snek - Main Menu")
        _handle_events(screen, play_button, quit_button)
        _draw(screen, objects_to_draw)

    pygame.quit()
    quit()


def _handle_events(screen: pygame.Surface, *args):
    """Screen and any number of objects with handle_event(event) methods.

    Args:
        screen (pygame.Surface): main screen
        *args: any number of objects with handle_event(event) methods
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                scenes.play_Snek(screen)

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

        for arg in args:
            arg.handle_event(event)


def _draw(screen: pygame.Surface, objects_to_draw: list):
    screen.fill(Color.BLACK.value)
    for obj in objects_to_draw:
        obj.draw(screen)
    pygame.display.update()
