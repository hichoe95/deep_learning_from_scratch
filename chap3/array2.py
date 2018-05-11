import numpy as np

A = np.array([[1,2] , [3,4]])
print('A = ', A)
print('shape of A = ', A.shape)

B = np.array([[5,6],[7,8]])
print('B = ', B)
print('shape of B = ', B.shape)

print('dot product of A and B = ', np.dot(A,B))
