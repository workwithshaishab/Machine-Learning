# flatten() is an array method, not a NumPy function.
# That means you call it on the array itself, not on the np module.

import numpy as np
array= np.array([[1,2,3],[4,5,6]])
flatten=array.flatten()
print(flatten)
flatten[0]=10    # changing flatten array won't change original array
print(flatten)
print(array)

# Returns a new copy of the array (modifying it won’t affect the original array).
# Always 1D.
