import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
Contour-plot av samme funksjon i
animate_scalarfield.py
"""

fig = plt.figure(facecolor='k')
ax = fig.add_subplot()

N = 70
M = 80

I = np.linspace(-5, 5, N)
J = np.linspace(-5, 5, N)


x, y = np.meshgrid(I, J, indexing='ij')
z_array = np.zeros((N, N, M))


f = lambda x, y, t: x**2 - np.sin(2*t)*y**2 + 10*np.sin(2*t)*np.cos(x)

t = np.linspace(0, 2*np.pi, M)
for i, t_i in enumerate(t):
   z_array[:, :, i] = f(x, y, t_i)


maxx = np.max(x)
maxy = np.max(y)

ax.tick_params(axis='x', colors='w')    # Setter ticks hvit
ax.tick_params(axis='y', colors='w')    # Setter ticks hvit
ax.spines['bottom'].set_color('w')      # Setter aksen hvit
ax.spines['left'].set_color('w')

def update(frame):
    ax.cla()
    ax.set_xlabel('x', color='w', weight='bold', fontsize=16)
    ax.set_ylabel('y', color='w', weight='bold', fontsize=16)
    contour = ax.contourf(x, y, z_array[:,:,frame], cmap='jet', levels=100)
    timelabel = ax.text(0.7*maxx, 0.8*maxy, f't={t[frame]:.1f}', fontsize=16, backgroundcolor='w')


ani = FuncAnimation(fig, update, frames=len(t), interval=1, blit=False)

plt.show()
