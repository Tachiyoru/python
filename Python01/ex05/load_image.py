from PIL import Image
import numpy as np


def ft_load(path: str):
    """
    Load an image, print its format,
        and its pixels content in RGB format.

    This function loads an image from the specified file path,
        prints its format and shape,
            and prints the content of its pixels in RGB format.

    Needs:
    - pip install Pillow
    - pip install numpy

    Parameters:
    - path (str): The path to the image file to load.

    Returns:
    - numpy.ndarray: A NumPy array representing
        the pixels content of the loaded image.

    Raises:
    - FileNotFoundError: If the specified image file is not found.
    - Exception: If any other error occurs during the loading process.

    Example:
        image_array = ft_load("landscape.jpg")
        print(image_array)
    """
    try:
        image = Image.open(path)
        if image.format not in ['JPEG', 'JPG']:
            raise ValueError("The image format should be JPG or JPEG")
        print("The format of the image is:", image.format)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image_array = np.array(image)
        print("The shape of the image is:", image_array.shape)
        return image_array

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)
