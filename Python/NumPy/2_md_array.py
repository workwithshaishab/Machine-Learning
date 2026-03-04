import numpy as np
array1=np.array([
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
                ])
print(array1.shape)
print(array1[0,0,1])

# add 9, 8, 12, 27
numbers=array1[0,2,2]+array1[0,2,1]+array1[1,0,2]+array1[2,2,2]
print(numbers)

array2= np.array([[1,2,3], [5,6,7]])
print(np.size(array2))  # prints 6 as there are six elements in an array


arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
arr3d = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]],
                  [[9, 10], [11, 12]]])
print(arr1d.ndim)  # 1dimensional
print(arr2d.ndim)  # 2dimensional
print(arr3d.ndim)  # 3dimensional
