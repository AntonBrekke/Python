import numpy as np
import matplotlib.pyplot as plt

class ODESolver:
    def __init__(self, f, T, N):
        self.f = f
        self.T = T
        self.N = N
        self.u = np.zeros(N+1)
        self.t = np.zeros(N+1)

    def set_initial_condition(self, U0):
        self.U0 = U0

    def solve(self):
        f = self.f
        dt = self.T/self.N
        self.u[0] = self.U0
        for n in range(self.N):
            self.t[n+1] = self.t[n] + dt
            self.u[n+1] = self.u[n] + dt*f(self.u[n], self.t[n])
        return self.u, self.t

    def plot(self):
        plt.plot(t, u)
        plt.show()


f = lambda u, t: -1/3*u*t

def exact(t):
    return np.exp(-1/6*t**2)

import sys
try:
    N = int(sys.argv[1])
except IndexError:
    print("\nYou need to put N solving steps for ODE as argument in command line\n")

problem = ODESolver(f, 1, N)
problem.set_initial_condition(1)
timepoints = np.linspace(0, 1, 1000)
plt.plot(timepoints, exact(timepoints))
problem.solve()
# problem.plot()

print('\n', "Local Error: \t \t Global Error", '\n')
for n in range(10):
    print(f'{abs(exact(problem.t[n]) - problem.u[n])} \t {abs(exact(problem.t[n]) - problem.u[n])*N}')
