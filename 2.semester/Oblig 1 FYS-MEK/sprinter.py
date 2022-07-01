# Anton Andreas Brekke
# antonabr@uio.no
# Oppgave a - g
import numpy as np
import matplotlib.pyplot as plt

class ForwardEuler:
    def __init__(self, f, N, T):
        self.f = f
        self.N = N
        self.a = np.zeros(N+1)
        self.v = np.zeros(N+1)
        self.x = np.zeros(N+1)
        self.t = np.linspace(0, T, N+1)

    def set_initial_condition(self, v0, x0):
        self.x0 = x0
        self.v0 = v0

    def solve(self):
        t = self.t; a = self.a; v = self.v; x = self.x
        a[0] = self.f(self.x0, self.v0, self.t[0])
        v[0] = self.v0
        x[0] = self.x0
        for n in range(self.N):
            dt = t[n+1] - t[n]
            v[n+1] = v[n] + dt*self.f(x[n], v[n], t[n])
            x[n+1] = x[n] + dt*v[n+1]
            a[n+1] = self.f(x[n+1], v[n+1], t[n+1])
        return self.a, self.v, self.x, self.t

class acceleration:
    def __init__(self, p, C_d, A_0, w, m):
        self.p = p; self.C_d = C_d; self.A_0 = A_0
        self.w = w; self.m = m

    def __call__(self, x, v, t):
        a = (800 - self.p*self.C_d*self.A_0*(v-self.w)**2) / (2*self.m)
        return a

a = acceleration(p=1.293, C_d=1.2, A_0=0.45, w=0, m=80)

method = ForwardEuler(a, 1000, 10)
method.set_initial_condition(v0=0, x0=0)
a, v, x, t = method.solve()

plt.subplot(311)
plt.plot(t, a, 'r', label=r'$a\;[m/s^2]$')
plt.legend()

plt.subplot(312)
plt.plot(t, v, 'b', label=r'$v\;[m/s]$')
plt.legend()

plt.subplot(313)
plt.plot(t, x, 'g', label=r'$s\;[m]$')
plt.xlabel(r'$t\;[s]$')
plt.legend()
# plt.savefig('sprinter.png')
plt.suptitle('Modellering 100meters-løp')
plt.show()

for n in range(len(t)):
    if x[n] > 100:
        print(f'\nt\tx\n{t[n-1]}\t{x[n-1]}\n {t[n]}\t{x[n]}\n')
        break

print(f'Terminalfart: {v[-1]}')