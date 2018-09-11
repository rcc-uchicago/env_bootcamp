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
