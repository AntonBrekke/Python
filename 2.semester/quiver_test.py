import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-3, 3, 50)
x, y = np.meshgrid(I, I, indexing='xy')

vx = x*y
vy = y*x

psi = 0.5*x**2*y - 1/6*y**3

# fig, (ax1, ax2) = plt.subplots(1,2)

plt.quiver(x[::2, ::2], y[::2, ::2], vx[::2, ::2], vy[::2, ::2])
# ax2.quiver(x[::2, ::2], y[::2, ::2], vx[::2, ::2], vy[::2, ::2])
# ax1.contour(x, y, psi, 70)
# ax2.streamplot(x, y, vx, vy)
plt.show()
