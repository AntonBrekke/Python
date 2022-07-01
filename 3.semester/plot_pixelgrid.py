import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

Px = 50
Py = 30

I = np.linspace(-0.5, Px-0.5, Px+1)
J = np.linspace(-0.55, Py-0.55, Py+1)

X, Y = np.meshgrid(I, J, indexing='xy')

plt.plot(X, Y, 'k', alpha=0.8)
plt.plot(X.T, Y.T, 'k', alpha=0.8)
# plt.axis('equal')
# plt.show()

data = np.zeros((Py, Px))
for i in range(Py):
    for j in range(Px):
        data[i,j] = np.random.uniform(0,1)

# create discrete colormap
cmap = colors.ListedColormap(['red', 'navy', 'pink', 'limegreen', 'purple', 'orange', 'royalblue'])
bounds = np.linspace(0, 1, 8)
norm = colors.BoundaryNorm(bounds, cmap.N)
plt.imshow(data, cmap=cmap)
plt.xticks([])
plt.yticks([])
# draw gridlines

plt.show()
