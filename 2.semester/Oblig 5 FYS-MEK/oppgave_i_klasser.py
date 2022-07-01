import numpy as np
import matplotlib.pyplot as plt

class Ball:
    def __init__(self, R, k, mu, m, g, dt, T):
        self.R = R; self.k = k; self.mu = mu;
        self.m = m; self.g = g; self.dt = dt

        self.t = np.arange(0, T+dt, dt)
        self.N = len(self.t)
        self.a = np.zeros([self.N, 2])
        self.v = np.zeros([self.N, 2])
        self.r = np.zeros([self.N, 2])
        self.alph = np.zeros(self.N)
        self.w = np.zeros(self.N)

        self.i = np.array([1,0])
        self.j = np.array([0,1])

    def acceleration(self, r, v, t):
        x = r[0]; y = r[1]
        m = self.m; k = self.k; mu = self.mu
        g = self.g; R = self.R
        if y > R:
            ax = 0
            ay = -g / m
        else:
            f = -mu*k*(R-y)**(3/2)
            if v[0] < 0:
                f = -f
            ax = f / m
            ay = (k*(R-y)**(3/2) - m*g) / m
        return ax*self.i + ay*self.j

    def alpha(self, y, v, t):
        m = self.m; k = self.k; mu = self.mu
        g = self.g; R = self.R
        if y < R:
            az = -3*mu*k*(R-y)**(3/2) / (2*m*R)
            return az
        else:
            return 0

    def set_initial_conditions(self, v0x, v0y, h):
        self.v[0,:] = v0x*self.i + v0y*self.j
        self.r[0,:] = h*self.j
        self.a[0,:] = self.acceleration(self.r[0,:], self.v[0,:], 0)
        self.w[0] = 0
        self.alph[0] = self.alpha(h, self.w[0], 0)

    def solve(self):
        N = self.N; a = self.a; v = self.v
        r = self.r; w = self.w; alph = self.alph
        dt = self.dt; t = self.t
        for n in range(N-1):
            v[n+1,:] = v[n,:] + dt*a[n,:]
            r[n+1,:] = r[n,:] + dt*v[n+1,:]
            a[n+1:,] = self.acceleration(r[n+1,:], v[n+1,:], t[n+1])

            w[n+1] = w[n] + dt*alph[n]
            alph[n+1] = self.alpha(r[n+1, 1], w[n+1], t[n+1])
        return v, r, w, t

ball = Ball(R=0.15, k=10000, mu=0.3, m=1, g=9.81, dt=0.001, T=1)
ball.set_initial_conditions(v0x=3, v0y=0, h=1)
v, r, w, t = ball.solve()

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
ax3.legend(['vx', 'vy'], loc=(0.5,0.05), prop={'size':6})
ax4.plot(t, w); ax4.set_xlabel(r'$t\,[s]$'); ax4.set_ylabel(r'$\omega\,[\frac{rad}{s}]$', rotation=0)
fig.tight_layout()
plt.show()
