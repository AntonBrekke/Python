import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_subplot(projection='polar')

I = np.linspace(-40, 40, 30)


x, y = np.meshgrid(I, I, indexing='xy')
thetap = np.arctan(y / x)
thetan = -np.arctan(y / x)

theta = np.arctan(y / x)

Ex = 1 / np.sqrt(x**2 + y**2) * np.cos(theta)
Ey = 1 / np.sqrt(x**2 + y**2) * np.sin(theta)

Ex[:, :15] *= -1
Ey[:, :15] *= -1

# plt.contourf(x, y, V)
plt.quiver(x[::2, ::2], y[::2, ::2], Ex[::2, ::2], Ey[::2, ::2])
plt.show()
