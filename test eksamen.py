from ODESolver import *
import numpy as np
import matplotlib.pyplot as plt
"""
class Ralston(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        K1 = f(u[k], t[k])
        K2 = f(u[k] + 2/3*dt*K1, t[k] + 2/3*dt)
        unew = u[k] + dt*(1/4*K1 + 3/4*K2)
        return unew

def SIRD(S0, I0, alpha, beta, gamma, T):
    def f(u, t):
        N = S0 + I0
        S, I = u[0], u[1]
        dS = -alpha(t)*S*I/N
        dI = alpha(t)*S*I/N - beta*I - gamma*I
        dR = beta*I
        dD = gamma*I
        return dS, dI, dR, dD

    solver = Ralston(f)
    solver.set_initial_condition([S0, I0, 0, 0])
    time = np.linspace(0, T, 10*T + 1)
    u, t = solver.solve(time)
    return t, u[:,0], u[:,1], u[:,2], u[:,3]

alpha = lambda t: 1.0
S0, I0, beta, gamma, T = 370000, 30, 0.025, 0.25, 100
t, S, I, R, D = SIRD(S0, I0, alpha, beta, gamma, T)

plt.plot(t, S)
plt.plot(t, I)
plt.plot(t, R)
plt.plot(t, D)
plt.legend(['S(t)', 'I(t)', 'R(t)', 'D(t)'])
# plt.show()
"""

def find(text, arg):
    for j in range(len(text)):
        if text[j:j+len(arg)] == arg:

            return j
    return False

print(find('text', 'text'))
