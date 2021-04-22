class Array:
    # Assignment 3.3

    def __init__(self, shape, *values):
        """
        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        self.shape = shape

        tempList = []
        if(len(values) <= shape[0]):
            for i in range(len(values)):
                if i == 0:
                    itemType = type(values[i])

                if isinstance(values[i], itemType):
                    tempList.append(values[i])
                else:
                    raise Exception("Arrays must be of one data type. Your values where: {}".format(values))

        self.values = tuple(tempList)

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """

        output = ""

        for x in self.values:
            output += str(x) + " "

        return output.strip()


    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """

        newArr = self.values + other

        return newArr


    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        pass

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """

        newArr = list(self.values)

        if (isinstance(other, (int, float))):
            newArr.remove(other)
        elif (isinstance(other, tuple)):
            for i in other:
                if i in newArr:
                    newArr.remove(i)
        else:
            pass

        return tuple(newArr)

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        pass

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """

        newArr = list()

        if not isinstance(other, tuple):
            for i in range(len(self.values)):
                newArr.append(self.values[i] * other)
        else:
            for i in range(len(self.values)):
                newArr.append(self.values[i] * other[i])

        return tuple(newArr)

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        pass

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal. False otherwise.
        """
        pass

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """

        newArr = list()

        if len(self.values) != len(other):
            raise ValueError("The arrays are not equal in length.")


        for i in range(len(self.values)):
            newArr.append(self.values[i] == other[i])


        return tuple(newArr)




    def mean(self):
        """Computes the mean of the array
        Only needs to work for numeric data types.
        Returns:
            float: The mean of the array values.
        """
        pass

    def variance(self):
        """Computes the variance of the array
        Only needs to work for numeric data types.
        The variance is computed as: mean((x - x.mean())**2)
        Returns:
            float: The mean of the array values.
        """
        pass

    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for numeric data types.
        Returns:
            float: The value of the smallest element in the array.
        """
        pass
