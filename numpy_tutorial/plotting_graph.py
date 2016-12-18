import numpy as np
import matplotlib.pyplot as plt

# Using numpy arrays enables us to express many kinds of data processing tasks that might otherwise require writing
# loops. The practice of replacing loops with an array expression is called vectorization

points = np.arange(-5, 5, 0.01)
#print(points)
# meshgrid takes two 1D arrays and produces two 2-D matrices corresponding to all pairs of (x, y) in two arrays
xs, ys = np.meshgrid(points, points)
#print(xs)
#print(ys)

z = np.sqrt(xs **2 + ys ** 2)
#print(z)

plt.interactive(False)
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()

plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()
