import numpy as np


def slice_me(family, start, end):
    """
    Prints the shape of the 2D array and returns a truncated
    version of the array based on the provided start and end indices.

    Args:
    family (list): 2D array.
    start (int): Start index for slicing.
    end (int): End index for slicing.

    Returns:
    list: Truncated version of the array.
    """
    if not isinstance(family, list):
        raise TypeError("Input must be a list.")

    if not all(isinstance(row, list) for row in family):
        raise ValueError("Input must be a 2D array.")

    if start < 0:
        start += len(family)
    if end < 0:
        end += len(family)

    lim = len(family)
    if (start < 0 or end < 0 or start >= lim or end >= lim or start > end):
        raise ValueError("Start and end indices not ok.")

    family_array = np.array(family)

    # Print the shape of the array
    print("My shape is :", family_array.shape)

    # Perform slicing
    sliced_array = family_array[start:end]

    # Print the shape of the sliced array
    print("My new shape is :", sliced_array.shape)

    # Convert the sliced NumPy array back to a list of lists
    sliced_family = sliced_array.tolist()

    return sliced_family
