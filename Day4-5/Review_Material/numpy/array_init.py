#!/usr/bin/env python3

import numpy as np

# To create a numpy array, we use the array() function which takes a sequence
# (such as a list) or nested sequence as an argument.
a = np.array([[1.0, 2.0], [3.5, 4.1]])
print("The type of a is", type(a))

# Many properties of the array are accessible:
print("The number of dimensions of a is", a.ndim)
print("The size of each dimension of a is", a.shape)
print("The number of elements of a is", a.size)
print("The type of the elements of a is", a.dtype)

# Numpy offers functions which can carry out many useful operations on these
# arrays.
print("The result of the matrix multiplication of a with iteslf is:")
print(np.dot(a, a))
print("The inverse of a is:")
print(np.linalg.inv(a))
