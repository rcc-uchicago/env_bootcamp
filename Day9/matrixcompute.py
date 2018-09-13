#!/usr/bin/env python

# TO DO: Explain here what this script does, and how to use it.
import sys
import time
import numpy

# Set matrix dimensions
# if len (sys.argv) == 3:
#    mat_size = int(sys.argv[1])
# else:
#    mat_size = 10

n = 6000
m = 4000

# CREATE DATA
# -----------
# Create random matrices, A and B. Define the a and b random matrices
print('Creating %d x %d matrices A and B.\n' % (n,m))
A = numpy.random.random_sample((n,m))
B = numpy.random.random_sample((n,m))

# MATRIX COMPUTATION
# ------------------
# Compute A'*B.
print('Multiplying transpose of A times B.')
t = time.time()
Y = A.T @ B
print('Computation took %0.2f seconds.' % (time.time() - t))
