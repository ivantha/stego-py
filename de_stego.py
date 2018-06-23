import cv2
import numpy as np
import common


def show(en_image_path):
    """
    Split an encrypted image
    :param en_image:
    """

    en_image = cv2.imread(en_image_path)
    de_image = en_image.copy()

    for i in range(de_image.shape[0]):
        for j in range(de_image.shape[1]):
            # Get the RGB (as a string tuple) from the current pixel
            r, g, b = common.__int_to_bin(en_image[i, j])

            # Extract the last 4 bits (corresponding to the hidden image)
            # Concatenate 4 zero bits because we are working with 8 bit values
            rgb = (r[4:] + "0000", g[4:] + "0000", b[4:] + "0000")

            # Convert it to an integer tuple
            de_image[i, j] = common.__bin_to_int(rgb)

    return de_image