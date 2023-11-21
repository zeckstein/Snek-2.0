from pathlib import Path
import pygame
from utils import load_image
from config import MINIMUM_WIDTH, MINIMUM_HEIGHT, INCREMENT

import logging

base_dir = Path(__file__).resolve().parent.parent.parent
# TODO investigate better way to global initialize and not need this in every file
pygame.mixer.init()
sfx_chomp = pygame.mixer.Sound(
    str(base_dir / "assets/sounds/sfx/chomp.mp3")
)

# TODO implement color selection?
class Segment(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center=position)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)


class Snek(pygame.sprite.Group):
    def __init__(self, screen: pygame.Surface):
        pygame.sprite.Group.__init__(self)
        # number of body segments / ALSO == score basically
        self._size = 1
        # initial direction RIGHT, velocity
        self.direction = "RIGHT"
        self.direction_list = []
        # TODO change INCREMENT to scale which should = size of head rect
        self.vx = INCREMENT
        self.vy = 0

        self.head_image = load_image('head')
        self.body_image = load_image('body')
        self.tail_image = load_image('tail')

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
        
        self.sfx_chomp = sfx_chomp

    def handle_event(self, event_key: pygame.KEYDOWN) -> None:
        # TODO update to options/settings controls once implemented
        """Handles pygame events for the Snek object.
        Args:
            event_key (pygame.KEYDOWN): a pygame.KEYDOWN event only accepts
            LEFT, RIGHT, UP, DOWN arrow keys
        """
        if event_key == pygame.K_LEFT and self.direction != "RIGHT":
            self._update_direction("LEFT")
        if event_key == pygame.K_RIGHT and self.direction != "LEFT":
            self._update_direction("RIGHT")
        if event_key == pygame.K_UP and self.direction != "DOWN":
            self._update_direction("UP")
        if event_key == pygame.K_DOWN and self.direction != "UP":
            self._update_direction("DOWN")

    
    def _update_direction(self, direction: str) -> None:
        """ensures no vertical u-turn onto self

        Args:
            direction (str): direction from input
        """
        current_x = self.head.rect.centerx
        current_y = self.head.rect.centery
        
        if direction == "RIGHT" and self.direction != "LEFT":
            head_predicted_position = (current_x + INCREMENT, current_y)
            if (head_predicted_position[0] == self.body[1].rect.centerx and 
                head_predicted_position[1] == self.body[1].rect.centery):
                pass
            else:
                self.vx = INCREMENT
                self.vy = 0
                self.direction = "RIGHT"
        if direction == "LEFT" and self.direction != "RIGHT":
            head_predicted_position = (current_x - INCREMENT, current_y)
            if (head_predicted_position[0] == self.body[1].rect.centerx and 
                head_predicted_position[1] == self.body[1].rect.centery):
                pass
            else:
                self.vx = -INCREMENT
                self.vy = 0
                self.direction = "LEFT"
        if direction == "UP" and self.direction != "DOWN":
            head_predicted_position = (current_x, current_y - INCREMENT)
            if (head_predicted_position[0] == self.body[1].rect.centerx and 
                head_predicted_position[1] == self.body[1].rect.centery):
                pass
            else:
                self.vx = 0
                self.vy = -INCREMENT
                self.direction = "UP"
        if direction == "DOWN" and self.direction != "UP":
            head_predicted_position = (current_x, current_y + INCREMENT)
            if (head_predicted_position[0] == self.body[1].rect.centerx and 
                head_predicted_position[1] == self.body[1].rect.centery):
                pass
            else:
                self.vx = 0
                self.vy = INCREMENT
                self.direction = "DOWN"
                
        
    def update(self, screen: pygame.Surface, chomp: bool) -> bool:
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

        if self._check_self_collision() or self._check_boundary_collision(screen):
            logging.info("DEAD")
            return False
        else:
            if chomp:
                self.sfx_chomp.play()
                self._grow()
            return True

    def _track_direction(self) -> None:
        # for head and tail rotations
        self.direction_list.append(self.direction)
        if len(self.direction_list) > self._size + 1:
            self.direction_list.pop(0)

    def _check_self_collision(self) -> bool:
        # get the coords out of the segments
        coords = [segment.rect.center for segment in self.body]
        # if any of the coordinates are the same (erased by set), there is a collision
        if len(coords) != len(set(coords)):
            logging.info("Snek self collision")
            return True
        else:
            return False

    def _check_boundary_collision(self, screen: pygame.Surface) -> bool:
        if (
            self.head.rect.centerx < 0
            or self.head.rect.centerx > screen.get_width()
            or self.head.rect.centery < 0
            or self.head.rect.centery > screen.get_height()
        ):
            logging.info("Snek out of bounds")
            return True
        else:
            return False
        
    def _grow(self) -> None:
        # Create a new body segment and add it to self.body
        new_segment = Segment(self.body_image, self.body[-1].rect.center)
        self.body[-1] = new_segment
        self.add(new_segment)
        self.body.append(self.tail)

        self._size += 1
        

    def draw(self, surface: pygame.Surface) -> None:
        """Draws the Snek object to the screen with correct head and tail orientation."""
        for i, segment in enumerate(self.body):
            if i == 0:
                if self.direction_list[-1] == "RIGHT":
                    head_image = pygame.transform.rotate(self.head_image, 270)
                elif self.direction_list[-1] == "LEFT":
                    head_image = pygame.transform.rotate(self.head_image, 90)
                elif self.direction_list[-1] == "DOWN":
                    head_image = pygame.transform.rotate(self.head_image, 180)
                elif self.direction_list[-1] == "UP":
                    head_image = pygame.transform.rotate(self.head_image, 0)
                segment.image = head_image
            elif i == len(self.body) - 1:
                if self.direction_list[0] == "RIGHT":
                    tail_image = pygame.transform.rotate(self.tail_image, 270)
                elif self.direction_list[0] == "LEFT":
                    tail_image = pygame.transform.rotate(self.tail_image, 90)
                elif self.direction_list[0] == "DOWN":
                    tail_image = pygame.transform.rotate(self.tail_image, 180)
                elif self.direction_list[0] == "UP":
                    tail_image = pygame.transform.rotate(self.tail_image, 0)
                segment.image = tail_image

            segment.draw(surface)


    def get_score(self) -> int:
        return self._size
