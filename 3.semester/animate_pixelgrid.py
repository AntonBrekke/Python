import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.animation import FuncAnimation
from numba import njit

fig = plt.figure()
ax = fig.add_subplot()

Px = 32
Py = 32

I = np.linspace(-0.5, Px-0.5, Px+1)
J = np.linspace(-0.55, Py-0.55, Py+1)

X, Y = np.meshgrid(I, J, indexing='xy')

# ax.axis('equal')
# ax.plot(X, Y, 'k', alpha=0.8)
# ax.plot(X.T, Y.T, 'k', alpha=0.8)
# plt.show()

# pixel = ax.imshow(np.zeros_like(X))

cmap = colors.ListedColormap(['red', 'navy', 'pink', 'limegreen', 'purple', 'orange', 'royalblue', 'gray'])
bounds = np.linspace(0, 1, 9)
norm = colors.BoundaryNorm(bounds, cmap.N)

def update(frame):
    @njit
    def datz():
        data_arr = np.zeros((Py, Px))
        for i in range(Py):
            for j in range(Px):
                data_arr[i,j] = np.random.uniform(0,1)
        return data_arr
    data = datz()
    pixel = ax.imshow(data, cmap=cmap)
    plt.xticks([])
    plt.yticks([])
    return pixel,
# draw gridlines

ani = FuncAnimation(fig, update, frames=[i for i in range(0,1000)], interval=5, blit=True)

plt.show()
