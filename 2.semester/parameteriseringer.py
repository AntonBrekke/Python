import numpy as np
import matplotlib.pyplot as plt

R = np.linspace(1, 5, 4)[:,None]

I = np.linspace(0, 2*np.pi, 500)[:,None]
J = np.linspace(0, 5, 500)[:,None]

theta, z = np.meshgrid(I, J, indexing='ij')

r = (R*np.cos(theta), R*np.sin(theta), z)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(*r, color='r')
plt.show()
