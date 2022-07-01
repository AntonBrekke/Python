import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-2*np.pi, 2*np.pi, 50)
x, y = np.meshgrid(I, I, indexing='xy')

"""
index 'ij' gir matrisen x_ij = [[0. 0. 0.], [0.5 0.5 0.5], [1. 1. 1.]]
og y_ij = [[0. 0.5 1.], [0. 0.5 1.], [0. 0.5 1.]] = transpose(x) for:

I = np.linspace(0, 1, 3)
x_ij, y_ij = np.meshgrid(I, I, indexing='ij')

index 'xy' gir matrisen x_xy = transpose(x_ij)
og y_xy = transpose(y_ij) for:

I = np.linspace(0, 1, 3)
x_xy, y_xy = np.meshgrid(I, I, indexing='xy')
"""
"""
plt.quiver(x[::2, ::2], y[::2, ::2], np.cos(x)[::2, ::2], np.sin(y)[::2, ::2])
plt.show()

# print(x)      # N x N - matrise, x = transponert(y)
print()
# print(y)      # # N x N - matrise, y = transponert(x)
A = [[1,2,3], [2,2,2], [6,4,2]]
B = [[1,1,1], [3,4,1], [2,3,1]]
x = [A[i][1:] for i in range(0, len(A), 2)]
print(x)
"""
u = np.log(abs(y)) + np.cos(np.exp(x) + y)
v = np.log(abs(x)) + np.sin(np.exp(y) + x)

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.quiver(x[::2, ::2], y[::2, ::2], u[::2, ::2], v[::2, ::2], np.sqrt(u**2 + v**2)[::2, ::2], cmap='jet')
ax2.streamplot(x, y, u, v, color = np.sqrt(u**2 + v**2), cmap='jet')
plt.show()
