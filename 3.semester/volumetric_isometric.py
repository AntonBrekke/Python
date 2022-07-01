import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = np.linspace(-5, 5, 25)
y = np.linspace(-5, 5, 25)
z = np.linspace(-5, 5, 25)
rx, ry, rz = np.meshgrid(x, y, z, indexing='xy')

V = rz**2

cmap = plt.get_cmap('plasma')
print(cmap(1000))

for i in range(len(z)):
    # print(cmap(V[:,:,i:i+1]))
    ax.plot_surface(rx[:,:,i], ry[:,:,i], V[:,:,i], alpha=0.4, color=cmap(z[i]))

plt.show()

V = np.exp(-rz**2)


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
