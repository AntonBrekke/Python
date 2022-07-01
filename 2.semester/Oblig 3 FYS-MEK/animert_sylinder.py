import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

class Sylinder:
    def __init__(self, h, k, l_0, m, mu, T, N):
        self.h = h
        self.k = k
        self.l_0 = l_0
        self.m = m
        self.mu = mu

        self.N = N      # Antall tidssteg

        self.a = np.zeros([N+1, 2])
        self.v = np.zeros([N+1, 2])
        self.r = np.zeros([N+1, 2])
        self.t = np.linspace(0, T, N+1)

        self.i = np.array([1,0])        # Enhetsvektor x-akse
        self.j = np.array([0,1])        # Enhetsvektor y-akse

    def set_initial_condition(self, v0, x0): # Setter initialbetingelser
        self.r0 = x0*self.i + self.h*self.j
        self.v0 = v0
        l0 = np.linalg.norm(self.r0)
        re0 = self.r0 / l0
        self.a0 = -self.k/self.m * (l0 - self.l_0)*re0 + self.k/self.m*self.h*(1 - self.l_0/l0)*self.j

    def solve(self):    # Løser differensiallikninger med E-C
        t = self.t; a = self.a; v = self.v; r = self.r
        a[0] = self.a0
        v[0] = self.v0
        r[0] = self.r0
        self.r[:,1] = self.h
        for n in range(self.N):
            dt = t[n+1] - t[n]
            v[n+1,:] = v[n,:] + dt*a[n,:]
            v_len = np.linalg.norm(v[n+1,:])
            v_e = v[n+1,:] / v_len
            r[n+1,:] = r[n,:] + dt*v[n+1,:]
            l = np.linalg.norm(r[n+1,:])
            re = r[n+1,:] / l
            G = -self.m*9.81 *self.j
            F = -self.k * (l - self.l_0)*re
            N = self.k*self.h*(1 - self.l_0/l)*self.j - G
            if v_len > 1e-8:
                fd = -self.mu * np.linalg.norm(N) * v_e
            else:
                fd = 0
            a[n+1,:] = (F + N + G + fd)/self.m
        return self.a, self.v, self.r, self.t

k = float(input('Bestem fjærkonstant:'))
method = Sylinder(h=0.3, k=500, l_0=0.5, m=5, mu=0.05, T=10, N=1000)
method.set_initial_condition(v0=[0,0], x0=0.75)
a, v, r, t = method.solve()
"""
class matplotlib.animation.FuncAnimation(fig, func,
    frames=None, init_func=None, fargs=None, save_count=None, cache_frame_data=True, **kwargs)
"""
fig, ax = plt.subplots()
plt.suptitle("Sylinder på horisontal stang", fontweight='bold')
xdata, ydata = [], []
xdata_s1, xdata_s2 = [], []
ln, = plt.plot([], [], 'royalblue')

ln_square, = plt.plot([], [], 'rs', markersize='20')
ln_square_side1, = plt.plot([], [], 'rs', markersize='20')
ln_square_side2, = plt.plot([], [], 'rs', markersize='20')

line, = plt.plot([], [], 'k', label=f'k={k}N/m')

if np.min(r[:,0]) > 0:
    xmin = -0.1
else:
    xmin = np.min(r[:,0])*1.5

def init():
    ax.set_xlim(xmin, np.max(r[:,0])*1.5)
    ax.set_ylim(-0.1, np.max(r[:,1])*1.5)
    return ln, # Kan være vilkårlig av ln, line, ln_ball. Kan ha bare ln, kan ha alle tre, kan ha to av dem etc. men må ikke ha akkurat den

def update(frame):
    xdata.append(r[frame][0])
    ydata.append(r[frame][1])

    xdata_s1.append(r[frame][0] - 0.06)
    xdata_s2.append(r[frame][0] + 0.06)
    ln.set_data(xdata[:], ydata[:])
    ln_square.set_data(xdata[-1:], ydata[-1:])
    ln_square_side1.set_data(xdata_s1[-1:], ydata[-1:])
    ln_square_side2.set_data(xdata_s2[-1:], ydata[-1:])
    line.set_data([0, r[frame][0]], [0, r[frame][1]-0.022])
    return ln, line, ln_square, ln_square_side1, ln_square_side2,       # Må returnere alle biter som skal animeres

ani = FuncAnimation(fig, update, frames=[i for i in range(0,method.N+1)], interval=20, init_func=init, blit=True)

writer = PillowWriter(fps=25)
plt.legend()
# ani.save("pendulum_klasse.gif", writer=writer)
plt.show()
