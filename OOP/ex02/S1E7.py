from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        super().die()

    def __repr__(self):
        vector = (self.family_name,
                  self.eyes,
                  self.hairs)
        return f"Vector: {vector}"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        super().die()

    def __repr__(self):
        vector = (self.family_name,
                  self.eyes,
                  self.hairs)
        return f"Vector: {vector}"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)


class Knight(Lannister):
    """Knight of the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.title = 'Ser'


class Lord(Lannister):
    """Lord of the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.title = 'Lord'
