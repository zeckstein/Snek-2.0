import pygame
from utils import load_image
from config import MINIMUM_WIDTH, MINIMUM_HEIGHT, INCREMENT

import logging


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
        self._size = 1
        # initial direction RIGHT, velocity
        self.direction = "RIGHT"
        self.direction_list = []
        # TODO change INCREMENT to scale which should = size of head
        self.vx = INCREMENT
        self.vy = 0

        # TODO add body ad tail images and parts
        self.head_image = load_image("head")
        self.body_image = load_image("body")
        self.tail_image = load_image("tail")

        # Calculate initial positions
        head_start_pos = (
            (screen.get_width() // 2),
            (screen.get_height() // 2),
        )
        body_position = (head_start_pos[0] - INCREMENT, head_start_pos[1])
        tail_position = (head_start_pos[0] - 2 * INCREMENT, head_start_pos[1])

        # create snake segments
        self.head = Segment(self.head_image, head_start_pos)
        self.first_body_segment = Segment(self.body_image, body_position)
        self.tail = Segment(self.tail_image, tail_position)
        # create snake body
        self.body = [self.head, self.first_body_segment, self.tail]

        # add snake segments to group
        # TODO check if necessary
        self.add(self.head)
        self.add(self.first_body_segment)
        self.add(self.tail)

    def handle_event(self, event_key):
        """
        TODO update to velocity based on scale perhaps? and velocity by clock tick
        limit to 1 increment per clock tick NO DIAGONALS
        """
        if event_key == pygame.K_LEFT and self.direction != "RIGHT":
            self.vx = -INCREMENT
            self.vy = 0
            self.direction = "LEFT"

        elif event_key == pygame.K_RIGHT and self.direction != "LEFT":
            self.vx = INCREMENT
            self.vy = 0
            self.direction = "RIGHT"

        elif event_key == pygame.K_UP and self.direction != "DOWN":
            self.vx = 0
            self.vy = -INCREMENT
            self.direction = "UP"

        elif event_key == pygame.K_DOWN and self.direction != "UP":
            self.vx = 0
            self.vy = INCREMENT
            self.direction = "DOWN"

        else:
            # continue same direction
            pass

    def grow(self):
        # Create a new body segment and add it to self.body
        new_segment = Segment(self.body_image, self.body[-1].rect.center)
        self.body[-1] = new_segment
        self.add(new_segment)
        self.body.append(self.tail)

        self._size += 1

    def update(self) -> bool:
        """Store the old positions of the head and body segments
        returns True if no collision, False if collision"""
        old_positions = [segment.rect.center for segment in self.body]

        # Move the head
        self.head.rect.centerx += self.vx
        self.head.rect.centery += self.vy

        # Move each body segment to the old position of the segment in front of it
        for i, segment in enumerate(self.body[1:]):
            segment.rect.center = old_positions[i]

        self._track_direction()

        if self._check_self_collision():
            logging.info("self collision detected")
            return False
        else:
            return True

    def _track_direction(self):
        # for head and tail rotations
        self.direction_list.append(self.direction)
        if len(self.direction_list) > self._size + 1:
            self.direction_list.pop(0)

    def _check_self_collision(self):
        # get the coords out of the segments
        coords = [segment.rect.center for segment in self.body]
        # if any of the coordinates are the same (erased by set), there is a collision
        if len(coords) != len(set(coords)):
            return True
        else:
            return False

    def draw(self, surface: pygame.Surface):
        for i, segment in enumerate(self.body):
            if i == 0:
                if self.direction_list[-1] == "RIGHT":
                    self.head_image = pygame.transform.rotate(load_image("head"), 270)
                elif self.direction_list[-1] == "LEFT":
                    self.head_image = pygame.transform.rotate(load_image("head"), 90)
                elif self.direction_list[-1] == "DOWN":
                    self.head_image = pygame.transform.rotate(load_image("head"), 180)
                elif self.direction_list[-1] == "UP":
                    self.head_image = pygame.transform.rotate(load_image("head"), 0)
                segment.image = self.head_image
            elif i == len(self.body) - 1:
                if self.direction_list[0] == "RIGHT":
                    self.tail_image = pygame.transform.rotate(load_image("tail"), 270)
                elif self.direction_list[0] == "LEFT":
                    self.tail_image = pygame.transform.rotate(load_image("tail"), 90)
                elif self.direction_list[0] == "DOWN":
                    self.tail_image = pygame.transform.rotate(load_image("tail"), 180)
                elif self.direction_list[0] == "UP":
                    self.tail_image = pygame.transform.rotate(load_image("tail"), 0)
                segment.image = self.tail_image
            else:
                segment.image = self.body_image
            segment.draw(surface)

    def get_score(self):
        return self._size
