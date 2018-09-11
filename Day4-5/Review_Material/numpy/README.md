Introduction to NumPy
======================

[Full topic list](../README.md)

[NumPy](http://www.numpy.org/) is a python package that offers support for
calculations involving large multi-dimensional arrays and matrices. Use of
this package will allow you to do these kinds of calculations significantly
faster than a native python implementation. There is a [NumPy
tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html) online at
the project website.

Installation
------------

If you're using the virtual machine provided as part of the TSM CDT this
  will already have been installed for you. Otherwise there are several
  different ways to do this. The easiest would be one of the following:

- numpy will be available through the package manager on the vast majority of
  Linux installations. E.g. on Ubuntu you could do `sudo apt install
  python3-numpy`.
- You can install it using the python package manager `pip`. E.g. to install
  the version for python3 system wide where you have sudo privileges you could
  do `sudo pip3 install numpy`.
- If you're using a
  [virtual environment](../python2/README.md#virtual-environments), and have
  it activated, you can install it with simply `pip install numpy`.

Basic Usage
-----------

The core element of Numpy is the N-dimensional array, which is referred to as
the `ndarray` container within numpy. In contrast to python lists, the objects
stored within an ndarray should all be of the same type.

An example showing how a numpy array can be initialized and used is given in
`array_init.py`:

```python
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
```
We can see that matrix multiplication and even matrix inversion can be
performed simply by calling numpy functions. We'll cover more numpy functions
later in this section.

A Simple Example
----------------

An example where a 2D matrix is read from a file and its eigenvalues
calculated and output is given in `matrix_eigvals.py`:

```python
#!/usr/bin/env python3

import numpy as np

arr2d = np.loadtxt("test_matrix.dat")
eigvals = np.linalg.eigvals(arr2d)
for ii, eigval in enumerate(eigvals):
    print(ii, eigval)
```

This really shows how simple numpy can make operations which could have been
quite complex. Here we have used two numpy functions to do all of our work:
[`loadtext`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html)
which reads a file and returns the data as a numpy array of appropriate
dimension, and
[`linalg.eigvals`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eigvals.html)
which returns the eigenvalues of a general matrix. `loadtext` offers many
useful options to customize how the data is read in.

Comparison with Built-In Python
-------------------------------

As well as the simplicity it offers through its commands, the other reason to
use numpy is speed. Using numpy can be significantly faster than using the
built-in python operations on a list. This can be seen in the
`timed_array_ops.py` code:

```python
#!/usr/bin/env python3

import numpy as np
from timeit import default_timer as timer
import random

size = 10000000

print("Built-in python:")
start = timer()
a = [random.random() for i in range(size)]
print("  Initializing array with", size, "random elements takes",
    timer() - start, "s.")
start = timer()
a_sum = sum(a)
print("  Sum of elements =", a_sum, "calculated in", timer() - start, "s.")
start = timer()
norm_a = sum([i**2 for i in a]) ** 0.5
print("  Norm of vector =", norm_a, "calculated in", timer() - start, "s.")

print("\nNumpy:")
start = timer()
np_a = np.random.random(size)
print("  Initializing array with", size, "random elements takes",
        timer() - start, "s.")
start = timer()
print("  Sum of elements =", np.sum(np_a), "calculated in", timer() - start,
        "s.")
print("  Using np.dot()")
start = timer()
np_norm = np.dot(np_a, np_a) ** 0.5
print("  Norm of vector =", np_norm, "calculated in", timer() - start, "s.")
# We could also have calculated the norm as np_norm = np.linalg.norm(np_a)
```
Here we've also used the `timeit` module from the standard library to get an
easy way to find how long sections of code take. In this example we generate a
vector with many random elements, find the sum of the elements and find the
norm of the vector. This is done using both standard python and numpy, with
the time for each step output. When you run this code you'll see that the
numpy operations are much faster.

Useful Numpy Operations
-----------------------

Numpy offers very many useful routines depending on what kind of data you're
working with and what you want to do. A categorized listing is available in
the [online documentation](https://docs.scipy.org/doc/numpy/reference/routines.html).
Here are a few you might find useful to begin with:

- Initialization - see [here](https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html) for a detailed listing.
    - [`array()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html)
      initializes an array from an existing sequence.
    - [`zeros()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html)
      intializes an array to zero.
    - [`arange()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html)
      gives an array of evenly spaced values within an interval for a given
      step size.
    - [`linspace()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html)
      like `arange()` but takes the number of points to produce in the interval
      rather than the step size, allowing better handling of endpoints of the range.
- Reading and writing data files - see [here](https://docs.scipy.org/doc/numpy/reference/routines.io.html) for a detailed listing.
    - [`loadtxt()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html) - as used in the example above, this will read a file to
      a numpy array. Many options are available, and it will even
      transparently decompress `.gz` or `.bz2` files.
    - [`genfromtxt()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html)
      this works very similarly to `loadtxt` but can be told what do when data
      is missing. The numpy website outlines some [basic
      usage](https://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html)
    - [`savetxt()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html) - this can be used to save an array to a text file.
- Mathematical functions - these are typically use to perform some operation element-wise on a numpy array.
    - [`sin()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html) - trigomentric sin.
    There are similar functions for the other trigonometric, inverse, and hyperbolic functions.
- Linear Algebra (all the following are in `np.linalg`)
    - [`det()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.det.html) - compute the determinant of an array.
    - [`eig()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html) - find the eigenvalues and eigenvectors of a square array.
    - [`eigvals()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eigvals.html) - find the eigenvalues of a general matrix.
    - [`inv()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.inv.html) - compute the inverse of a matrix.
    - [`solve()`](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve) - solve a linear matrix equation.
