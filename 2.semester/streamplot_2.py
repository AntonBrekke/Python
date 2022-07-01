import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-3, 3, 40)
x, y = np.meshgrid(I, I, indexing='xy')
u = -x
v = y
speed = np.sqrt(u**2 + v**2)

fig, ax = plt.subplots(1,2)
strm = ax[1].streamplot(x, y, u, v, color = speed, cmap='autumn')
fig.colorbar(strm.lines)

ax[0].contour(x, y, -x*y, 10)
ax[0].quiver(x[::2, ::2], y[::2, ::2], -x[::2, ::2], y[::2, ::2])

plt.show()
