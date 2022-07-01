import matplotlib.pyplot as plt
import numpy as np


# prepare some coordinates
x, y, z = np.indices((8, 8, 8))

# draw cuboids in the top left and bottom right corners, and a link between
# them
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & (y >= 5) & (z >= 5)
link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

# combine the objects into a single boolean array
voxels = cube1 | cube2 | link

# set the colors of each object
colors = np.empty(voxels.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
colors[cube2] = 'green'

# and plot everything
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxels, facecolors=colors, edgecolor='k', alpha=0.5)

plt.show()


def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x

# prepare some coordinates, and attach rgb values to each
r, g, b = np.indices((17, 17, 17)) / 16.0
rc = midpoints(r)
gc = midpoints(g)
bc = midpoints(b)

# define a sphere about [0.5, 0.5, 0.5]
sphere = (rc - 0.5)**2 + (gc - 0.5)**2 + (bc - 0.5)**2 < 0.5**2

# combine the color components
colors = np.zeros(sphere.shape + (3,))
colors[..., 0] = rc
colors[..., 1] = gc
colors[..., 2] = bc

# and plot everything
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r, g, b, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
ax.set(xlabel='r', ylabel='g', zlabel='b')

I = np.linspace(1, 5, 11)
J = np.linspace(0, 2*np.pi, 11)
K = np.linspace(0, np.pi, 11)


x = np.linspace(-5, 5, 25)
y = np.linspace(-5, 5, 25)
z = np.linspace(-5, 5, 25)
rx, ry, rz = np.meshgrid(x, y, z, indexing='xy')

r, theta, phi = np.meshgrid(I, J, K, indexing='xy')
px = r*np.cos(theta)*np.sin(phi)
py = r*np.sin(theta)*np.sin(phi)
pz = r*np.cos(phi)
V = rz + rx

import plotly.graph_objects as go

fig = go.Figure(data=go.Volume(
    x = rx.flatten(),
    y = ry.flatten(),
    z = rz.flatten(),
    value = V.flatten(),
    opacity = 0.5,
    surface_count = 20, # number of isosurface
    colorscale='plasma'
))
fig.show()
