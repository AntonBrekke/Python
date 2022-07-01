import numpy as np
import matplotlib.pyplot as plt

N = 40
I = np.linspace(-1, 1, N)
x, y = np.meshgrid(I, I, indexing='ij')

CS = plt.contour(x, y, x**2 + y**2)
plt.clabel(CS, inline=1, fontsize=10, fmt='%1.2f', colors='k')
plt.quiver(x[::2, ::2], y[::2, ::2], 2*x[::2, ::2], 2*y[::2, ::2])  # Gradient
plt.axis('equal')
plt.show()
