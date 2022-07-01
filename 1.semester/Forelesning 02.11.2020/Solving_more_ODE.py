
import numpy as np

class ODESolver:
    def __init__(self, f):
        self.f = f

    def set_initial_condition(self, U0):
        self.U0 = U0

    def solve(self, timepoints):
        n = time_points.size
        self.t = time_points
        self.u = np.zeros(n)
        self.u[0] = self.U0
        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
        return self.u, self.t
