import numpy as np
# checking nan(Not a number)
array1= np.array([1,2,np.nan,4,np.nan,5,6,np.nan,7,8,9])
print(np.isnan(array1))

# not a number to number
clean_array1= np.nan_to_num(array1)   #default value is 0
clean_array2= np.nan_to_num(array1, nan=10)
print(clean_array1)
print(clean_array2)


# checking infinite value
array2= np.array([1,2,np.inf,4,5,-np.inf])
print(np.isinf(array2))
clean_array3= np.nan_to_num(array2, posinf=3, neginf=6)
print(clean_array3)