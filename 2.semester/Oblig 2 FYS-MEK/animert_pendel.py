import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


k = float(input('Bestem fjærkonstant:'))
g = 9.81
m = 0.1
L_0 = 1
theta = np.pi/6


i = np.array([1,0])
j = np.array([0,1])

T = 10
N = 1000

t = np.linspace(0, T, N+1)
a = np.zeros([N+1, 2])
v = np.zeros([N+1, 2])
r = np.zeros([N+1, 2])
re = np.zeros([N+1, 2])

v0 =[0,0]; r0 = L_0*np.sin(theta)*i - L_0*np.cos(theta)*j
r[0,:] = r0
R = np.linalg.norm(r[0])
re[0] = r[0,:] / R
a[0,:] = -g*j - k*(np.linalg.norm(r0) - L_0)*re[0]/m
v[0,:] = v0

for n in range(N):
    dt = t[n+1] - t[n]
    v[n+1,:] = v[n,:] + dt*a[n,:]
    r[n+1,:] = r[n,:] + dt*v[n+1,:]
    R = np.linalg.norm(r[n+1,:])
    re[n+1,:] = r[n+1,:] / R
    a[n+1,:] = -g*j - k*(R - L_0)*re[n+1]/m
"""
class matplotlib.animation.FuncAnimation(fig, func,
    frames=None, init_func=None, fargs=None, save_count=None, cache_frame_data=True, **kwargs)
"""
fig, ax = plt.subplots()
plt.suptitle("Pendulum", fontweight='bold')
xdata, ydata = [], []
ln, = plt.plot([], [], 'royalblue')

ln_ball, = plt.plot([], [], 'ro', markersize='20')

xdata_line, ydata_line = [], []
line, = plt.plot([], [], 'k', label=f'k={k}N/m')

def init():
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1.2, 0)
    return ln,

def update(frame):
    xdata.append(r[frame][0])
    ydata.append(r[frame][1])
    ln.set_data(xdata[-50:], ydata[-50:])
    ln_ball.set_data(xdata[-1:], ydata[-1:])
    line.set_data([0, r[frame][0]], [0, r[frame][1]])
    return ln, line, ln_ball,

ani = FuncAnimation(fig, update, frames=[i for i in range(0,N+1)], interval=20, init_func=init, blit=True)

writer = PillowWriter(fps=25)
plt.legend()
# ani.save("pendulum.gif", writer=writer)
plt.show()
