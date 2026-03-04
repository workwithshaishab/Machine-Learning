#Reshaping means changing the shape of an array eg. 1D to 2D
#Reshaping does not create copy

import numpy as np
array= np.array([10,20,30,40,50,60,70,80,90])
print(array)
print(array.shape) #first dimensions has 9 elements
new_arr=array.reshape(3,3)
print(new_arr)

array1=np.array([[1,2,3], [4,5,6]])
print(array1.shape)   #prints 2,3  first dimension has 2 elements second dimension has 3 elements

print("Shape=",np.shape(array))  # This is a numpy function, the code previously was an array method.