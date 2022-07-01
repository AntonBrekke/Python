import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
Kopiert fra
https://www.tutorialspoint.com/how-to-animate-3d-plot-surface-in-matplotlib
EDIT: Jeg har redigert den så den funker etter hvordan jeg pleier å gjøre det,
men får ikke til å funke med blit=True
"""


N = 70
M = 80

fig = plt.figure(facecolor='k')
ax = fig.add_subplot(projection='3d')


I = np.linspace(-5, 5, N)
J = np.linspace(-5, 5, N)
x, y = np.meshgrid(I, J, indexing='xy')
zarray = np.zeros((N, N, M))

f = lambda x, y, t: x**2 - np.sin(2*t)*y**2 + 10*np.sin(2*t)*np.cos(x)

t = np.linspace(0, 2*np.pi, M)
for i, t_i in enumerate(t):
   zarray[:, :, i] = f(x, y, t_i)

minz = np.min(zarray)
maxz = np.max(zarray)
maxx = np.max(x)
maxy = np.max(y)

"""
# Kan sette akser etc. dersom man ønsker, husk ax.grid(False) i update
ax.w_xaxis.line.set_color('w')      # Setter aksen hvit
ax.w_yaxis.line.set_color('w')      # Setter aksen hvit
ax.w_zaxis.line.set_color('w')      # Setter aksen hvit
ax.xaxis.pane.set_color('k')        # Setter farge til pane (alternativt ax.xaxis.pane.fill = False)
ax.yaxis.pane.set_color('k')        # Setter farge til pane (alternativt ax.yaxis.pane.fill = False)
ax.zaxis.pane.set_color('k')        # Setter farge til pane (alternativt ax.zaxis.pane.fill = False)
ax.xaxis.pane.set_edgecolor(None)       # Fjerner kanten
ax.yaxis.pane.set_edgecolor(None)       # Fjerner kanten
ax.zaxis.pane.set_edgecolor(None)       # Fjerner kanten
ax.tick_params(axis='x', colors='w')    # Setter ticks hvit
ax.tick_params(axis='y', colors='w')    # Setter ticks hvit
ax.tick_params(axis='z', colors='w')    # Setter ticks hvit
"""

def update(frame):
    ax.cla()
    ax.axis('off')        # Skrur av alle akser
    # ax.grid(False)      # Fjerner grid (trenger ikke hvis ax.axis('off') er på)
    ax.set_zlim(minz, maxz)
    ax.set_facecolor('k')       # Setter farge rundt plott til svart
    plot = ax.plot_surface(x, y, zarray[:, :, frame], cmap='hot')
    timelabel = ax.text(0.8*maxx, 0.8*maxy, maxz, f't={t[frame]:.1f}', fontsize=16, color='w', weight='bold')

ani = animation.FuncAnimation(fig, update, frames=len(t), interval=1, blit=False)

plt.show()
