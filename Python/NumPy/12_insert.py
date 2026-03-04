import numpy as np
array= np.array([10,20,40,50,60,70])
print(array)
new_arr= np.insert(array, 2, 30, axis=0) # axis=0=>rows and axis=1=>
# if axis=0 not written, default value is axis=0 i.e. in rows
print(new_arr)


# Now Lets see in 2D array
array_2d= np.array([[1,2],[3,4],[5,6]])
print(array_2d)

# Insert a row [0,2] after [1,2]
new_arr2= np.insert(array_2d, 1, [0,2], axis=0)
print(new_arr2)

# Insert a column
new_arr3= np.insert(array_2d, 2, [7,8,9], axis=1)
print(new_arr3)

# Now lets see when axis=none, it inserts in a flattened array
new_arr4= np.insert(array_2d, 2, [7,8,9,10], axis=None) #prints 1,2,7,8,9,10,3,4,5,6
print(new_arr4)
