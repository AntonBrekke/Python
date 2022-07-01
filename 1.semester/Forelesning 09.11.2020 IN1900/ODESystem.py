import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *

class RadioactiveDecay:
    def __init__(self, tau_a, tau_b):
        self.tau_a = tau_a
        self.tau_b = tau_b

    def __call__(self, u, t):
        tau_a = self.tau_a
        tau_b = self.tau_b

        du_a = u[1]/tau_b - u[0]/tau_a
        du_b = u[0]/tau_a - u[1]/tau_b
        return [du_a, du_b]

    def check_convergence(self,u):
        tol = 1e-6
        return abs(u[0]/u[1] - self.tau_a/self.tau_b) < tol


problem = RadioactiveDecay(tau_a=8, tau_b=40)
solver = RungeKutta4(problem)
solver.set_initial_condition([1,1])

T_stop = 100
dt = 1/6
Steps = int(T_stop/dt)

time = np.linspace(0, T_stop, Steps+1)

u, t = solver.solve(time)

plt.plot(t,u)
plt.show()

print(problem.check_convergence(u[-1,:]))
