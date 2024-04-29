import numpy as np


def give_bmi(height, weight) -> list[int | float]:
    """
    Calculate BMI values from height and weight lists.

    Args:
    height (list[int | float]): List of heights.
    weight (list[int | float]): List of weights.

    Returns:
    list[int | float]: List of BMI values.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")

    # chech if the lists are empty
    if not height or not weight:
        raise ValueError("Height and weight lists must not be empty.")

    # check if the lists contain only numbers
    try:
        height = [float(h) for h in height]
        weight = [float(w) for w in weight]
    except ValueError:
        raise ValueError("Height and weight lists must contain only numbers.")

    height_arr = np.array(height)
    weight_arr = np.array(weight)

    bmi = weight_arr / (height_arr ** 2)

    return bmi.tolist()


def apply_limit(bmi, limit) -> list[bool]:
    """
    Check if BMI values are above a given limit.

    Args:
    bmi (list[int | float]): List of BMI values.
    limit (int): BMI limit.

    Returns:
    list[bool]: List of boolean values indicating whether
    each BMI is above the limit.
    """

    if not bmi:
        raise ValueError("BMI list is empty.")

    if not isinstance(limit, (int, float)) or limit <= 0:
        raise ValueError("Limit must be a positive integer or float.")

    above_limit = [value > limit for value in bmi]

    return above_limit
