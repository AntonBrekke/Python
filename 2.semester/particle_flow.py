import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

I = np.linspace(-2*np.pi, 2*np.pi, 50)
x, y = np.meshgrid(I, I, indexing='xy')

u = x
v = y

fig, ax = plt.subplots()
plt.suptitle("Partikkel gjennom felt", fontweight='bold')
xdata, ydata = [], []

particle, = plt.plot(xdata, ydata, 'ro', markersize='2')
arrow = plt.quiver(x[::2, ::2], y[::2, ::2], u[::2, ::2], v[::2, ::2])

"""
if np.min(r[:,0]) > 0:
    xmin = -0.1
else:
    xmin = np.min(r[:,0])*1.5
"""
print(u)
def init():
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    return particle, # Kan være vilkårlig av ln, line, ln_ball. Kan ha bare ln, kan ha alle tre, kan ha to av dem etc. men må ikke ha akkurat den

def update(frame):
    xdata.append(u[0][frame])
    ydata.append(v[frame][0])
    particle.set_data(xdata[-1:], ydata[-1:])
    return particle, arrow,      # Må returnere alle biter som skal animeres

ani = FuncAnimation(fig, update, frames=[i for i in range(len(I))], interval=20, init_func=init, blit=True)

writer = PillowWriter(fps=25)
plt.legend()
# ani.save("pendulum_klasse.gif", writer=writer)
plt.show()
