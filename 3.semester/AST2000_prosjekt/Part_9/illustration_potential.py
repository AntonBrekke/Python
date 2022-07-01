import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot()

x = np.linspace(1, 10, 500)
ground = lambda x: 1 + np.exp(-0.2*x)*np.cos(x - 2)

N = 10000
time = 10
dt = time / N
g = np.array([0, -9.81])
r = np.zeros((N,2))
v = np.zeros((N,2))
r[0] = (4, ground(4))
v[0] = (1,0)

for i in range(N-1):
    v[i+1] = v[i] + g*dt
    if r[i, 1] <= ground(r[i, 0]):
        r[i+1, 0] = r[i, 0] + v[i+1, 0]*dt
        r[i+1, 1] = ground(r[i+1, 0])


gr, = ax.plot(x, ground(x))
line, = ax.plot(r[0,0], r[0,1], 'ro')
def animate(frame):
    line.set_data(r[frame, 0], r[frame, 1])
    return line, gr

ani = FuncAnimation(fig, func=animate, frames=[i for i in range(0, N, 10)], interval=10, blit=True, repeat=True)
plt.show()
