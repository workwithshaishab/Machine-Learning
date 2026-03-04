# Vectorization means replacing explicit Python loops with array operations.
# Instead of iterating element-by-element, NumPy applies the operation to the whole array at once.

import numpy as np
array1= np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
result= array1**2
print(result)