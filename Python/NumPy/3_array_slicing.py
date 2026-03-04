import numpy as np

array=np.array([[ 1, 2, 3, 4, 5],
 [6, 7, 8, 9, 10],
 [11, 12, 13, 14, 15]])
#print(array[1:3]) #1st and 2nd
#print(array[:1])     #Last
#print(array[1, 1:4]) #prints [7 8 9]
#print(array[0:3, 2])  #prints [3 8 13]
#print(array[0:3, 1:4]) #prints [2 3 4 7 8 9 12 13 14]
print(array[0,0])
print(array[1,4])


#array[start:end:step]
#print(array[::-1]) #reverse

arr= np.array([1,2,3,4,5,6,7,8,9])
#print(arr[2:5:2]) #prints [3 5]
#print(arr[0:7:3]) #prints [1 4 7]
