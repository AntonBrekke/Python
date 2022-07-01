import numpy as np
import matplotlib.pyplot as plt

class ODESolver:
    def __init__(self, f):
        self.f = f

    def set_initial_condition(self, U0):
        self.U0 = U0

    def solve(self, timepoints):
        N = timepoints.size
        self.u = np.zeros(N)
        self.t = timepoints
        self.u[0] = self.U0
        for n in range(N-1):
            dt = self.t[n+1] - self.t[n]
            self.u[n+1] = self.advance()
        return self.u, self.t

    def plot(self):
        plt.plot(self.t, self.u)
        plt.show()

class ForwardEuler(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[k+1] - t[k]
        unew = u[n] + dt*f(u[n], t[n])
        return unew


class MidpointEuler(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[k+1] - t[k]
        K1 = dt/2 * f(u[n], t[n])
        K2 = dt/2
        unew = u[n] + dt*f(u[n] + K1, t[n] + K2)
        return unew



f = lambda u, t: 5*u*t

problem = ForwardEuler(f)
problem.set_initial_condition(1)
print(problem.U0)
timepoints = np.linspace(0,1,100)
u, t = problem.solve(timepoints)
plt.plot(t, u)
plt.show()
