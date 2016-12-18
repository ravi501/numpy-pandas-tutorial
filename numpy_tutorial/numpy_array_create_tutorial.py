import numpy as np

'''
ndarrays

ndarray is a fast, flexible container offered by NumPy for large data sets in Python which enables us to peform
mathematical operations on whole blocks of data
'''

# The easiest way to create an array is to use the array function
data = [6, 7, 8.3, 9]
nd_array = np.array(data)
print(nd_array)

#When data types of all the elements are same, a ndarray with int dtype gets created
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
nd_array2 = np.array(data2)
print(nd_array2)
print(nd_array2.dtype)

#When the data types are different, ndarray converts all the elements to the element with a bigger dtype
data3 = [[1.0, 2.0, 3.0, 4.0], [5, 6.0, 7.0, 8.0]]
nd_array3 = np.array(data3)
print(nd_array3)
print(nd_array3.dtype)

# When the data type of one of the elements is a unicode character, ndarray converts all the
# elements to unicodes
data4 = [[1.0, 2.0, 3.0, 4.0], [5, '6.0', 7.0, 8.0]]
nd_array4 = np.array(data4)
print(nd_array4)
print(nd_array4.dtype)

# Zeroes and One's create and array with all zeroes or one's respectively
data5 = np.zeros(10)
print(data5)
data6 = np.zeros((3,4))
print(data6)

# Create empty arrays
data7 = np.empty((2,3,2))
print(data7)

# arange is an array-valued version of the built-in Python range function
data8 = np.arange(15)
print(data8)

'''
Array creation functions in NumPy

1) array            - Convert input data list (list, tuple, array) to an ndarray
2) arange           - Like the built-in range function in python, but returns an ndarray instead of a list
3) ones, ones_like/ - Produces an array of one's with given shape and dtype. ones_like takes another array and produces
  zeros, zeros_like   a one's array of same shape and size
4)empty, empty_like - Create new arrays by allocating new memory, but do not populate with any values
'''




