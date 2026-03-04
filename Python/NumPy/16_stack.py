import numpy as np
array1= np.array([1,2,3])
array2= np.array([4,5,6])
print(np.stack((array1, array2)))   #axis=0 by default
print(np.stack((array1, array2), axis=1))

print(np.vstack((array1, array2)))
print(np.hstack((array1, array2)))
print(np.dstack((array1, array2)))