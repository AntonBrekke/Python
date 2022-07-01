# Exercise E.21 Langtangen


"""Function implementing the Forward Euler method for scalar ODEs."""
import numpy as np

def RungeKutta4(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    u[0] = U0
    dt = T/n
    for k in range(n):
        t[k+1] = t[k] + dt
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k]+0.5*K1, t[k]+0.5*dt)
        K3 = dt*f(u[k]+0.5*K2, t[k]+0.5*dt)
        K4 = dt*f(u[k]+K3, t[k]+dt)
        u[k+1] = u[k] + 1/6*(K1 + 2*K2 + 2*K3 + K4)
    return u, t

# Problem: u'=u
def f(u, t):
    return u

u, t = RungeKutta4(f, U0=1, T=4, n=20)

def test_RungeKutta4():
    """Use knowledge of an exact numerical solution for testing."""
    def f(u, t):
        return 0.2 + (u - u_exact(t))**4

    def u_exact(t):
        return 0.2*t + 3

    u, t = RungeKutta4(f, U0=u_exact(0), T=3, n=5)
    u_e = u_exact(t)
    error = np.abs(u_e - u).max()
    success = error < 1E-14
    assert success, f'|exact - u| = {error} != 0'

test_RungeKutta4()
