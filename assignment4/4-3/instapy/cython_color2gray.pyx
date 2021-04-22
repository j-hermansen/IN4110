import os
import timeit
import cv2

cpdef greyscale_image_cython(input_filename, output_filename=None):

    image = cv2.imread(input_filename)
    imageAsRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cpdef int i
    cpdef int j
    for i in range(len(imageAsRGB)):
        for j in range(len(imageAsRGB[i])):
            sum = (imageAsRGB[i, j, 0] * .29 + imageAsRGB[i, j, 1] * .72 + imageAsRGB[i, j, 2] * 0.07)
            imageAsRGB[i, j, 0] = sum
            imageAsRGB[i, j, 1] = sum
            imageAsRGB[i, j, 2] = sum

    if not (output_filename is None):
        cv2.imwrite("{}.jpeg".format(output_filename), imageAsRGB)

    return imageAsRGB


# cy = timeit.timeit('cython_color2gray("rain.jpg")', setup='import cython_color2gray', number=1000)
# py = timeit.timeit('python_color2gray.greyscale_filter("rain.jpg")', setup='import python_color2gray', number=1000)
#
# print(cy, py)
# print('Cython is {}x faster'.format(py/cy))

# file = open("cython_report_color2gray.txt", "w")
# scriptName = os.path.basename(__file__)
#
# file.write("Average runtime running {} after 3 runs: {}\n".format(scriptName, min(runtimes)))
# file.write("Average runtime running of {} is {} times faster or slower than python_color2gray\n".format(scriptName, min(runtimes)))
# file.write("Average runtime running of {} is {} times faster or slower than numpy_color2gray\n".format(scriptName, min(runtimes)))
# file.write("Average runtime running of {} is {} times faster or slower than numba_color2gray\n".format(scriptName, min(runtimes)))
# file.write("Timing performed using: manual timing\n")
#
# file.write("Advantages/disadvantages using Numba compared to NumPy")
#
# file.close()