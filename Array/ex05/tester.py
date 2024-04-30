from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from PIL import Image
import sys
import os


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

        os.system("open " + image_path)

        # Invert the colors of the image
        inverted_img = ft_invert(img)
        img2 = Image.fromarray(inverted_img)
        img2.save("inverted_image.jpeg")
        # img2.show()

        # # filter red
        red_img = ft_green(img)
        img3 = Image.fromarray(red_img)
        img3.save("red_image.jpeg")
        # img3.show()

        # filter green
        green_img = ft_red(img)
        img4 = Image.fromarray(green_img)
        img4.save("green_image.jpeg")
        # img4.show()

        # filter blue
        blue_img = ft_blue(img)
        img5 = Image.fromarray(blue_img)
        img5.save("blue_image.jpeg")
        # img5.show()

        # filter grey
        grey_img = ft_grey(img)
        img6 = Image.fromarray(grey_img)
        img6.save("grey_image.jpeg")
        # img6.show()

        os.system("xdg-open inverted_image.jpeg")
        os.system("xdg-open red_image.jpeg")
        os.system("xdg-open green_image.jpeg")
        os.system("xdg-open blue_image.jpeg")
        os.system("xdg-open grey_image.jpeg")

    except Exception as e:
        print(f"Error zooming image: {e}")
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tester.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    main(image_path)
