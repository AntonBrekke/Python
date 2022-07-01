import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
ax = fig.add_subplot()

theta = np.linspace(-5, 10, 400)
xdata, ydata = [], []
plot, = ax.plot([], [], 'r')

def init():
    f = 6*np.cos(2*theta)*np.exp(-0.4*theta)
    ax.set_xlim(-5, 10)
    ax.set_ylim(np.min(f), np.max(f))
    return ()

def update(frame):
    f = 6*np.cos(2*theta[frame])*np.exp(-0.4*theta[frame])
    xdata.append(theta[frame])
    ydata.append(f)
    plot.set_data(xdata, ydata)
    return plot,

ani = FuncAnimation(fig, update, frames=[i for i in range(len(theta))], interval=10, init_func=init, blit=True, repeat=False)
plt.show()
