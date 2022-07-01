import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
gs = fig.add_gridspec(3,2)
ax1 = fig.add_subplot(gs[0, 1], projection='3d', title=r'3D plot of $\vec{r}(t)$')
ax2 = fig.add_subplot(gs[1, 1], projection='3d')
ax3 = fig.add_subplot(gs[0::, 0], projection='3d')
ax4 = fig.add_subplot(gs[2, 1], projection='polar')

t = np.linspace(-4*np.pi, 4*np.pi, 300)

z = np.linspace(-5, 5, 300)

r = z**2 + 1
x = r*np.cos(t)
y = r*np.sin(t)

ax1.plot3D(x, y, z)

# Plotter en kule
theta = np.linspace(0, 2*np.pi, 20)
phi = np.linspace(-np.pi/2, np.pi/2, 20)
theta, phi = np.meshgrid(theta, phi, indexing='ij')
r = 1
x = r*np.cos(theta)*np.cos(phi)
y = r*np.sin(theta)*np.cos(phi)
z = r*np.sin(phi)

ax2.plot_surface(x, y, z, cmap=plt.cm.jet)
ax3.plot_wireframe(x, y, z, color='r')

c1 = np.linspace(-np.pi/4, np.pi/4, 800)
c2 = np.linspace(3*np.pi/4, 5*np.pi/4, 800)
ax4.plot(c1, np.sqrt(np.cos(2*c1)), c2, np.sqrt(np.cos(2*c2)))
fig.tight_layout()
plt.show()
