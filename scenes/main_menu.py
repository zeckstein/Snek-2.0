import pygame
import logging
from classes.elements.text import Text
from classes.elements.button import Button
from config import Color
import scenes


def main_menu(screen: pygame.Surface, FPS: int):
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
        callback=lambda: scenes.play_Snek(screen, FPS),
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
        callback=lambda: pygame.quit(),
    )

    # game loop
    while True:
        pygame.display.set_caption("Snek - Main Menu")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            play_button.handle_event(event)
            quit_button.handle_event(event)

        # draw
        screen.fill(Color.BLACK.value)
        game_title.draw(screen)
        menu_title.draw(screen)
        play_button.draw(screen)
        quit_button.draw(screen)
        pygame.display.update()
