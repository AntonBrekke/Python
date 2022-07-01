# Exercise E.49 Langtangen
import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *

class PredatorPrey:
    def __init__(self,r,m,a,b):
        self.r = r; self.m = m
        self.a = a; self.b = b

    def __call__(self, u, t):
        r = self.r; m = self.m
        a = self.a; b = self.b
        x, y = u

        dx = r*x - a*x*y
        dy = -m*y + b*x*y
        return [dx, dy]


problem = PredatorPrey(r = 1, m = 1, a = 0.3, b = 0.2)
solver = ForwardEuler(problem)
solver.set_initial_condition([1,1])

time = np.linspace(0,20,1001)

u, t = solver.solve(time)

plt.plot(t,u)
plt.legend(['Prey', 'Predator'])
plt.show()
