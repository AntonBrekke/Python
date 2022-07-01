import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

def cls():
    os.system('cls')

class EulerCromer:
    def __init__(self, U0, x0, alpha, m, T, N):
        self.U0 = U0
        self.x0 = x0
        self.alpha = alpha
        self.m = m
        self.T = T

        self.N = N      # Antall tidssteg

        self.a = np.zeros(N+1)
        self.v = np.zeros(N+1)
        self.x = np.zeros(N+1)
        self.t = np.linspace(0, T, N+1)

    def acceleration(self, x, v):
        U0 = self.U0; alpha = self.alpha; m = self.m; x0 = self.x0
        if abs(x) < x0 and x != 0:
            return (-U0*abs(x) - alpha*v*x0*x) / (x0*x*m)
        else:
            return 0

    def set_initial_condition(self, v_0, x_0): # Setter initialbetingelser
        self.x_0 = x_0
        self.v_0 = v_0
        self.a_0 = self.acceleration(x_0, v_0)


    def solve(self):    # Løser differensiallikninger med E-C
        t = self.t; a = self.a; v = self.v; x = self.x
        a[0] = self.a_0
        v[0] = self.v_0
        x[0] = self.x_0
        for n in range(self.N):
            dt = t[n+1] - t[n]
            v[n+1] = v[n] + dt*a[n]
            x[n+1] = x[n] + dt*v[n+1]
            a[n+1] = self.acceleration(x[n+1], v[n+1])

        return a, v, x, t

method = EulerCromer(U0=150, x0=2, alpha=39.48, m=23, T=10, N=1000)
method.set_initial_condition(v_0=8.0, x_0=-5)
a, v, x, t = method.solve()
"""
class matplotlib.animation.FuncAnimation(fig, func,
    frames=None, init_func=None, fargs=None, save_count=None, cache_frame_data=True, **kwargs)
"""
"""
Animerer atomets bevegelse langs x-aksen over tid
"""
def animation():
    fig, ax = plt.subplots()
    plt.suptitle("Atom fanget i kraftfelt", fontweight='bold')
    plt.xlabel(r'$t\;[s]$')
    plt.ylabel(r'$x\;[m]$')
    xdata, tdata = [], []
    ln, = plt.plot([], [], 'royalblue')

    ln_atom, = plt.plot([], [], 'ro', label='atom', markersize='8')

    def init():
        ax.set_xlim(0, 10)
        ax.set_ylim(-5, 5)
        return ln, # Kan være vilkårlig av ln, line, ln_ball. Kan ha bare ln, kan ha alle tre, kan ha to av dem etc. men må ikke ha akkurat den

    def update(frame):
        xdata.append(x[frame])
        tdata.append(t[frame])
        ln.set_data(tdata[-450:], xdata[-450:])
        ln_atom.set_data(tdata[-1], xdata[-1])
        return ln, ln_atom,       # Må returnere alle biter som skal animeres

    ani = FuncAnimation(fig, update, frames=[i for i in range(0,method.N+1)], interval=5, init_func=init, blit=True)

    writer = PillowWriter(fps=25)
    plt.legend()
    # ani.save("atom_klasse.gif", writer=writer)
    plt.show()
