import sys, os
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print('shape of x_train.shape = ',x_train.shape)
print('shape of t_train = ',t_train.shape)
print('shape of x_test = ',x_test.shape)
print('shape of t_test = ',t_test.shape)
