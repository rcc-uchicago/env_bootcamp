#!/usr/bin/env python

# TO DO: Explain here what this script does, and how to use it.
# Motivation: compute p x p covariance matrix.
import sys
import time
import numpy

# Set matrix dimensions
# if len (sys.argv) == 3:
#    mat_size = int(sys.argv[1])
# else:
#    mat_size = 10

n = 6000
p = 4000

# CREATE DATA
# -----------
# Create a random matrix, X.
print('Creating %d x %d matrix, X.' % (n,p))
X = numpy.random.random_sample((n,p))

# MATRIX COMPUTATION
# ------------------
# Compute X'*X.
print('Computing X\'*X (transpose of X times X).')
t = time.time()
R = X.T @ X
print('Computation took %0.2f seconds.' % (time.time() - t))
