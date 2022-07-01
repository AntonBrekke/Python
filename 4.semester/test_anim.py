import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])[:,None]
L = 0.65
f = 1    # Hz
k = np.pi*n / L
w = 2*np.pi*f
A = n

x = np.linspace(0, L, 1000)
t = np.linspace(0, 10, 1000)

f = lambda x, t: A*np.sin(k*x)*np.cos(w*t)


fig = plt.figure()
ax = fig.add_subplot()

def update(frame):
    ax.clear()
    ax.set_ylim(-1.1*A, 1.1*A)
    ax.set_xlabel('x', fontsize=16, weight='bold'); ax.set_ylabel('f', fontsize=16, weight='bold')
    tot = np.sum(f(x, t[frame]), axis=0)
    p, = ax.plot(x, tot, color='r')
    return p,

ani2 = FuncAnimation(fig, update, frames=len(t), interval=10, blit=True)
plt.show()
