import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-5, 5, 50)
Y = np.linspace(-5, 5, 50)

x, y = np.meshgrid(X, Y, indexing='ij')

u = x
v = -y

Psi = x*y
phi = 1/2*(x**2 - y**2)

C = (1,1,1)
fig = plt.figure(facecolor=C)
ax = fig.add_subplot(facecolor=C)
# ax.spines['bottom'].set_color('w')      # Setter aksen hvit
# ax.spines['left'].set_color('w')
# ax.tick_params(axis='x', colors='w')    # Setter ticks hvit
# ax.tick_params(axis='y', colors='w')

len = np.sqrt(u**2 + v**2)
N = 2

ax.quiver(x[::N, ::N], y[::N, ::N], u[::N, ::N], v[::N, ::N])
ax.contour(x, y, Psi, levels=10, colors='r')
ax.contour(x, y, phi, levels=10, colors='b', linestyles='dashed')
ax.plot([0,0], [0,0], 'ko', markersize=12)
plt.show()
