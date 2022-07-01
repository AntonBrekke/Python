import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 10)[None,:]
phi = np.linspace(0, np.pi, 10)[:,None]
R = np.linspace(1, 5, 10)

t, p, r = np.meshgrid(theta, phi, R)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = r*np.cos(t)*np.sin(p)
y = r*np.sin(t)*np.sin(p)
z = r*np.cos(p)
# ax.plot_wireframe(x, y, z, color='k', alpha=0.5)
ax.plot3D(t[0],p[0],R)
plt.show()
