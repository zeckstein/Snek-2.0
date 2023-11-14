import pygame
from utils import load_image
from config import MINIMUM_WIDTH, MINIMUM_HEIGHT, INCREMENT

import logging

"""IMPLEMENT SPRITE GROUPS, 
This just tests displaying ad moving the head
MAYBE try to get resizable scale working also
"""

# TODO implement color selection?


class Segment(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center=position)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class Snek(pygame.sprite.Group):
    def __init__(self, screen: pygame.Surface):
        pygame.sprite.Group.__init__(self)
        # number of body segments / ALSO == score basically
        self.size = 3
        # initial direction RIGHT
        self.vx = INCREMENT
        self.vy = 0

        # TODO add body ad tail images and parts
        self.head_image = pygame.transform.rotate(load_image("head"), 270)
        self.body_image = load_image("body")
        self.tail_image = pygame.transform.rotate(load_image("tail"), 270)

        # Calculate initial positions
        head_start_pos = (
            (screen.get_width() // 2),
            (screen.get_height() // 2),
        )
        head_position = head_start_pos
        body_position = (head_start_pos[0] - INCREMENT, head_start_pos[1])
        tail_position = (head_start_pos[0] - 2 * INCREMENT, head_start_pos[1])

        self.head = Segment(self.head_image, head_position)
        self.body = [Segment(self.body_image, body_position)]
        self.tail = Segment(self.tail_image, tail_position)

        self.add(self.head)
        self.add(self.body[0])
        self.add(self.tail)

    def update_direction(self, event_key):
        """
        TODO Needs to be updated to velocity based on scale, and velocity by clock tick
        limit to 1 increment per clock tick NO DIAGONALS
        """
        if event_key == pygame.K_LEFT:
            self.vx = -INCREMENT
            self.vy = 0
            logging.debug("KEY LEFT")

        elif event_key == pygame.K_RIGHT:
            self.vx = INCREMENT
            self.vy = 0
            logging.debug("KEY RIGHT")

        elif event_key == pygame.K_UP:
            self.vx = 0
            self.vy = -INCREMENT
            logging.debug("KEY UP")

        elif event_key == pygame.K_DOWN:
            self.vx = 0
            self.vy = INCREMENT
            logging.debug("KEY DOWN")

        else:
            # continue same direction
            pass

    def grow(self):
        # Create a new body segment and add it to the group
        new_body_segment = Segment(self.body[0].image, self.tail.rect.center)
        self.body.insert(0, new_body_segment)
        self.add(new_body_segment)

    def move(self):
        # current center position of head
        initial_head_pos = self.head.rect.center
        # move head
        self.head.rect.center = (
            initial_head_pos[0] + self.vx,
            initial_head_pos[1] + self.vy,
        )

        # move first body segment to position of head before it moved
        self.body[0].rect.center = initial_head_pos

        # move tail

    def draw(self, surface: pygame.Surface):
        self.head.draw(surface)
        for segment in self.body:
            segment.draw(surface)
        self.tail.draw(surface)
