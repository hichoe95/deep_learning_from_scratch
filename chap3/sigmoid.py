import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])

print('x = ',sigmoid(x))

t = np.array([1.0, 2.0, 3.0])
print('t = ', t)
print('1. + t = ', 1.0 + t)
print('1. / t = ', 1./t)

a = np.arange(-5., 5., 0.1)
b = sigmoid(a)
plt.plot(a,b)
plt.ylim(-0.1, 1.1)
plt.show()
