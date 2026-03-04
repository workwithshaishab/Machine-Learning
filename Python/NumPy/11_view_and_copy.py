import numpy as np

# Copy=>
# Makes a new array in memory.
# Changes in copy does not affect the original array.
# Safer, but uses more memory.
array1= np.array([1,2,3,4])
array2= array1.copy()  # creates a copy of array1
array2[3]=5
print(array1)
print(array2)


# View=>
# Creates a different object but shares the same data in memory.
# Changes in view affect the original array.
# Saves memory, but can cause unintended side effects.
array3= np.array([5,6,7,8])
array4= array3.view()  # creates a view of array1
array4[1]=0
print(array3)
print(array4)