import cv2
import numpy as np


def __is_large(img1_path, img2_path):
    """
    Compare the size of two images.
    Returns true if img1 is larger than img2
    :param img1_path:
    :param img2_path:
    :return: boolean
    """

    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    height1, width1, channels1 = img1.shape
    height2, width2, channels2 = img2.shape

    return (height1 > height2) and (width1 > width2)


def __int_to_bin(rgb):
    """
    Convert an integer tuple to a binary (string) tuple.
    :param rgb: An integer tuple (e.g. (220, 110, 96))
    :return: A string tuple (e.g. ("00101010", "11101011", "00010110"))
    """

    r, g, b = rgb
    return '{0:08b}'.format(r), '{0:08b}'.format(g), '{0:08b}'.format(b)


def __bin_to_int(rgb):
    """
    Convert a binary (string) tuple to an integer tuple.
    :param rgb: A string tuple (e.g. ("00101010", "11101011", "00010110"))
    :return: Return an int tuple (e.g. (220, 110, 96))
    """

    r, g, b = rgb
    return int(r, 2), int(g, 2), int(b, 2)


def __merge_rgb(rgb1, rgb2):
    """
    Merge two RGB tuples.
    :param rgb1: A string tuple (e.g. ("00101010", "11101011", "00010110"))
    :param rgb2: Another string tuple (e.g. ("00101010", "11101011", "00010110"))
    :return: An integer tuple with the two RGB values merged.
    """

    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    rgb = (r1[:4] + r2[:4], g1[:4] + g2[:4], b1[:4] + b2[:4])
    return rgb