# Transpose of a matrix means interchanging rows and columns.
import numpy as np
array= np.array([[1,2,3],[4,5,6]])
print(array.transpose())    # this is an array method.
print(np.transpose(array))  # this is a numpy function.
print(array.T)