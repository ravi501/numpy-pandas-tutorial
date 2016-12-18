import numpy as np

'''
Arrays in numpy let you apply an operation on all the elements. This is called vectorization.

Any arithmetic operation between equal-sized arrays applies the operation element-wise
'''

arr = np.array( [[1., 2., 3.],
                [4., 5., 6.]])

# Multiplying two arrays is done element-wise
arr1 = arr * arr
print(arr1)

arr2 = arr - arr
print(arr2)

arr3 = 1/arr
print(arr3)

arr4 = arr ** 0.5
print(arr4)


