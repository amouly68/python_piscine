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
        # Open the image
        img = Image.open(path)
        
        # Print the image format and shape
        print("The shape of image is:", img.size + (3,))

        # Convert the image to a numpy array
        img_array = np.array(img)

        return img_array
    except Exception as e:
        raise ValueError(f"Error loading image: {e}")

# Test the function
if __name__ == "__main__":
    print(ft_load("landscape.jpg"))
