import numpy as np
array= np.array([1,2,3,4,5])
array= array*2
print(array)
print(type(array))  # type of array
print(array.dtype)  # type of data stored in array
# arr * 2 applies the operation element-wise.
# Unlike Python lists (where you’d need a loop), NumPy does this in one step.

arr2= np.zeros(0)
print(arr2)

arr3= np.zeros(2,int)
print(arr3)

arr4= np.zeros((2,3))
print(arr4)
