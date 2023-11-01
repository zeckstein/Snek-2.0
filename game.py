import os
import pygame
from classes.apple import Apple
from classes.snek import Snek
from config import MINIMUM_WIDTH, MINIMUM_HEIGHT

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

# set min and max window size
MINIMUM_WIDTH = MINIMUM_WIDTH
MINIMUM_HEIGHT = MINIMUM_HEIGHT
# TODO move to config?
FPS = 5

## So window opens centered,/ might be for MS Windows only?
# os.environ["SDL_VIDEO_CENTERED"] = "1"
## BUT this apparently causes issue when i want to setmode for resize too small
## snaps the window to the center on resize instead of just initial open
## even when i put it in the init method i think


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snek")

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (MINIMUM_WIDTH, MINIMUM_HEIGHT), pygame.RESIZABLE
        )
        self.snek = Snek()
        self.apple = Apple()
        self.running = True

        # TODO add pause menu
        self.pause_menu = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self._handle_input()
            self._game_logic()
            self._draw()

        pygame.quit()

    def _handle_input(self):
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT or event.type == pygame.K_ESCAPE
            ):  # TODO update escape to open and close menu
                self.running = False

            # maintain minimum window size
            # TODO add flags to larger resize for bigger game scale
            if event.type == pygame.VIDEORESIZE:
                logging.debug("resize event: %s", event)
                if self.screen.get_width() < MINIMUM_WIDTH:
                    self.screen = pygame.display.set_mode(
                        (MINIMUM_WIDTH, self.screen.get_height()), pygame.RESIZABLE
                    )
                    logging.debug("width below min")
                if self.screen.get_height() < MINIMUM_HEIGHT:
                    self.screen = pygame.display.set_mode(
                        (self.screen.get_width(), MINIMUM_HEIGHT), pygame.RESIZABLE
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

                self.snek.update_direction(direction)

    def _game_logic(self):
        # see if Snek is intersecting Apple
        self.snek.move()
        if pygame.sprite.collide_rect(self.snek, self.apple):
            self.snek.grow()
            self.apple.update()

        # add collision detection for snek and wall
        if (
            self.snek.rect.x < 0
            or self.snek.rect.x > self.screen.get_width() - self.snek.rect.width
            or self.snek.rect.y < 0
            or self.snek.rect.y > self.screen.get_height() - self.snek.rect.height
        ):
            # TODO add game over and restart instead of quit
            self.running = False

    def _draw(self):
        self.screen.fill("black")
        self.apple.draw(self.screen)
        self.snek.draw(self.screen)
        pygame.display.flip()
