import sys
from pathlib import Path
import pygame
import logging
from classes.elements import Text, Button
import scenes
from utils import Color
from options import Options

base_dir = Path(__file__).resolve().parent.parent
# get the options instance
options = Options()


# (#TODO add option controls)
def options_menu(screen: pygame.Surface):
    logging.info("Entering OPTIONS menu")

    screen_width = screen.get_width()

    # text
    menu_title = Text(
        "Options Menu",
        50,
        Color.WHITE,
        screen_width / 2,
        screen.get_height() / 10,
    )

    # Available options
    speed_option = Text(
        "Speed", 50, Color.WHITE, screen_width / 3.5, 300, alignment="right"
    )

    # speed options buttons
    speed_slow_button = Button(
        "Slow",
        80,
        50,
        screen_width / 2 - 90 + (screen_width * 0.05),
        300,
        bg_color=Color.YELLOW,
        hover_color=Color.LIGHT_YELLOW,
        click_color=Color.DARK_YELLOW,
        callback=lambda: options.update_speed(3),
    )

    speed_medium_button = Button(
        "Medium",
        80,
        50,
        screen_width / 2 + (screen_width * 0.05),
        300,
        bg_color=Color.YELLOW,
        hover_color=Color.LIGHT_YELLOW,
        click_color=Color.DARK_YELLOW,
        callback=lambda: options.update_speed(5),
    )

    speed_fast_button = Button(
        "Fast",
        80,
        50,
        screen_width / 2 + 90 + (screen_width * 0.05),
        300,
        bg_color=Color.YELLOW,
        hover_color=Color.LIGHT_YELLOW,
        click_color=Color.DARK_YELLOW,
        callback=lambda: options.update_speed(11),
    )

    size_option = Text(
        "Grid Size", 50, Color.WHITE, screen_width / 3.5, 200, alignment="right"
    )

    # size options buttons
    size_small_9_button = Button(
        "5",
        80,
        50,
        screen_width / 2 - 90 + (screen_width * 0.05),
        200,
        bg_color=Color.YELLOW,
        hover_color=Color.LIGHT_YELLOW,
        click_color=Color.DARK_YELLOW,
        callback=lambda: options.update_grid_size(5),
    )

    size_medium_15_button = Button(
        "15",
        80,
        50,
        screen_width / 2 + (screen_width * 0.05),
        200,
        bg_color=Color.YELLOW,
        hover_color=Color.LIGHT_YELLOW,
        click_color=Color.DARK_YELLOW,
        callback=lambda: options.update_grid_size(15),
    )

    size_large_21_button = Button(
        "25",
        80,
        50,
        screen_width / 2 + 90 + (screen_width * 0.05),
        200,
        bg_color=Color.YELLOW,
        hover_color=Color.LIGHT_YELLOW,
        click_color=Color.DARK_YELLOW,
        callback=lambda: options.update_grid_size(25),
    )
    
    # navigation buttons
    back_button = Button(
        "Back",
        200,
        50,
        screen_width / 2,
        (screen.get_height() * 0.75),
        bg_color=Color.YELLOW,
        hover_color=Color.LIGHT_YELLOW,
        click_color=Color.DARK_YELLOW,
        callback=lambda: scenes.main_menu(screen),
    )
    quit_button = Button(
        "Quit",
        200,
        50,
        screen_width / 2,
        (screen.get_height() * 0.75) + 70,
        bg_color=Color.RED,
        hover_color=Color.LIGHT_RED,
        click_color=Color.DARK_RED,
        callback=lambda: sys.exit(),
    )
    # place all the things you want drawn here
    drawn_objects_with_handle_event = [
        speed_slow_button,
        speed_medium_button,
        speed_fast_button,
        size_small_9_button,
        size_medium_15_button,
        size_large_21_button,
        back_button,
        quit_button,
    ]
    objects_to_draw = [
        *drawn_objects_with_handle_event,
        menu_title,
        size_option,
        speed_option,
    ]

    # game loop
    running = True
    while running:
        pygame.display.set_caption("Snek - Options Menu")
        _handle_events(screen, *drawn_objects_with_handle_event)
        _draw(screen, objects_to_draw)


def _handle_events(screen: pygame.Surface, *args):
    """Screen and any number of objects with handle_event(event) methods.

    Args:
        screen (pygame.Surface): main screen
        *args: any number of objects with handle_event(event) methods
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                scenes.main_menu(screen)

        for arg in args:
            arg.handle_event(event)


def _draw(screen: pygame.Surface, objects_to_draw: list):
    screen.fill(Color.BLACK.value)
    for obj in objects_to_draw:
        obj.draw(screen)
    pygame.display.update()
