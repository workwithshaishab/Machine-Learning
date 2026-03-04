# Broadcasting is a set of rules that NumPy follows when performing operations (like addition,
# multiplication, etc.) on arrays of different shapes.

# It allows NumPy to "stretch" the smaller array across the larger one without actually copying
# data, so operations become very efficient.

import numpy as np
array1= np.array([100,200,300])
deduction= 10 # 10%  scalar value
final_value=  array1-deduction/100*array1
print(final_value)


# A scalar is just a single number (not an array, not a list).
# It has no dimensions → shape () in NumPy.


# In 2D Array

# Matching dimension
array2= np.array([[10,20,30],[40,50,60]])
expand_value= [10,10,10]
result1=array2+expand_value
print(result1)


# Expanding single elements
array3= np.array([10,20,30])
array4= np.array([40])
result2= array3+array4
print(result2)


# Incompatible shapes=> This occurs errors
"""
array5= np.array([10,20,30])
array6= np.array([40,50])
result3= array5+array6
print(result3)
"""