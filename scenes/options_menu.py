from pathlib import Path
import pygame
import logging
from classes.elements import Text, Button, TextInput
import scenes
from utils import Color
from config import MINIMUM_WIDTH, MINIMUM_HEIGHT

base_dir = Path(__file__).resolve().parent.parent


# (#TODO add option controls)
def options_menu(screen: pygame.Surface):
    logging.info("Entering OPTIONS menu")

    # text
    menu_title = Text("Options Menu", 50, Color.WHITE, screen.get_width() // 2, 100)
    note_text = Text(
        "Under Construction", 30, Color.WHITE, screen.get_width() // 2, 200
    )

    # TODO REVIEW THIS
    # TEXT INPUT TEST
    text_input = TextInput(border_color=Color.PURPLE, border_width=2)

    # buttons
    back_button = Button(
        "Back",
        200,
        50,
        screen.get_width() / 2,
        screen.get_height() / 2,
        bg_color=Color.YELLOW,
        hover_color=Color.LIGHT_YELLOW,
        click_color=Color.DARK_YELLOW,
        callback=lambda: scenes.main_menu(screen),
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
    drawn_objects_with_handle_event = [text_input, back_button, quit_button]
    objects_to_draw = [
        *drawn_objects_with_handle_event,
        menu_title,
        note_text,
    ]

    # game loop
    running = True
    while running:
        pygame.display.set_caption("Snek - Options Menu")
        _handle_events(screen, *drawn_objects_with_handle_event)
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
