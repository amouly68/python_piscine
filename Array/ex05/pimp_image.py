import numpy as np


def ft_invert(array) -> np.ndarray:
    """
    Invert the colors of the image.
    """
    try:
        print("Inverts the colors of the image received")
        return 255 - array
    except Exception as e:
        print(f"Error inverting image: {e}")
        return None


def ft_red(array) -> np.ndarray:
    """
    only red channel of the image.
    """
    try:
        array_red = array.copy()
        array_red[:, :, 1] = 0
        array_red[:, :, 2] = 0
        print("filter red to the image received")
        return array_red
    except Exception as e:
        print(f"Error setting red channel to 0: {e}")
        return None


def ft_green(array) -> np.ndarray:
    """
    only green channel of the image.
    """
    try:
        array_green = array.copy()
        array_green[:, :, 0] = 0
        array_green[:, :, 2] = 0
        print("filter green to the image received")
        return array_green
    except Exception as e:
        print(f"Error setting green channel to 0: {e}")
        return None


def ft_blue(array) -> np.ndarray:
    """
    only blue channel of the image.
    """
    try:
        array_blue = array.copy()
        array_blue[:, :, 0] = 0
        array_blue[:, :, 1] = 0
        print("filter blue to the image received")
        return array_blue
    except Exception as e:
        print(f"Error setting blue channel to 0: {e}")
        return None


def ft_grey(array) -> np.ndarray:
    """
    convert the image to greyscale.
    """
    try:
        array_grey = array.copy()
        arr = array_grey.squeeze()
        print("convert the image to greyscale")
        return arr.mean(axis=2).astype(np.uint8)
    except Exception as e:
        print(f"Error converting image to greyscale: {e}")
        return None
