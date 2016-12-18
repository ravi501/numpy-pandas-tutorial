import numpy as np


'''
Data types for ndarray

The data type or dtype is a special object containing information the ndarray needs to interpret a chunk of memory as
a particular data type
'''

arr1 = np.array([1, 2, 3], dtype=np.float64)
print(arr1)
print(arr1.dtype)

arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr2)
print(arr2.dtype)

# astype converts one data type to an other data type
arr3 = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr3.astype(np.int32))