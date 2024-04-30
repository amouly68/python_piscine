class calculator:
    """A class to perform basic arithmetic operations on a vector."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Return the dot product of two vectors."""
        result = sum([i * j for i, j in zip(V1, V2)])
        print(f"Dot product is : {result}")
        return result

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors."""
        result = [float(i + j) for i, j in zip(V1, V2)]
        print(f"Add vector is : {result}")
        return result

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors."""
        result = [float(i - j) for i, j in zip(V1, V2)]
        print(f"Subtract vector is : {result}")
        return result
