# ravel() is an array method, not a NumPy function.
# That means you call it on the array itself, not on the np module.

import numpy as np
array= np.array([[1,2,3],[4,5,6]])
ravel = array.ravel()
print(ravel)
ravel[0]= 20 # Changes in the raveled array may affect the original array.
print(ravel)
print(array)

# Returns a view of the original array whenever possible (no copy).
# Faster and memory-efficient.
