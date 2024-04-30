
class calculator:
    """A class to perform basic arithmetic operations on a vector."""

    def __init__(self, vector) -> None:
        """ Initializes the vector attribute."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add the object to all elem of vector"""
        self.vector = [i + object for i in self.vector]
        print(self.vector)
        return self.vector

    def __mul__(self, object) -> None:
        """Multiply the object to all elem of vector"""
        self.vector = [i * object for i in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, object) -> None:
        """Subtract the object to all elem of vector"""
        self.vector = [i - object for i in self.vector]
        print(self.vector)
        return self.vector

    def __truediv__(self, object) -> None:
        """Divide the object to all elem of vector"""
        if object == 0:
            raise ValueError("Cannot divide by zero!")
        self.vector = [i / object for i in self.vector]
        print(self.vector)
        return self.vector
