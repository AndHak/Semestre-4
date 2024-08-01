#Producto punto entre una matriz y un vector

import numpy as np

A = np.array([[1,2,3], [4,5,6]])
B = np.array([1,2,3])

result = np.dot(A, B)

print("Producto punto de una matriz y un vector")
print(result)