import numpy as np
import matplotlib.pyplot as plt
from numba import njit


A = 2
B = 1.5
x = np.linspace(0, 2*np.pi, 200)
f = A*np.sin(B*x)

sigma = np.random.normal(0, 1, x.shape)
ff = f + sigma
plt.plot(x, ff)

@njit
def f_model(A, B, x):
    return A*np.sin(B*x)

A = np.linspace(1.8, 2.2, 500)
B = np.linspace(1.3, 1.7, 500)

@njit
def least_squares():
    sq = np.zeros((len(A), len(B)))
    for i in range(len(A)):
        for j in range(len(B)):
            sq[i,j] = np.sum((ff - f_model(A[i], B[j], x))**2)
    min = np.min(sq)
    where = np.where(sq==min)
    i, j = where
    return min, i, j

min, i, j = least_squares()
print(i,j)
print(A[i], B[j], min)
plt.plot(x, f_model(A[i], B[j], x))
plt.show()
