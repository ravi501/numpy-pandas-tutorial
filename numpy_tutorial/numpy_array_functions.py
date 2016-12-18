import numpy as np

'''
Universal functions perform element-wise operations on data in ndarrays
'''

arr = np.arange(8)

print(np.sqrt(arr))
print(np.exp(arr))

x = np.random.randn(8)
y = np.random.randn(8)
# Maximum prints the element-wise maximum
print(np.maximum(x, y))

