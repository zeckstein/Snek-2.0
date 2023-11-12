from enum import Enum


class Color(Enum):
    """use these colors to create buttons and text # TODO check in on this statement"""

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    SILVER = (192, 192, 192)
    GRAY = (128, 128, 128)
    MAROON = (128, 0, 0)
    OLIVE = (128, 128, 0)
    LIME = (0, 128, 0)
    TEAL = (0, 128, 128)
    NAVY = (0, 0, 128)
    DARK_RED = (139, 0, 0)
    LIGHT_GRAY = (211, 211, 211)


# CONSTANTS
MINIMUM_WIDTH = 600
MINIMUM_HEIGHT = 600
INCREMENT = 40

FPS = 5
