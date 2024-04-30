from PIL import Image
import numpy as np


def ft_load(path):
    """
    Load an image and print its format and pixel content in RGB format.

    Args:
    path (str): Path to the image file.

    Returns:
    numpy.ndarray: Array representing the pixel content of the image.

    """
    try:
        img = Image.open(path)
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        return img_array

    except Exception as e:
        print(f"Error loading image: {e}")
        return None
