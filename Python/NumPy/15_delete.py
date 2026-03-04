import numpy as np

# DELETING 1D ARRAY
array1= np.array([1,2,3,4,5,6,7])
new_arr1= np.delete(array1, 2, axis=0)
print(new_arr1)

# DELETING 2D ARRAY
array2= np.array([[1,2,3],[4,5,6]])
new_arr2= np.delete(array2,0, axis=0)  #deleting first row
print(new_arr2)
new_arr3= np.delete(array2,0, axis=1)  #deleting first column
print(new_arr3)
# DELETING 3D ARRAY
array3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
new_arr4= np.delete(array3, 1, axis=0)
print(new_arr4)
new_arr5= np.delete(array3, 1, axis=1)
print(new_arr5)