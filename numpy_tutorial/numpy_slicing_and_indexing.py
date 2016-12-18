import numpy as np

# Indexing on 1-D arrays is simple, as they act similar to python lists

'''
Single dimensional array
'''
arr = np.arange(15)
print(arr[5])
print(arr[5:8])
arr[5:8] = 12
print(arr)

arr_slice = arr[5:8]
print(arr_slice)
arr_slice[:] = 64;
print(arr)

# As we can see from above, numpy does not create a new memory space for arr_slice. This is because, numpy has been
# created with large data use cases in mind, performance and memory problems would come up if numpy copied data left
# and right.


'''
Multi-dimensional arrays
'''
array2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print(array2d[2])
print(array2d[0][2])
print(array2d[0, 2])

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [7, 8, 9], [10, 11, 12] ])
print(arr3d[0])


'''
Indexing
'''
print(array2d[:2])
print(array2d[:2, 1:])
print(array2d[1, 2:])

'''
Boolean Indexing
'''
print('=======================================================')
print('Boolean indexing')
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(names == 'Bob')
print(data[names == 'Bob'])
print(data[names == 'Bob', 2:])
print(data[names == 'Bob', 3])

# To select everything but Bob, you can either use != or negate the condition using -
print(data[-(names == 'Bob')])

#Selecting two of the three names to combine multiple boolean conditions, use boolean logical operations like & or |
print(data[(names == 'Bob') | (names == 'Will')])

# To set all the negative values in the array to zero:
data[ data < 0 ] = 0
print(data)

'''
Fancy indexing
'''
print('===================================')
print('Fancy indexing')
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print(arr)
print('Fancy indexing array:')
print(arr[[4, 3, 0, 6]])
print(arr[[-3, -5, -7]])



