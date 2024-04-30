from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for a character in a story or game."""

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a new instance of a character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool): True if is alive, False otherwise.@
                            Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Set the character's alive status to False, representing their death.
        """
        self.is_alive = False


class Stark(Character):
    """Represents a member of the Stark family in a fantasy universe."""

    def die(self):
        """Kill the character by setting is_alive to False."""
        super().die()
        print(f"{self.first_name} STARK died.")
