import numpy as np
import matplotlib.pyplot as plt

class Sylinder:
    def __init__(self, h, k, l_0, m, T, N):
        self.h = h
        self.k = k
        self.l_0 = l_0
        self.m = m

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
        self.a0 = -self.k/self.m * (l0 - self.l_0)*re0

    def solve(self):    # Løser differensiallikninger med E-C
        t = self.t; a = self.a; v = self.v; r = self.r
        a[0] = self.a0
        v[0] = self.v0
        r[0] = self.r0
        self.r[:,1] = self.h; self.a[:,1] = 0
        for n in range(self.N):
            dt = t[n+1] - t[n]
            v[n+1,0] = v[n,0] + dt*a[n,0]
            r[n+1,0] = r[n,0] + dt*v[n+1,0]
            l = np.linalg.norm(r[n+1,:])
            re = r[n+1,:] / l
            F = -self.k * (l - self.l_0)*re
            a[n+1,0] = F[0]/self.m
        return self.a, self.v, self.r, self.t

method = Sylinder(h=0.3, k=500, l_0=0.5, m=5, T=10, N=1000)
method.set_initial_condition(v0=[0,0], x0=0.6)
a, v, r, t = method.solve()

fig, ax = plt.subplots(3,1)
ax[0].plot(t, a); ax[0].legend([r'$a_x$', r'$a_y$'], loc="lower right")
ax[0].set_xlabel(r'$t\;[s]$'); ax[0].set_ylabel(r'$a\;[m/s^2]$')
ax[1].plot(t, v); ax[1].legend([r'$v_x$', r'$v_y$'], loc="lower right")
ax[1].set_xlabel(r'$t\;[s]$'); ax[1].set_ylabel(r'$v\;[m/s]$')
ax[2].plot(t, r); ax[2].legend([r'$x$', r'$y$'], loc="lower right")
ax[2].set_xlabel(r'$t\;[s]$'); ax[2].set_ylabel(r'$r\;[m]$')
fig.tight_layout()
# plt.savefig('oppgave_f.png')
plt.show()
