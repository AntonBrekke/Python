import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

fig = plt.figure(facecolor='k', figsize=(8,8))
ax = fig.add_subplot()
ax.set_facecolor('k')
ax.set_title('Animated quiver', fontsize=20, weight='bold', color='w')

N = 55

I = np.linspace(-5, 5, N)
J = np.linspace(-5, 5, N)

x, y = np.meshgrid(I, J, indexing='xy')

t = np.linspace(0, 2*np.pi, 100)

maxx = np.max(x) - 1
maxy = np.max(y) - 0.2

def update(frame):
    u = np.cos(t[frame])*2*y - np.sin(t[frame])*y
    v = np.sin(t[frame])*y + np.cos(2*t[frame])*x
    len = np.sqrt(u**2 + v**2)
    plot = ax.quiver(x[::2, ::2], y[::2, ::2], u[::2, ::2], v[::2, ::2], len[::2, ::2], cmap='gist_rainbow')
    timelabel = ax.text(maxx, maxy, f't={t[frame]:.1f}', fontsize=16, backgroundcolor='w')
    return plot, timelabel

ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)
# writergif = PillowWriter(fps=30)
# ani.save('quiver_ani.gif', writer=writergif)
"""
Lagringen funker ikke :(
"""
plt.show()
