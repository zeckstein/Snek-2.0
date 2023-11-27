import logging
from config import FPS


class Options:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.speed = FPS
            # update what we store for grid size
            cls._instance.grid_size = 15  # TODO implement grid size feature
        return cls._instance

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def grid_size(self):
        return self._grid_size

    @grid_size.setter
    def grid_size(self, value):
        self._grid_size = value

    def update_speed(self, new_speed):
        self.speed = new_speed
        logging.debug(f"Speed updated to {self.speed}")

    def update_grid_size(self, new_grid_size):
        self.grid_size = new_grid_size
        logging.debug(f"Grid size updated to {self.grid_size}")
