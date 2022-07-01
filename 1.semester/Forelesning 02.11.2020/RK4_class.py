# Exercise E22 Langtangen

"""Class(es) implementing the Forward Euler method for scalar ODEs."""

import numpy as np

class RungeKutta4(object):
    """
    Class for solving an ODE,
      du/dt = f(u, t)
    by the RungeKutta4 solver.
    Class attributes:
    t: array of time values
    u: array of solution values (at time points t)
    k: step number of the most recently computed solution
    f: callable object implementing f(u, t)
    dt: time step (assumed constant)
    """
    def __init__(self, f):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))
        self.f = f

    def set_initial_condition(self, U0):
        self.U0 = float(U0)

    def solve(self, time_points):
        """Compute u for t values in time_points list."""
        self.t = np.asarray(time_points)
        self.u = np.zeros(len(time_points))
        # Assume self.t[0] corresponds to self.U0
        self.u[0] = self.U0

        for k in range(len(self.t)-1):
            self.k = k
            self.u[k+1] = self.advance()
        return self.u, self.t

    def advance(self):
        """Advance the solution one time step."""
        # Load attributes into local variables to
        # obtain a formula that is as close as possible
        # to the mathematical notation.
        u, f, k, t = self.u, self.f, self.k, self.t

        dt = t[k+1] - t[k]
        K1 = dt * f(u[k], t[k])
        K2 = dt * f(u[k] + 0.5*K1, t[k] + dt)
        K3 = dt * f(u[k] + 0.5*K2, t[k] + dt)
        K4 = dt* f(u[k] + K3, t[k])
        u_new = u[k] + 1/6*(K1 + 2*K2 + 2*K3 + K4)
        return u_new


def test_RungeKutta4():
    """Use knowledge of an exact numerical solution for testing."""
    u_exact = lambda t: 0.2*t + 3
    f = lambda u, t: 0.2 + (u - e_exact(t))**4

    solver = RungeKutta4(f)

    # Solve for first time interval [0, 1.2]
    solver.set_initial_condition(u_exact(0))
    u1, t1 = solver.solve([0, 0.4, 1, 1.2])

    # Continue with a new time interval [1.2, 1.5]
    solver.set_initial_condition(u1[-1])
    u2, t2 = solver.solve([1.2, 1.4, 1.5])

    # Append u2 to u1 and t2 to t1
    u = np.concatenate((u1, u2))
    t = np.concatenate((t1, t2))

    u_e = u_exact(t)
    error = np.abs(u_e - u).max()
    assert error < 1E-14, '|exact - u| = %g != 0' % error
