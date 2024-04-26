from load_image import ft_load
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tester.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    print(ft_load(image_path))
