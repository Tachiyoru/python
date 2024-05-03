import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(image, scale=2):
    """
    Takes a PIL Image and returns a new image that is a
        cropped "zoomed-in" version of the original.
    Parameters:
    - image: a PIL Image object
    - scale: the scale factor to zoom. Higher values result
      in higher zoom levels. Default is 2.

    Returns: a new PIL Image that is a zoomed-in version of the original image
    The left and top define the upper left corner of the box,
    while right and bottom define the lower right corner.
    """
    width, height = image.size
    new_width = width // scale
    new_height = height // scale

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    image = image.crop((left, top, right, bottom))
    return image


def main():
    image_path = "animal.jpeg"
    img = ft_load(image_path)

    if img is None:
        return

    print(f"The shape of image is: {np.array(img).shape}")

    print(np.array(img))

    img_zoomed = zoom_image(img)
    print(f"New shape after slicing: {np.array(img_zoomed).shape}")
    print(np.array(img_zoomed))

    plt.imshow(img_zoomed, cmap='gray')
    plt.xticks(np.arange(0, img_zoomed.size[0], step=50))
    plt.yticks(np.arange(0, img_zoomed.size[1], step=50))
    plt.show()


if __name__ == "__main__":
    main()
