import os
import time

import cv2
import numpy as np


# from image_greyscale import greyscale_filter_np

def greyscale_filter_np(filename):
    """Function to read image and make it greyscale using numpy.

    :param filename: image name in filepath
    :return: new greyscaled 3d array that represents image
    """

    sepiamatrix = np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])

    image = cv2.imread(filename)
    imageAsRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # print(imageAsRGB[0, 0, 0])
    # print(imageAsRGB[:, :, 0])
    # print(imageAsRGB)

    np.multiply(imageAsRGB[:, :, 0], sepiamatrix[0, 0])
    np.multiply(imageAsRGB[:, :, 1], sepiamatrix[0, 1])
    np.multiply(imageAsRGB[:, :, 2], sepiamatrix[0, 2])

    #
    # np.multiply(imageAsRGB[:, :, 0], sepiamatrix[0])
    # np.multiply(imageAsRGB[:, :, 1], sepiamatrix[1])
    # np.multiply(imageAsRGB[:, :, 2], sepiamatrix[2])

    # imageAsRGB[:, :, 0] = (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07)
    # imageAsRGB[:, :, 1] = (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07)
    # imageAsRGB[:, :, 2] = (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07)

    # np.add(imageAsRGB[:, :, 0], (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07))
    # np.add(imageAsRGB[:, :, 1], (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07))
    # np.add(imageAsRGB[:, :, 2], (imageAsRGB[:, :, 0] * .29 + imageAsRGB[:, :, 1] * .72 + imageAsRGB[:, :, 2] * .07))
    #
    cv2.imwrite("rain_sepia.jpeg", imageAsRGB)


greyscale_filter_np("../4-3/tests/rain.jpg")

# filename = "rain.jpg"
# file = open("numpy_report_color2gray.txt", "w")
# scriptName = os.path.basename(__file__)
#
# runtimes = []
#
# for i in range(3):
#     t0 = time.time()
#     greyscale_filter_np(filename)
#     t1 = time.time()
#     runtime = t1 - t0
#     runtimes.append(runtime)
#
# file.write("Timing: {}\n".format(scriptName))
# file.write("Average runtime running {} after 3 runs: {}\n".format(scriptName, min(runtimes)))
# file.write("Average runtime running of {} is {} times faster or slower than python_color2gray\n".format(scriptName, min(runtimes)))
# file.write("Timing performed using: manual timing\n")
#
# file.close()
