import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
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


def rotate(image):
    """
    Rotate/transpose the input image.
    Args:
        image (PIL.Image.Image): The input image.
    Returns:
        PIL.Image.Image: The transposed image.
    """
    img_d = np.array(image)
    transposed_data = [[row[i] for row in img_d] for i in range(len(img_d[0]))]
    return Image.fromarray(np.uint8(transposed_data))


def main():
    try:
        image_path = "animal.jpeg"
        img = ft_load(image_path)

        if img is None:
            return

        img_cropped = zoom_image(img)
        print(f"The shape of image is: {np.array(img_cropped).shape}")
        print(np.array(img_cropped))

        img_transposed = rotate(img_cropped)
        print(f"New shape after Transpose: {np.array(img_transposed).shape}")
        print(np.array(img_transposed))

        img_gray = img_transposed.convert('L')
        plt.imshow(img_gray, cmap='gray')
        # plt.xticks([])
        # plt.yticks([])
        plt.show()
    except Exception as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
