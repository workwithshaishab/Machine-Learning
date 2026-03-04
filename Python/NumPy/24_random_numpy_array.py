import numpy as np
array1D= np.random.rand(5)
print(array1D)

array2D= np.random.rand(5,4)
print(array2D)

array_int_1D = np.random.randint(1, 10, size=5)  # 5 integers from 1 to 9, for 1D Array
print(array_int_1D)

arr_int_2D = np.random.randint(1, 10, size=(2,3))  # for 2D Array
print(arr_int_2D)

arr_int_3D = np.random.randint(1, 10, size=(2,3,3))  # for 2D Array
print(arr_int_3D)

array_normal = np.random.randn(5)   # mean=0, std=1
print(array_normal)

arr_choice = np.random.choice([10,20,30,40], size=5)
print(arr_choice)