#Operations on Numpy arrays
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))
a = np.array([1, 2, 3, 5, 6])
print(np.add(arr, a))
print(np.subtract(arr, a))
print(np.negative(arr, a))
print(np.multiply(arr, a))
print(np.floor_divide(arr, a))
print(np.mod(arr, a))
#Output
# 15
# [ 2  4  6  9 11]
# [ 0  0  0 -1 -1]
# [-1 -2 -3 -4 -5]
# [ -1  -4  -9 -16 -25]
# [-1 -1 -1 -1 -1]
# [0 0 0 0 0]