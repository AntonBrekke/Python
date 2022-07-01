import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

N = 10

I = np.linspace(0, 1, N)
J = np.linspace(0, 2*np.pi, N)
K = np.linspace(0, np.pi, N)

R, theta, phi = np.meshgrid(I, J, K, indexing='xy')

x = R*np.cos(theta)*np.sin(phi)
y = R*np.sin(theta)*np.sin(phi)
z = R*np.cos(phi)


for i in range(0, len(x[0])):
    # ax.plot_wireframe(x[i], y[i], z[i])
    # ax.plot_wireframe(x[:,i], y[:,i], z[:,i], alpha=0.3)






plt.show()
