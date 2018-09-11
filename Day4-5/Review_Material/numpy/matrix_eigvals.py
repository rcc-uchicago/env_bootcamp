#!/usr/bin/env python3

import numpy as np

arr2d = np.loadtxt("test_matrix.dat")
eigvals = np.linalg.eigvals(arr2d)
for ii, eigval in enumerate(eigvals):
    print(ii, eigval)
