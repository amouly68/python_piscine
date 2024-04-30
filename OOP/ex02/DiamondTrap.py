from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King of the Seven Kingdoms."""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, color):
        self._eyes = color

    @property
    def hairs(self):
        return self._hairs

    @hairs.setter
    def hairs(self, color):
        if color == 'blond':
            self._hairs = 'light'
        else:
            self._hairs = color

    def set_eyes(self, color):
        """Set the eye color of the King."""
        self.eyes = color

    def get_eyes(self):
        """Get the eye color of the King."""
        return self.eyes

    def set_hairs(self, color):
        """Set the hair color of the King."""
        self.hairs = color

    def get_hairs(self):
        """Get the hair color of the King."""
        return self.hairs
