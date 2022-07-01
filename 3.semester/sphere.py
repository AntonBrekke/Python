import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

r = 1
theta0 = np.pi/4
phi0 = np.pi/4

I = np.linspace(-np.pi/8 + phi0, np.pi/8 + phi0, 40)
J = np.linspace(-np.pi/8 + theta0, np.pi/8 + theta0, 40)

phi, theta = np.meshgrid(I, J, indexing='ij')

x = r*np.cos(phi)*np.sin(theta)
y = r*np.sin(phi)*np.sin(theta)
z = r*np.cos(theta)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.plot_wireframe(x,y,z)
plt.show()
