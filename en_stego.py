import cv2
import numpy as np
import common


def hide(parent_image_path, child_image_path):
    """
    Hide the child image inside parent.
    :param parent_image_path:
    :param child_image_path:
    """

    # Initialize images
    parent_image = cv2.imread(parent_image_path)
    child_image = cv2.imread(child_image_path)

    en_image = parent_image.copy()

    # Check whether the parent image is larger
    if not common.__is_large(parent_image_path, child_image_path):
        raise ValueError('Parent image size is lower than the child image size')

    # Iterate all the pixels in parent image
    for i in range(parent_image.shape[0]):
        for j in range(parent_image.shape[1]):
            parent_rgb = common.__int_to_bin(parent_image[i, j])

            # Use a black pixel as default
            child_rgb = common.__int_to_bin((0, 0, 0))

            # Check if the pixel map position is valid for the second image
            if i < child_image.shape[0] and j < child_image.shape[1]:
                child_rgb = common.__int_to_bin(child_image[i, j])

            # Merge the two pixels and convert it to a integer tuple
            rgb = common.__merge_rgb(parent_rgb, child_rgb)

            en_image[i, j] = common.__bin_to_int(rgb)

    return en_image
