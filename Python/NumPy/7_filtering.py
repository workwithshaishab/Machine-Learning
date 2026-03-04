# Boolean Masking

# Boolean masking in NumPy is a very powerful feature that lets you filter/select elements
# from an array based on conditions.

import numpy as np
array= np.array([10,20,30,40,50,60,70,80,90])
print(array[array>40])
print(array[array%20==0])
print(array[array<40])
print(array[array==100])
print(array[array==20])