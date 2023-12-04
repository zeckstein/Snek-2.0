import logging


class Options:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            
            cls._instance._screen_width = 600
            cls._instance._screen_height = 600
            cls._instance._speed = 5
            cls._instance._grid_size = 15
            cls._instance._scale = 40
        return cls._instance

    @property
    def screen_width(self):
        return self._screen_width

    @screen_width.setter
    def screen_width(self, value):
        self._screen_width = value

    @property
    def screen_height(self):
        return self._screen_height

    @screen_height.setter
    def screen_height(self, value):
        self._screen_height = value

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
        
    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = value

    def update_speed(self, new_speed):
        self.speed = new_speed
        logging.debug(f"Speed updated to {self.speed}")

    def update_grid_size(self, new_grid_size):
        self.grid_size = new_grid_size
        self._update_scale()
        logging.debug(f"Grid size updated to {self.grid_size}")
        
    def _update_scale(self):
        # assuming a square field atm
        self.scale = self.screen_width // self.grid_size
        logging.debug(f"Scale updated to {self.scale}")


