import cv2
import numpy as np
from numba import jit


def greyscale_image(input_filename, output_filename=None):
    """Function to read image and make it greyscale.

    :param filename: image name in filepath
    :return: new greyscaled 3d array that represents image
    """
    image = cv2.imread(input_filename)

    imageAsRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    for i in range(len(imageAsRGB)):
        for j in range(len(imageAsRGB[i])):
            sum = (imageAsRGB[i, j, 0] * .29 + imageAsRGB[i, j, 1] * .72 + imageAsRGB[i, j, 2] * 0.07)
            imageAsRGB[i, j, 0] = sum
            imageAsRGB[i, j, 1] = sum
            imageAsRGB[i, j, 2] = sum

    if not (output_filename is None):
        cv2.imwrite("{}.jpeg".format(output_filename), imageAsRGB)

    return imageAsRGB


def greyscale_image_numpy(input_filename, output_filename=None):
    """Function to read image and make it greyscale using numpy.

    :param filename: image name in filepath
    :return: new greyscaled 3d array that represents image
    """
    image = cv2.imread(input_filename)
    imageAsRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # imageAsRGB[:, :, 0] = (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07)
    # imageAsRGB[:, :, 1] = (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07)
    # imageAsRGB[:, :, 2] = (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07)

    np.add(imageAsRGB[:, :, 0], (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07))
    np.add(imageAsRGB[:, :, 1], (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07))
    np.add(imageAsRGB[:, :, 2], (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07))

    if not (output_filename is None):
        cv2.imwrite("{}.jpeg".format(output_filename), imageAsRGB)

    return imageAsRGB


# @jit
# def greyscale_image_numba(input_filename, output_filename=None):
#     """Function to read image and make it greyscale using numba.
#
#     :param filename: image name in filepath
#     :return: new greyscaled 3d array that represents image
#     """
#     image = cv2.imread(input_filename)
#     imageAsRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     for i in range(len(imageAsRGB)):
#         for j in range(len(imageAsRGB[i])):
#             sum = (imageAsRGB[i, j, 0] * .29 + imageAsRGB[i, j, 1] * .72 + imageAsRGB[i, j, 2] * 0.07)
#             imageAsRGB[i, j, 0] = sum
#             imageAsRGB[i, j, 1] = sum
#             imageAsRGB[i, j, 2] = sum
#
#     if not (output_filename is None):
#         cv2.imwrite("{}.jpeg".format(output_filename), imageAsRGB)
#
#     return imageAsRGB


# def sepia_image(input_filename, output_filename=None):
#     sepiamatrix = [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
#     image = cv2.imread(input_filename)
#     # imageAsRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
#     (b, g, r) = cv2.split(image)
#     # (r, g, b) = cv2.split(imageAsRGB)
#
#     r_new = r * sepiamatrix[0][0] + g * sepiamatrix[0][1] + b * sepiamatrix[0][2]
#     g_new = r * sepiamatrix[1][0] + g * sepiamatrix[1][1] + b * sepiamatrix[1][2]
#     b_new = r * sepiamatrix[2][0] + g * sepiamatrix[2][1] + b * sepiamatrix[2][2]
#
#     img_new = cv2.merge((b_new, g_new, r_new))
#     # img_new = cv2.merge((r_new,g_new,b_new))
#
#     if not (output_filename is None):
#         cv2.imwrite("{}.jpeg".format(output_filename), img_new)
#
#     return img_new
