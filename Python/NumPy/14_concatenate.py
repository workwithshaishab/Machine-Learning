import numpy as np
array1= np.array([1,2,3,4])
array2= np.array([5,6,7,8])
new_arr1= np.concatenate((array1,array2), axis=0)
print(new_arr1)


# Concatenating 2D Array
array3= np.array([[1,2,3],[4,5,6]])
array4= np.array([[10,20,30],[40,50,60]])
new_arr2= np.concatenate((array3,array4), axis=0)
print(new_arr2)

new_arr3= np.concatenate((array3,array4), axis=1)
print(new_arr3)   # prints 1 2 3 10 20 30      4 5 6 40 50 60


# Concatenating 3D Array
array5 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
array6 = np.array([
    [[9, 10], [11, 12]],
    [[13, 14], [15, 16]]
])
new_arr4= np.concatenate((array5,array6), axis=0)
print(new_arr4)

new_arr5= np.concatenate((array5, array6), axis=1)
print(new_arr5)