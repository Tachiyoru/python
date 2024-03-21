import numpy as np

def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    return 255 - array

# def ft_red(array: np.ndarray) -> np.ndarray:
#     """
#     Enhances the red color in the image.
#     """
#     array[..., 0] *= 2  # Multiplying red channel by 2
#     return array

def ft_red(array):
    red_channel = array[:, :, 0]
    return np.stack([red_channel, np.zeros_like(red_channel), np.zeros_like(red_channel)], axis=2)


def ft_green(array):
    green_channel = array[:, :, 1]
    return np.stack([np.zeros_like(green_channel), green_channel, np.zeros_like(green_channel)], axis=2)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Set the blue color in the image to maximum.
    """
    array[..., 2] = 255  # Setting blue channel to 255
    return array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale.
    """
    return np.dot(array[...,:3], [0.2989, 0.5870, 0.1140])
