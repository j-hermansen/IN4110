from assignment3.array import Array


def test_if_print_returns_string():
    arr1 = Array((5,), 1, 2, 3, 4, 5)

    assert str(arr1) == "1 2 3 4 5"


def test_append_single_element():
    arr1 = Array((3,), 1, 2, 3)
    new_array = arr1 + (4,)

    assert new_array == (1, 2, 3, 4)


def test_append_array():
    arr1 = Array((3,), 1, 2, 3)
    arr2 = (4, 5, 6)
    new_array = arr1 + arr2

    assert new_array == (1, 2, 3, 4, 5, 6)


def test_substract_single_element():
    arr = Array((3,), 1, 3, 9)
    nr = 3
    new_array = arr - nr

    assert new_array == (1, 9)


def test_substract_array():
    arr = Array((5,), 1, 3, 9, 5, 2)
    arr2 = (3, 5, 2)

    new_array = arr - arr2

    assert new_array == (1, 9)


def test_multiply_array_with_integer():
    arr = Array((5,), 1, 3, 9, 5, 2)
    num = 2

    new_array = arr * num

    assert new_array == (2, 6, 18, 10, 4)


def test_comparing_arrays():
    arr = Array((5,), 1, 3, 9, 5, 2)
    arr2 = Array((5,), 1, 3, 9, 5, 2)

    assert arr == arr2


def test_comparing_arrays():
    arr = [4, 1, 9, 11, 43]
    arr2 = [4, 2, 9, 11, 43]

    isNotTheSame = array.__eq__(arr, arr2)

    assert isNotTheSame == "false"


def test_comparing_arrays_element_wise():
    arr = [1, 0, 3, 4]
    arr2 = [1, 0, 3, 4]

    isTrue = array.is_equal(arr, arr2)

    assert isTrue == ['true', 'true', 'true', 'true']


def test_comparing_arrays_element_wise2():
    arr = [11, 2, 3]
    arr2 = [11, 2, 3]

    isTrue = array.is_equal(arr, arr2)

    assert isTrue == ['true', 'true', 'true']


def test_mean_of_array():
    arr = [9, 2, 3, 2]

    meanValue = array.mean(arr)

    assert meanValue == 4


def test_mean_of_array2():
    arr = [3, 3, 3, 3]

    meanValue = array.mean(arr)

    assert meanValue == 3


def test_variance_of_array():
    arr = [3, 3, 3, 3]

    varValue = array.variance(arr)

    varArr = []
    for x in arr:
        varArr.append((x - array.mean(arr)) ** 2)
    correctVar = array.mean(varArr)

    assert varValue == correctVar


def test_variance_of_array2():
    arr = [13, 43, 1, 10]

    varValue = array.variance(arr)

    varArr = []
    for x in arr:
        varArr.append((x - array.mean(arr)) ** 2)
    correctVar = array.mean(varArr)

    assert varValue == correctVar


def test_smallest_array_element():
    arr = [13, 43, 1, 10]

    minValue = array.min_element(arr)

    assert minValue == 1


def test_smallest_array_element2():
    arr = [13, 43, 101, 10]

    minValue = array.min_element(arr)

    assert minValue == 13
