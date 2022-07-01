import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-5, 5, 200)
x, y = np.meshgrid(I, I, indexing='ij')
true = True
while true:
    A = input('gradient or streamline?')
    if A == 'streamline':
        plt.quiver(x[::8, ::8], y[::8, ::8], np.sin(y)[::8, ::8], -2*x[::8, ::8])
        true = False
    elif A == 'gradient':
        plt.quiver(x[::5, ::5], y[::5, ::5], 2*x[::5, ::5], np.sin(y)[::5, ::5])
        true = False
K = [*range(0, 10)]
plt.contour(x, y, x**2-np.cos(y), K, cmap='jet')
# plt.scatter(x[::5, ::5], y[::5, ::5], color='k', s=5)
plt.axis('equal')
plt.show()
