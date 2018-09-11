import pysal
import numpy as np

f = pysal.open(pysal.examples.get_path("stl_hom.txt"))

y = np.array(f.by_col['HR8893'])

w = pysal.open(pysal.examples.get_path("stl.gal")).read()

print ("\n\n")

print ("w = " + str(w) + "\n")  # print Weight object reference

mi = pysal.Moran(y, w, two_tailed=False)

print ("%.3f"%mi.I + "\n") 

print (str(mi.EI) + "\n")

print ("%.5f"%mi.p_norm + "\n")

# print (help(mi))