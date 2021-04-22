import timeit

py = timeit.timeit('greyscale_filter("../../rain.jpg")', setup='import instapy.greyscale_filter', number=1)

print(py)

