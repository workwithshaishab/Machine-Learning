import numpy as np
array1= np.array([10,20,30,40,50])
array2= np.array([60,70,80,90])
new_arr1= np.append(array1,array2, axis=0)  #values of array2
print(new_arr1)
new_arr2= np.append(array1, [100,200])  #by default axis=0
print(new_arr2)


#Appending 2D Array
array3= np.array([[1,2,3],[4,5,6]])
array4= np.array([[10,20,30],[40,50,60]])
new_arr3= np.append(array3, array4, axis=1)
print(new_arr3)