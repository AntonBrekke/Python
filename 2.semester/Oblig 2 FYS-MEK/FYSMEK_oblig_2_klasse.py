import numpy as np
import matplotlib.pyplot as plt

class Pendulum:
    def __init__(self, g, k, L_0, r_start, m, T, N):
        self.g = g
        self.k = k
        self.L_0 = L_0
        self.r_start = r_start
        self.m = m

        self.N = N      # Antall tidssteg

        self.a = np.zeros([N+1, 2])
        self.v = np.zeros([N+1, 2])
        self.r = np.zeros([N+1, 2])
        self.t = np.linspace(0, T, N+1)

        self.i = np.array([1,0])        # Enhetsvektor x-akse
        self.j = np.array([0,1])        # Enhetsvektor y-akse

    def set_initial_condition(self, v0, theta): # Setter initialbetingelser
        self.r0 = self.r_start*np.sin(theta)*self.i - self.r_start*np.cos(theta)*self.j
        self.v0 = v0
        R0 = np.linalg.norm(self.r0)
        re0 = self.r0 / R0
        self.a0 = -self.g*self.j - self.k*(R0 - self.L_0)*re0/self.m

    def solve(self):    # Løser differensiallikninger med E-C
        t = self.t; a = self.a; v = self.v; r = self.r
        a[0] = self.a0
        v[0] = self.v0
        r[0] = self.r0
        for n in range(self.N):
            dt = t[n+1] - t[n]
            v[n+1,:] = v[n,:] + dt*a[n,:]
            r[n+1,:] = r[n,:] + dt*v[n+1,:]
            R = np.linalg.norm(r[n+1,:])
            re = r[n+1,:] / R
            a[n+1,:] = -self.g*self.j - self.k*(R - self.L_0)*re/self.m
        return self.a, self.v, self.r, self.t

method = Pendulum(g=9.81, k=20, L_0=1, r_start=1, m=0.1, T=10, N=1000)
method.set_initial_condition(v0=[0,0], theta = np.pi/6)
a, v, r, t = method.solve()

fig, ax = plt.subplots(3,1)
ax[0].plot(t, a); ax[0].legend([r'$a_x$', r'$a_y$'], loc="lower right")
ax[0].set_xlim([0, 10])
ax[1].plot(t, v); ax[1].legend([r'$v_x$', r'$v_y$'], loc="lower right")
ax[1].set_xlim(0, 10)
ax[2].plot(r[:,0], r[:,1]); ax[2].legend([r'$r$'], loc="lower right")
# plt.savefig('pendel_plot')
plt.show()
