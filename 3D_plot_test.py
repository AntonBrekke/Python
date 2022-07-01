import numpy as np

class Plot:
    def __init__(self, h0, R):
        self.h0 = h0
        self.R = R

    def h(self, x, y):
        h0, R = self.h0, self.R
        eq = (4-(x**2 + y**2)**0.5)**2
        return eq

    def q(self, x, y):
        h0, R = self.h0, self.R
        eq = h0/(1 + (x**2 + y**2)/R**2)
        return eq

plot = Plot(2277, 4)
t = np.linspace(-10, 10, 50)
x, y = np.meshgrid(t, t, indexing="ij")
h = plot.h(x,y)

t1 = np.linspace(-10, 10, 50)
x1, y1 = np.meshgrid(t1, t1, indexing="ij")
q = plot.q(x1,y1)

import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax = fig.add_subplot(121, projection="3d", xlabel="Plot 1", title=r'$cos\left(\frac{h0}{R}\cdot x\right) - sin^2\left(\frac{h0}{2R}\cdot y\right)+1$')
# ax.set_zlim3d(0, 5)
ax2 = fig.add_subplot(122, projection="3d", xlabel="Plot 2", ylabel = "Mountain", title=r'$\frac{h0}{1 + \frac{x^2+y^2}{R^2}}$')
surf = ax.plot_surface(x, y, h, rstride=1, cstride=1, cmap=plt.cm.ocean,
 linewidth=0, antialiased=False)
surf2 = ax2.plot_surface(x1, y1, q, rstride=1, cstride=1, cmap=plt.cm.terrain,
 linewidth=0, antialiased=False)
cbar_ax = fig.add_axes([0.4, 0.05, 0.025, 0.155])
fig.colorbar(surf, cax=cbar_ax)
cbar_ax2 = fig.add_axes([0.6, 0.05, 0.025, 0.155])
fig.colorbar(surf2, cax=cbar_ax2)
fig.suptitle("3D Plot")

plt.show()
