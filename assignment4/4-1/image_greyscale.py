import cv2
import numpy as np
from numba import jit


# def greyscale_filter(filename):
#     """Function to read image and make it greyscale.
#
#     :param filename: image name in filepath
#     :return: new greyscaled 3d array that represents image
#     """
#     image = cv2.imread(filename)
#     imageAsRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     for i in range(len(imageAsRGB)):
#         for j in range(len(imageAsRGB[i])):
#             sum = (imageAsRGB[i, j, 0] * .29 + imageAsRGB[i, j, 1] * .72 + imageAsRGB[i, j, 2] * 0.07)
#             imageAsRGB[i, j, 0] = sum
#             imageAsRGB[i, j, 1] = sum
#             imageAsRGB[i, j, 2] = sum
#     cv2.imwrite("rain_grayscale.jpeg", imageAsRGB)
#     return imageAsRGB


# def greyscale_filter_np(filename):
#     """Function to read image and make it greyscale using numpy.
#
#     :param filename: image name in filepath
#     :return: new greyscaled 3d array that represents image
#     """
#     image = cv2.imread(filename)
#     imageAsRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
#     # imageAsRGB[:, :, 0] = (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07)
#     # imageAsRGB[:, :, 1] = (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07)
#     # imageAsRGB[:, :, 2] = (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07)
#
#     np.add(imageAsRGB[:, :, 0], (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07))
#     np.add(imageAsRGB[:, :, 1], (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07))
#     np.add(imageAsRGB[:, :, 2], (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07))
#
#     cv2.imwrite("rain_grayscale.jpeg", imageAsRGB)

# @jit
# def greyscale_filter_numba(filename):
#     """Function to read image and make it greyscale using numba.
#
#     :param filename: image name in filepath
#     :return: new greyscaled 3d array that represents image
#     """
#     image = cv2.imread(filename)
#     imageAsRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     for i in range(len(imageAsRGB)):
#         for j in range(len(imageAsRGB[i])):
#             sum = (imageAsRGB[i, j, 0] * .29 + imageAsRGB[i, j, 1] * .72 + imageAsRGB[i, j, 2] * 0.07)
#             imageAsRGB[i, j, 0] = sum
#             imageAsRGB[i, j, 1] = sum
#             imageAsRGB[i, j, 2] = sum
#     cv2.imwrite("rain_grayscale.jpeg", imageAsRGB)
#     return imageAsRGB

# def greyscale_filter_cython(filename):
#     """Function to read image and make it greyscale using cython.
#
#     :param filename: image name in filepath
#     :return: new greyscaled 3d array that represents image
#     """
#     pass

