import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A = 1
w = -1
k = 1

def wave(x, t, k):
    return A*np.cos(k*x - w*t)

x = np.linspace(-10, 10, 400)
t = np.linspace(0, 30, 400)

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

k_lin = np.linspace(0, 10, 11)
c_lin = np.linspace(0, 5, 11)
c_lin = np.ones(11)

sumwave = 0
for i in range(len(k_lin)):
    sumwave += c_lin[i]*wave(x[None,:], t[:,None], k_lin[i])

def update(frame):
    p1, = ax1.plot(x, wave(x, t[frame], k), 'r')
    p2, = ax2.plot(x, sumwave[frame,:], 'r')
    # p3, = ax2.plot(x[frame], sumwave[frame, frame], 'bo')
    p4, = ax2.plot(x[320], sumwave[frame, 320], 'bo')
    return p1, p2, p4

ani = FuncAnimation(fig, update, frames=len(t), interval=10, blit=True)
plt.show()
