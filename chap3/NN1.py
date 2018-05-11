# page 86 - 88
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identity_fucntion(x):
    return x

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print('shape of X = ', X.shape)
print('shape of W1 = ', W1.shape)
print('shape of B1 = ', B1.shape)

A1 = np.dot(X, W1) + B1

Z1 = sigmoid(A1) # activation function

print('A1 = ', A1)
print('Z1 = ', Z1)

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3,0.6]])
B2 = np.array([0.1, 0.2])

print('shape of Z1 = ', Z1.shape)
print('shape of W2 = ', W2.shape)
print('shape of B2 = ', B2.shape)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

print('shape of Z2 = ', Z2.shape)
print('shape of W3 = ', W3.shape)
print('shape of B3 = ', B3.shape)

A3 = np.dot(Z2, W3) + B3
Y = identity_fucntion(A3)

print('A3 = ', A3)
print('Y = ', Y)
