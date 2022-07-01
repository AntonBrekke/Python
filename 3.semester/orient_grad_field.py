import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-5, 5, 20)

x, y = np.meshgrid(I, I, indexing='ij')

f = x**2 + y**2

u, v = np.gradient(f)

plt.contourf(x, y, f, cmap='plasma')
plt.quiver(x[::2, ::2], y[::2, ::2], u[::2, ::2], v[::2, ::2])
plt.show()
