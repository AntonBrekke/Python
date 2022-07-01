# Exercise E.5 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ODESolver

# a)
# Implementerer midtpunkt-metoden
class ExplicitMidpoint(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        dt2 = dt/2
        K1 = f(u[k], t[k])
        K2 = f(u[k] + dt2*K1, t[k] + dt2)
        unew = u[k] + dt*K2
        return unew

f = lambda u, t: np.cos(t) - t*np.sin(t)    # Diff. u' = cos(t) - t*sin(t)
U0 = 0          # Initialbetingelse, gitt i oppgave
T_0 = 0         # Start av intervall, gitt i oppgave
T = 4*np.pi           # Slutt av intervall, gitt i oppgave
N = 20         # Antall steg, gitt i oppgave


# Analytisk:
def exact(t):
    return t*np.cos(t)

t = np.linspace(T_0, T, 1000)
plt.plot(t, exact(t), 'r--', label='Analytical', linewidth=3)


# Numerisk:
method = ExplicitMidpoint(f)
method.set_initial_condition(U0)
time_points = np.linspace(T_0, T, N+1)
u, t = method.solve(time_points)
plt.plot(t, u, 'blue', label = 'ExplicitMidtpoint')

# Plot
plt.xlabel(f'N = {N}' + r'$,\quad\Delta t \approx$' + f'{T/N}')
plt.legend()
plt.show()

# Kjøretest fra terminal:
"""
PS C:\Python\Oblig uke 46 IN1900> python Midpoint.py
PS C:\Python\Oblig uke 46 IN1900>
"""
