import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


N = 6000
T = 60
t = np.linspace(0, T, N+1)
m = 1
Q = 1

i = np.array([1,0])
j = np.array([0,1])

def F_field(r, v):
    x = r[0]; y=r[1]
    F_x = y*np.sin(np.log(abs(x))) / Q
    F_y = x*np.cos(y) / Q
    if F_x > 10 and F_y > 10:
        return 0
    else:
        return (F_x*i + F_y*j)

x_start = -100; y_start = -0
vx_start = 10.1; vy_start = 0

a = np.zeros([N+1, 2])
v = np.zeros([N+1, 2])
r = np.zeros([N+1, 2])

r[0,:] = x_start*i + y_start*j
v[0,:] = vx_start*i + vy_start*j
a[0,:] = F_field(r[0,:], v[0,:]) / m

for n in range(N):
    dt = t[n+1] - t[n]
    v[n+1,:] = v[n,:] + dt*a[n,:]
    r[n+1,:] = r[n,:] + dt*v[n+1]
    a[n+1,:] = F_field(r[n+1,:], v[n+1,:]) / m

"""
class matplotlib.animation.FuncAnimation(fig, func,
    frames=None, init_func=None, fargs=None, save_count=None, cache_frame_data=True, **kwargs)
"""
"""
Animerer atomets bevegelse langs x-aksen over tid
"""
def animation():
    I = np.linspace(-100, 100, 50)
    x, y = np.meshgrid(I, I, indexing='xy')
    F_x = y*np.sin(np.log(abs(x)))*m
    F_y = x*np.cos(y)*m
    fig, ax = plt.subplots()
    ax.quiver(x[::2, ::2], y[::2, ::2], (F_x / Q)[::2, ::2], (F_y / Q)[::2, ::2])
    plt.suptitle("Partikkel i kraftfelt", fontweight='bold')
    plt.xlabel(r'$x\;[m]$')
    plt.ylabel(r'$y\;[m]$')
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'royalblue')

    ln_atom, = plt.plot([], [], 'ro', label='Partikkel', markersize='8')

    def init():
        ax.set_xlim(-100, 100)
        ax.set_ylim(-100, 100)
        return ln, # Kan være vilkårlig av ln, line, ln_ball. Kan ha bare ln, kan ha alle tre, kan ha to av dem etc. men må ikke ha akkurat den

    def update(frame):
        xdata.append(r[frame][0])
        ydata.append(r[frame][1])
        ln.set_data(xdata[-450:], ydata[-450:])
        ln_atom.set_data(xdata[-1], ydata[-1])
        return ln, ln_atom,       # Må returnere alle biter som skal animeres

    speed = 3
    ani = FuncAnimation(fig, update, frames=[i for i in range(0, N+1, speed)], interval=20, init_func=init, blit=True)

    writer = PillowWriter(fps=25)
    plt.legend()
    # ani.save("partikkel_kraftfelt.gif", writer=writer)
    plt.show()

animation()
