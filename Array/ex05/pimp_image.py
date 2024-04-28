from load_image import ft_load
from PIL import Image
import numpy as np
import sys


def ft_invert(array) :
    """
    Invert the colors of the image.

    Args:
    array (numpy.ndarray): Array representing the pixel content of the image.

    Returns:
    numpy.ndarray: Array representing the pixel content of the image with inverted colors.
    """
    try:
        # Invert the colors of the image
        return 255 - array
    except Exception as e:
        print(f"Error inverting image: {e}")
        return None


def ft_red(array):
    """
    only red channel of the image.
    """
    try:
        # Set the red channel of the image to 0
        array_red = array.copy()
        array_red[:, :, 1] = 0
        array_red[:, :, 2] = 0
        return array_red
    except Exception as e:
        print(f"Error setting red channel to 0: {e}")
        return None

# #your code here
def ft_green(array) :
    """
    only green channel of the image.
    """
    try:
        # Set the green channel of the image to 0
        array_green = array.copy()
        array_green[:, :, 0] = 0
        array_green[:, :, 2] = 0
        return array_green
    except Exception as e:
        print(f"Error setting green channel to 0: {e}")
        return None

def ft_blue(array) :
    """
    only blue channel of the image.
    """
    try:
        # Set the blue channel of the image to 0
        array_blue = array.copy()
        array_blue[:, :, 0] = 0
        array_blue[:, :, 1] = 0
        return array_blue
    except Exception as e:
        print(f"Error setting blue channel to 0: {e}")
        return None

def ft_grey(array) :
    """
    convert the image to greyscale.
    """
    try:
        array_grey = array.copy()
        arr = array_grey.squeeze()
        return arr.mean(axis=2).astype(np.uint8)
    except Exception as e:
        print(f"Error converting image to greyscale: {e}")
        return None




def main(image_path):
    """
    do the pimping of the image
    """
    try:
        # Load the image
        img = ft_load(image_path)
        if img is None:
            return None
        print(img)


        # Invert the colors of the image
        # inverted_img = ft_invert(img)
        # img2 = Image.fromarray(inverted_img)
        # # img2.save("inverted_image.jpeg")
        # img2.show()

        # # filter red
        # red_img = ft_green(img)
        # img3 = Image.fromarray(red_img)
        # # img3.save("red_image.jpeg")
        # img3.show()

        # # filter green
        # green_img = ft_red(img)
        # img4 = Image.fromarray(green_img)
        # # img4.save("green_image.jpeg")
        # img4.show()

        # # filter blue
        # blue_img = ft_blue(img)
        # img5 = Image.fromarray(blue_img)
        # # img5.save("blue_image.jpeg")
        # img5.show()

        # # filter grey
        grey_img = ft_grey(img)
        img6 = Image.fromarray(grey_img)
        # img6.save("grey_image.jpeg")
        img6.show()

    except Exception as e:
        print(f"Error zooming image: {e}")
        return None
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tester.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    main(image_path)