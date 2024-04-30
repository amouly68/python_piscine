from load_image import ft_load
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os


def add_pixel_scale(image, interval=50):
    """
    Add a pixel scale to the image.
    """

    offset_x = 40
    offset_y = 5
    new_w = image.width + 30
    new_h = image.height + 30
    new_img = Image.new("RGB", (new_w, new_h + 30), color="white")
    new_img.paste(image, (offset_x, offset_y))

    # Dessine l'échelle des pixels sur l'axe x
    draw = ImageDraw.Draw(new_img)
    font = ImageFont.load_default()

    for i in range(offset_x, image.width + offset_x, interval):
        draw.line([(i, image.height + offset_y),
                   (i, image.height + offset_y + 5)], fill="black", width=2)
        if i != image.width + offset_x:
            draw.text((i - 5, image.height + 10), str(i - offset_x),
                      fill="black", font=font)

    # Dessine l'échelle des pixels sur l'axe y
    for i in range(offset_y, image.height + offset_y, interval):
        draw.line([(offset_x - 5, i), (offset_x, i)], fill="black", width=2)
        if i != image.height:
            draw.text((offset_x - 25, i - 5), str(i - offset_y),
                      fill="black", font=font)

    return new_img


def rotate_image(img):
    """
    Rotate the image by 90 degrees to the left.

    Args:
    img (numpy.ndarray): Array representing the pixel content of the image.

    Returns:
    numpy.ndarray: Array representing the pixel content of the rotated image.
    """

    try:
        img_r = np.zeros((img.shape[1], img.shape[0]), dtype=np.uint8)
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                img_r[y, x] = img[x, y]
        return img_r
    except Exception as e:
        print(f"Error rotating image: {e}")
        return None


def main():
    """
    totate the image by 90 degrees to the left
    """
    try:
        # Load the image
        img = ft_load("animal.jpeg")
        if img is None:
            return None

        Zoom_numpy = img[100:500, 450:850, :1]
        img2 = Image.fromarray(Zoom_numpy.squeeze())
        print(f"The shape of the image: {Zoom_numpy.shape} or {img2.size}")
        print(img)

        rotated_img = rotate_image(Zoom_numpy.squeeze())
        img = Image.fromarray(rotated_img)
        print(f"New shape after Transpose: {img.size}")
        img = add_pixel_scale(img)

        img.save("rotated_image.jpeg")
        os.system("xdg-open rotated_image.jpeg")

        print(rotated_img)

    except Exception as e:
        print(f"Error zooming image: {e}")
        return None


if __name__ == "__main__":
    main()
