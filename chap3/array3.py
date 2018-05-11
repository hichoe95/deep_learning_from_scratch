import numpy as np

A = np.array([[1,2,3], [4,5,6]])
print('A = ', A)
print('shape of A = ', A.shape)

B = np.array([[1,2],[3,4],[5,6]])
print('B = ', B)
print('shape of B = ', B.shape)

print('dot product of A and B = ', np.dot(A,B))
