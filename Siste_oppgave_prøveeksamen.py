from ODESolver import *

class Heun3(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        K1 = dt * f(u[k], t[k])
        K2 = dt * f(u[k] + K1/3, t[k] + dt/3)
        K3 = dt * f(u[k] + 2*K2/3, t[k] + 2*dt/3)
        u_new = u[k] + K1/4 + 3*K3/4
        return u_new

def SEIS(S0, E0, p, q, r, T):
    def f(u, t):
        S, E, I = u[0], u[1], u[2]
        dS = -p(t)*S*I + r*I
        dE = p(t)*S*I - q*E
        dI = q*E - r*I
        return [dS, dE, dI]

    solver = Heun3(f)           # Fra tidligere oppgave
    solver.set_initial_condition([S0, E0, 0])
    import numpy as np
    time = np.linspace(0, T, 10*T + 1)
    u, t = solver.solve(time)
    return t, u[:,0], u[:,1], u[:,2]

p = lambda t: 0.0233
S0, E0, q, r, T = 4.0, 0.2, 0.1, 0.1, 100
t, S, E, I = SEIS(S0, E0, p, q, r, T)

import matplotlib.pyplot as plt
plt.plot(t, S)
plt.plot(t, E)
plt.plot(t, I)
plt.legend(['S(t)', 'E(t)', 'I(t)'])
plt.show()
