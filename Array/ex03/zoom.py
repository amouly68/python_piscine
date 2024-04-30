from load_image import ft_load
from PIL import Image, ImageDraw, ImageFont
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


def main():
    """
    Zoom in the image by cropping the image to the center 400x400 pixels.
    """
    try:
        # Load the image
        img = ft_load("animal.jpeg")
        if img is None:
            return None
        print(img)

        # PIL = Image.fromarray(img).crop((450, 100, 850, 500)).convert("L")
        # PIL.show()
        # array_PIL = np.array(PIL)
        # print(f"New shape after slicing: {array_PIL.shape}")
        # print(array_PIL)

        Zoom_numpy = img[100:500, 450:850, :1]
        img2 = Image.fromarray(Zoom_numpy.squeeze())
        print(f"New shape after slicing: {Zoom_numpy.shape} or {img2.size}")
        img2 = add_pixel_scale(img2)

        img2.save("zoomed_image.jpeg")
        os.system("xdg-open zoomed_image.jpeg")
        print(Zoom_numpy)

    except Exception as e:
        print(f"Error zooming image: {e}")
        return None


if __name__ == "__main__":
    main()
