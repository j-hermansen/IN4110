import timeit

cy = timeit.timeit('cython_color2gray.cython_color2gray("rain.jpg")', setup='import cython_color2gray', number=1)
np = timeit.timeit('numpy_color2gray.greyscale_filter_np("rain.jpg")', setup='import numpy_color2gray', number=1)
nm = timeit.timeit('numba_color2gray.greyscale_filter_numba("rain.jpg")', setup='import numba_color2gray', number=1)
py = timeit.timeit('python_color2gray.greyscale_filter("rain.jpg")', setup='import python_color2gray', number=1)

print(cy, np, nm, py)

print('Numpy is {}x faster than python'.format(py/np))
print('Numba is {}x faster than numpy'.format(np/nm))
print('Cython is {}x faster than numba'.format(nm/cy))

print("\nSepia filter\n")

py = timeit.timeit('python_color2sepia.sepia_filter("assignment4/rain.jpg")', setup='import python_color2sepia', number=1)

