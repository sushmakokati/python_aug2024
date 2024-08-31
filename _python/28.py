import numpy as np
vector = np.arange(5)
print('Vector:', vector)
print("Vector shape:\n", vector.shape)

matrix = np.ones([3, 2])
print("Matrix:\n", matrix)
print("Matrix shape:\n", matrix.shape)

tensor = np.zeros([2, 3, 3])
print("Tensor:\n", tensor)
print("Tensor shape:\n", tensor.shape)

print(tensor[0][1][1]) #Prints the 1st Matrix's 2nd Row, 2nd element