import random

import cv2
import numpy as np

import instapy

# from cython_color2gray import greyscale_image_cython

def test_grayscale_filter():

    # create random 3d array
    python_image_array = np.random.randint(0, 256, size=(20, 30, 3))

    # write image with created 3d array
    cv2.imwrite("test.jpg", python_image_array)

    # read created image
    image = cv2.imread("test.jpg")

    # convert from bgr to rgb
    imageAsRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # make the greyscale converting for the first pixel
    sum = (imageAsRGB[0, 0, 0] * .29 + imageAsRGB[0, 0, 1] * .72 + imageAsRGB[0, 0, 2] * 0.07)
    imageAsRGB[0, 0, 0] = sum
    imageAsRGB[0, 0, 1] = sum
    imageAsRGB[0, 0, 2] = sum

    # pass image to greyscale function
    python_image_greyscale_array = instapy.greyscale_image("test.jpg")
    # python_image_greyscale_array_numpy = instapy.greyscale_image_numpy("test.jpg")
    # python_image_greyscale_array_numba = instapy.greyscale_image_numba("test.jpg")
    # python_image_greyscale_array_cython = greyscale_image_cython("test.jpg")

    # check if pixel are changed correctly
    assert imageAsRGB[0, 0, 0] == python_image_greyscale_array[0, 0, 0]
    # assert imageAsRGB[0, 0, 0] == python_image_greyscale_array_numpy[0, 0, 0]
    # assert imageAsRGB[0, 0, 0] == python_image_greyscale_array_numba[0, 0, 0]
    # assert imageAsRGB[0, 0, 0] == python_image_greyscale_array_cython[0, 0, 0]


def test_sepia_filter():
    # create random 3d array
    python_image_array = np.random.randint(0, 256, size=(20, 30, 3))
    sepiamatrix = [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]

    # write image with created 3d array
    cv2.imwrite("test.jpg", python_image_array)

    # read created image
    image = cv2.imread("test.jpg")

    # make the greyscale converting for the first pixel
    (b, g, r) = cv2.split(image)

    r_new = r * sepiamatrix[0][0] + g * sepiamatrix[0][1] + b * sepiamatrix[0][2]
    g_new = r * sepiamatrix[1][0] + g * sepiamatrix[1][1] + b * sepiamatrix[1][2]
    b_new = r * sepiamatrix[2][0] + g * sepiamatrix[2][1] + b * sepiamatrix[2][2]

    img_new = cv2.merge((b_new, g_new, r_new))

    # pass image to sepia function
    python_image_sepia_array = instapy.sepia_image("test.jpg")

    print(python_image_sepia_array[0, 0, 0])
    print(img_new[0, 0, 0])

    # check if pixel are changed correctly
    # assert img_new[0, 0, 0] == python_image_sepia_array[0, 0, 0]
    # assert imageAsRGB[0, 0, 0] == python_image_greyscale_array_numpy[0, 0, 0]
    # assert imageAsRGB[0, 0, 0] == python_image_greyscale_array_numba[0, 0, 0]
    # assert imageAsRGB[0, 0, 0] == python_image_greyscale_array_cython[0, 0, 0]
