import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-5, 5, 100); G = np.linspace(-2, 8, 100)
x, y = np.meshgrid(G, I, indexing='ij')
gradf = plt.quiver(x[::4, ::4], y[::4, ::4], 1/x[::4, ::4], 2*y[::4, ::4])
z = [i for i in range(-30,31)]
plt.contour(x, y, np.log(x)+y**2, z)
plt.axis('equal')
plt.show()
