import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-5, 5, 40)
x, y = np.meshgrid(I, I, indexing='xy')

psi = 0.5*(y**2 - x**2)
phi = -x*y

plt.contour(x, y, psi, 10, colors='royalblue')
plt.contour(x, y, phi, 10, colors='r')
plt.quiver(x[::2, ::2], y[::2, ::2], -y[::2, ::2], -x[::2, ::2])
plt.show()


# ALternativ fra Mikael:

x = np.linspace(-1, 1, 1000)[:,None]
C = np.linspace(-1, 1, 5)[None,:]
plt.plot(x, -C/5/x, '--')
plt.plot(x, np.sqrt(2*C/10 + x**2), x, -np.sqrt(2*C/10 + x**2))
plt.axis([-1, 1, -1, 1])
plt.show()
