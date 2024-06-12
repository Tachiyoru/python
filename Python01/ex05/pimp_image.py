import numpy as np


def ft_invert(array: np.array) -> np.array:
    """Inverts the color of the image received."""
    res = np.copy(array)
    res[:, :, 0] = 255 - array[:, :, 0]
    res[:, :, 1] = 255 - array[:, :, 1]
    res[:, :, 2] = 255 - array[:, :, 2]
    return res


def ft_red(array: np.array) -> np.array:
    """applies red filter"""
    res = np.copy(array)
    res[:, :, 1] = 0
    res[:, :, 2] = 0
    return res


def ft_green(array: np.array) -> np.array:
    """applies green filter"""
    res = np.copy(array)
    res[:, :, 0] -= array[:, :, 0]
    res[:, :, 2] -= array[:, :, 2]
    return res


def ft_blue(array: np.array) -> np.array:
    """applies blue filter"""
    res = np.copy(array)
    res[:, :, 1] = 0
    res[:, :, 0] = 0
    return res


def ft_grey(array: np.array) -> np.array:
    """applies grayscale filter"""
    res = (array[:, :, 0] / 3.344) + (array[:, :, 1] / 1.704)\
        + (array[:, :, 2] / 8.772)
    return res
