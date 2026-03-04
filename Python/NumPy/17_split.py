import numpy as np

# Splitting 1D Array
array1=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.split(array1, 5))

# Let's access split array
array2=np.array([10,20,30,40,50,60,70,80,90,100])
new_arr1= np.split(array2,5)
print(new_arr1)
print(new_arr1[0])
print(new_arr1[1])
print(new_arr1[2])
print(new_arr1[3])
print(new_arr1[4])

# Splitting 2D Array
array3 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

new_arr2 = np.split(array3, 3)
print(new_arr2)
print(new_arr2[2])

new_arr3= np.split(array3, 2, axis=1)
print(new_arr3)

new_arr4 = np.hsplit(array3, 2)
print(new_arr4)

array4= array3.reshape(2,3,2)  #2 matrices of 3*2
print(array4)
new_arr5= np.split(array4,2)
print(new_arr5)

new_arr6= np.split(array4,3, axis=1)
print(new_arr6)