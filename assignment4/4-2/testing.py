import timeit

print("\nSepia filter\n")

py = timeit.timeit('python_color2sepia.sepia_filter("../rain.jpg")', setup='import python_color2sepia', number=1)

print(py)

# print('Numpy is {}x faster than python'.format(py/np))
# print('Numba is {}x faster than numpy'.format(np/nm))
# print('Cython is {}x faster than numba'.format(nm/cy))


