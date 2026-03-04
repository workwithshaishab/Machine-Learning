import numpy as np

array1= np.array([1,2,3,4])
array2= np.array([True, False, True, False])
new_arr=array1[array2]
print(new_arr)


array3= np.array([15,16,17,18])
filter= []
for i in array3:
    if i>16:
        filter.append(True)
    else:
        filter.append(False)

print(array3[filter])

# Instead of looping, numpy allows you to do this
array3 = np.array([15,16,17,18])
new_arr = array3[array3 > 16]
print(new_arr)
