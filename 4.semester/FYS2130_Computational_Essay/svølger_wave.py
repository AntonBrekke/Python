import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import collections  as mc
from matplotlib.colors import ListedColormap

L = 0.65    # m
T = 70.3    # N
mu = 0.0034    # kg / m
lmbda = 0.06    # m
f = 1 / (2*L) * np.sqrt(T / mu)
f = 5

k = 2*np.pi / lmbda    # 1 / m, x = L =>
omega = 2*np.pi*f
A = 0.01

"""
Stående bølger har f(x,t) = f1(x,t) + f1(x,-t) dvs.
f1(x,t) = A*sin(k*x - w*t)
f2(x,t) = A*sin(k*x + w*t)
f(x,t) = f1(x,t) + f2(x,t)

kan skrives om som
f(x,t) = A*sin(kx)*cos(w*t)
"""

# Kan bruke f2(x,t) = f1(x, -t) men definerer f2 for ordens skyld
def h(x, t):
    return A * np.sin(k*x) * np.cos(omega*t)


x = np.linspace(0, L, 1500)
t = np.linspace(0, 10, 2000)

fig = plt.figure(facecolor='k')
ax = fig.add_subplot(facecolor=[0.12, 0.12, 0.12])
ax.spines['bottom'].set_color('w')      # Setter aksen hvit
ax.spines['left'].set_color('w')
ax.tick_params(axis='x', colors='w')    # Setter ticks hvit
ax.tick_params(axis='y', colors='w')

# Henter cmap som skal plotte linje i ulike farger
get_cmap = plt.get_cmap('plasma')
dat0 = h(x, t[0])
colors = np.array(get_cmap(abs(dat0) / np.max(abs(dat0))))      # Farger etter høyde y rundt nullpunktet, normaliserer maximum
# Tar get_cmap og speiler det om bunn
cbarcolors = np.array(get_cmap(np.concatenate((np.linspace(1, 0, 300), np.linspace(0, 1, 300)))))
lines = np.zeros([len(dat0), 2, 2])
for n in range(len(lines)-1):
    lines[n, 0, :] = [x[n], dat0[n]]
    lines[n, 1, :] = [x[n+1], dat0[n+1]]

lc = mc.LineCollection(lines, colors=colors, linewidths=2)
# Setter fargen på cbar
sm = plt.cm.ScalarMappable(cmap=ListedColormap(cbarcolors))
sm.set_clim(vmin=np.min(dat0), vmax=np.max(dat0))
cbar = fig.colorbar(sm, ax=ax, ticks=np.linspace(np.min(dat0), np.max(dat0), 7))
cbar.ax.set_yticklabels([f'{i:.1f}' for i in np.linspace(np.min(dat0), np.max(dat0), 7)])  # vertically oriented colorbar
cbar.ax.tick_params(colors='w')

def init():
    ax.set_xlim(np.min(x), np.max(x))
    ax.set_ylim(-2.5*A, 2.5*A)
    return ()

def update(frame):
    ax.clear()
    ax.set_xlim(np.min(x), np.max(x))
    ax.set_ylim(-2.5*A, 2.5*A)
    dat = h(x, t[frame])
    dat0 = h(x, t[0])
    colors = np.array(get_cmap(abs(dat) / np.max(abs(dat0))))      # Farger etter høyde y rundt nullpunktet, normaliserer maximum
    lines = np.zeros([len(dat), 2, 2])
    for n in range(len(lines)-1):
        lines[n, 0, :] = [x[n], dat[n]]
        lines[n, 1, :] = [x[n+1], dat[n+1]]

    lc = mc.LineCollection(lines, colors=colors, linewidths=2)
    ax.add_collection(lc)
    return lc,

ani = FuncAnimation(fig, update, init_func=init, frames=len(t), interval=10, blit=True)
plt.show()
