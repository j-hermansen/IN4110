import os
import time
from numba import jit

import cv2
# from image_greyscale import greyscale_filter_numba

@jit
def greyscale_filter_numba(filename):
    """Function to read image and make it greyscale using numba.

    :param filename: image name in filepath
    :return: new greyscaled 3d array that represents image
    """
    image = cv2.imread(filename)
    imageAsRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    for i in range(len(imageAsRGB)):
        for j in range(len(imageAsRGB[i])):
            sum = (imageAsRGB[i, j, 0] * .29 + imageAsRGB[i, j, 1] * .72 + imageAsRGB[i, j, 2] * 0.07)
            imageAsRGB[i, j, 0] = sum
            imageAsRGB[i, j, 1] = sum
            imageAsRGB[i, j, 2] = sum
    cv2.imwrite("rain_grayscale.jpeg", imageAsRGB)
    return imageAsRGB

# filename = "rain.jpg"
# file = open("numba_report_color2gray.txt", "w")
# scriptName = os.path.basename(__file__)
#
# runtimes = []
#
# for i in range(3):
#     t0 = time.time()
#     greyscale_filter_numba(filename)
#     t1 = time.time()
#     runtime = t1 - t0
#     runtimes.append(runtime)
#
# file.write("Average runtime running {} after 3 runs: {}\n".format(scriptName, min(runtimes)))
# file.write("Average runtime running of {} is {} times faster or slower than python_color2gray\n".format(scriptName, min(runtimes)))
# file.write("Average runtime running of {} is {} times faster or slower than numpy_color2gray\n".format(scriptName, min(runtimes)))
# file.write("Timing performed using: manual timing\n")
#
# file.write("Advantages/disadvantages using Numba compared to NumPy")
#
# file.close()

