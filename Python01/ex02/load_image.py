from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """This function loads an image from the specified file path,
    prints its format and shape,
        and prints the content of its pixels in RGB format."""
    try:
        image = Image.open(path)
        if image.format not in ['JPEG', 'JPG']:
            raise ValueError("The image format should be JPG or JPEG")
        print("The format of the image is:", image.format)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image_array = np.array(image)
        print("The shape of the image is:", image_array.shape)
        print(image_array)
        return image_array
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    image_path = "landscape.jpg"
    ft_load(image_path)
