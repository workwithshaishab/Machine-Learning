"""
searchsorted() which performs a binary search in the array, and returns the index where
the specified value would be inserted to maintain the search order.

The searchsorted() method is assumed to be used on sorted arrays.
"""

import numpy as np
array1= np.array([1,2,3,4,5,4,4])
print(np.where(array1==4))
print(np.where(array1%2==0)),
print(np.searchsorted(array1, 5))

array2= np.array([3,4,5,6,7,8,9])
print(np.searchsorted(array2, 4, side='right'))   # prints 2 as the number 4 must be inserted in index 2
print(np.searchsorted(array2, 1, side='right'))  # at rightward, if 1 must be inserted it should be
                                                       # in index 0
print(np.searchsorted(array2,4))   # by default side is left   prints 2
print(np.searchsorted(array2,4, side='right'))   #prints 1

arr = np.array([1, 3, 5, 7])
print(np.searchsorted(arr, [2, 4, 6]))   # 1 2 3, 2 would be inserted in index1 4 in index2 and 6 in index3
                                               # only one of them from 2,4,6 is inserted. It just shows where the
                                               # numbers should be inserted