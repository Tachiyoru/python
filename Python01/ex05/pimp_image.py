import numpy as np


def ft_invert(array: np.array) -> np.array:
    """Inverts the color of the image received."""
    res = np.full(array.shape, 255, dtype=np.uint8)
    res -= array
    return res


def ft_red(array: np.array) -> np.array:
    """applies red filter"""
    res = np.full(array.shape, (1, 0, 0), dtype=np.uint8)
    res *= array
    return res


def ft_green(array: np.array) -> np.array:
    """applies green filter"""
    res = np.copy(array)
    res[:, :, 0] -= array[:, :, 0]
    res[:, :, 2] -= array[:, :, 2]
    return res


def ft_blue(array: np.array) -> np.array:
    """applies blue filter"""
    res = np.zeros_like(array, dtype=np.uint8)
    res[:, :, 2] = array[:, :, 2]
    return res


def ft_grey(array: np.array) -> np.array:
    """applies grayscale filter"""
    g_ch = array[:, :, 1]
    res = np.stack([g_ch, g_ch, g_ch], axis=2)
    return res.astype(np.uint8)
