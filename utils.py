from pygame.image import load
from pygame import Surface

from pathlib import Path


def load_image(name: str, with_alpha=True) -> Surface:
    """Provide name of file without extension and it will load it from assets/images folder.

    Args:
        name (str): filename without extension, PNG atm
        with_alpha (bool, optional): if has alpha parts to see. Defaults to True.

    Returns:
        Pygame Surface: image as a pygame surface
    """
    filename = Path(__file__).parent / Path(f"assets/images/{name}.png")

    loaded_image = load(filename.resolve())
    if with_alpha:
        return loaded_image.convert_alpha()
    else:
        return loaded_image.convert()
