import numpy as np
array1= np.array([1,2,3,4,'reyna'])
print(np.astype(array1, list))

array2= np.array([10,20,30,40])
print(np.astype(array2, bool))
print(np.astype(array2, float))

arr1= np.array([1.3,2.6,9.9])
arr_as_int= arr1.astype(int)  # converts stored elements into integer datatype
print(arr_as_int)
print(arr_as_int.dtype)