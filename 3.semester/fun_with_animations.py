import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot()

x = np.linspace(0, 10, 400)
a = np.linspace(0.1, 5, 600)

def update(frame):
    f = np.cos(a[1-frame]*x)*np.sin(a[frame]*x)*np.exp(-a[frame]*x)
    func, = ax.plot(x,f)
    func.set_data(x,f)
    labels = np.linspace(np.min(f), np.max(f), 8)
    ax.set_yticks(labels)
    # ax.set_ylim(np.min(f), np.max(f))
    return func,

ani = FuncAnimation(fig, update, frames=[i for i in range(len(a))], interval=20, blit=True)
plt.show()

fig = plt.figure()
ax = fig.add_subplot()

r = 2
theta = np.linspace(0, 2*np.pi, 200)
xdata, ydata = [], []
ax.axis('equal')

def init():
    ax.set_xlim(-(r+1), (r+1))
    ax.set_ylim(-(r+1), (r+1))
    return ()

def cupdate(frame):
    circle, = ax.plot([], [], linewidth=5)
    x = r*np.cos(theta[frame])
    y = r*np.sin(theta[frame])
    xdata.append(x)
    ydata.append(y)
    circle.set_data(xdata, ydata)
    return circle,

ani = FuncAnimation(fig, cupdate, frames=[i for i in range(len(theta))], init_func=init, interval=20, blit=True, repeat=False)
plt.show()
