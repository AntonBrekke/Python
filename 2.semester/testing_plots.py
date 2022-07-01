import numpy as np
import matplotlib.pyplot as plt

def cubegrid_face(color):
    I = np.linspace(0, 1, 5)
    x, y, z = np.meshgrid(I, I, I, indexing='xy')

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for i in range(-1, 1):
        ax.plot_wireframe(x[0], y[i], z[0], color=color)
        ax.plot_wireframe(y[i], x[0], z[0], color=color)
        ax.plot_wireframe(x[0], y[:,0].transpose(), z[0, :,i][None,:], color=color)
    ax.scatter(0.5, 0.5, 0.5, color='yellow', s=250)


def cubegrid(color):
    I = np.linspace(0, 1, 5)
    x, y, z = np.meshgrid(I, I, I, indexing='ij')

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for i in range(len(x[0])):
        ax.plot_wireframe(x[i], y[i], z[i], color=color, alpha=0.4)
        ax.plot_wireframe(y[i], x[i], z[i], color=color, alpha=0.4)
    ax.scatter(0.5, 0.5, 0.5, color='yellow', s=250)

def sphere_grid(color):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    I = np.linspace(0, 1, 13)
    J = np.linspace(0, 2*np.pi, 13)
    K = np.linspace(0, np.pi, 13)

    R, theta, phi = np.meshgrid(I, J, K, indexing='xy')

    x = R*np.cos(theta)*np.sin(phi)
    y = R*np.sin(theta)*np.sin(phi)
    z = R*np.cos(phi)

    for i in range(0, len(x[0]), 3):
        ax.plot_wireframe(x[i], y[i], z[i], color=color, alpha=0.3)
        ax.plot_wireframe(y[i], z[i], x[i], color=color, alpha=0.3)
        ax.plot_wireframe(x[:,-1], y[:,-1], z[:,-1], color=color, alpha=0.5)


    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')

# cubegrid_face('r')
# cubegrid('g')
sphere_grid('r')
plt.show()
