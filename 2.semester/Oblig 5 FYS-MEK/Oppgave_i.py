import numpy as np
import matplotlib.pyplot as plt

dt = 0.001
t = np.arange(0, 1+dt, dt)
N = len(t)
R = 0.15
h = 1
v0x = 3
k = 10000
mu = 0.3
m = 1
g = 9.81

i = np.array([1,0])
j = np.array([0,1])

def acceleration(r, v, t, n):
    x = r[0]
    y = r[1]
    if y > R:
        ax = 0
        ay = -g / m
    else:
        f = -mu*k*(R-y)**(3/2)
        if v[0] < 0:
            f = -f
        ax = f / m
        ay = (k*(R-y)**(3/2) - m*g) / m
    return ax*i + ay*j


def alpha(y, v, t):
    if y < R:
        az = -3*mu*k*(R-y)**(3/2) / (2*m*R)
        return az
    else:
        return 0

a = np.zeros([N, 2])
v = np.zeros([N, 2])
r = np.zeros([N, 2])

alph = np.zeros(N)
w = np.zeros(N)

t_n = 0
v[0,:] = v0x*i
r[0,:] = h*j
a[0,:] = acceleration(r[0,:], v[0,:], t_n, 0)

w[0] = 0
alph[0] = alpha(h, w[0], 0)

a_z = 0
for n in range(N-1):
    t_n += dt
    v[n+1,:] = v[n,:] + dt*a[n,:]
    r[n+1,:] = r[n,:] + dt*v[n+1,:]
    a[n+1:,] = acceleration(r[n+1,:], v[n+1,:], t_n, n)

    w[n+1] = w[n] + dt*alph[n]
    alph[n+1] = alpha(r[n+1, 1], w[n+1], t_n)

fig = plt.figure()
gs = fig.add_gridspec(3,2)
# Definerer plot
ax1 = fig.add_subplot(gs[0,:], title='Bevegelse av ball')
ax2 = fig.add_subplot(gs[1,:], title='Bevegelse y-retning over tid')
ax3 = fig.add_subplot(gs[2, 0], label='v_x',title='Translasjonshastighet')
ax4 = fig.add_subplot(gs[2, 1], title='Vinkelhastighet')

ax1.plot(r[:,0], r[:,1]); ax1.set_xlabel(r'$x\,[m]$'); ax1.set_ylabel(r'$y\,[m]$', rotation=0)
ax2.plot(t, r[:,1]); ax2.set_xlabel(r'$t\,[s]$'); ax2.set_ylabel(r'$y\,[m]$', rotation=0)
ax3.plot(t, v); ax3.set_xlabel(r'$t\,[s]$'); ax3.set_ylabel(r'$v\,[\frac{m}{s}]$', rotation=0)
ax3.legend(['vx', 'vy'], loc='lower right, prop={'size':6})
ax4.plot(t, w); ax4.set_xlabel(r'$t\,[s]$'); ax4.set_ylabel(r'$\omega\,[\frac{rad}{s}]$', rotation=0)
fig.tight_layout()
plt.show()
