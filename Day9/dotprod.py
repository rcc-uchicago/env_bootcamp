import sys
import time
import numpy as np

# Set matrix dimensions
if len (sys.argv) == 2 :
   mat_size = int(sys.argv[1])
else:
   mat_size = 10

# Define the a and b random matrices
a = np.random.random_sample((mat_size, mat_size))
b = np.random.random_sample((mat_size, mat_size))
# set initial time
t = time.time()
# compute dot product
n = np.dot(a,b)
elapsed_time = time.time()  -t
print('NUMPY DOT PRODUCT TIME ELAPSED:  %s SECONDS.' % (elapsed_time))

# EOF
