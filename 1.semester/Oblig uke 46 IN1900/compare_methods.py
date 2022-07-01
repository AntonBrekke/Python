# Exercise E.8 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *

# a)
class ExplicitMidpoint(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        dt2 = dt/2
        K1 = f(u[k], t[k])
        K2 = f(u[k] + dt2*K1, t[k] + dt2)
        unew = u[k] + dt*K2
        return unew

class Heun(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        K1 = f(u[k], t[k])
        K2 = f(u[k] + dt*K1, t[k] + dt)
        unew = u[k] + dt*(K1/2 + K2/2)
        return unew

# b)
f = lambda u,t: t*np.cos(t) - np.sin(t)     # Diff, u'(t) = t*cos(t) - sin(t)

def exact(t):           # Analytisk løsning
    return t*np.sin(t) + 2*np.cos(t)


U0 = 2      # Initialbetingelse

# Compare metoder:
MP = ExplicitMidpoint(f)
Heun = Heun(f)
RK4 = RungeKutta4(f)

MP.set_initial_condition(U0)
Heun.set_initial_condition(U0)
RK4.set_initial_condition(U0)

# Plotter ved bruk av subplots:
n_list = [20, 25, 50, 150]      # Antall løsningspunkter 
fig, axes = plt.subplots(2, 2, sharex='all', sharey = 'all')
fig.suptitle('Compare methods')
m = 0
n = 0
for i in range(len(n_list)):
    time_points = np.linspace(0, 8*np.pi, n_list[i])
    if n > 1:
        n = 0
        m += 1
    x,t = MP.solve(time_points)
    axes[m,n].plot(t,x,'r--', label = 'Euler Midpoint')
    x,t = Heun.solve(time_points)
    axes[m,n].plot(t,x,'b--', label = 'Heuns method')
    x,t = RK4.solve(time_points)
    axes[m,n].plot(t,x,'g--', label = 'RungeKutta4')
    axes[m,n].set_title(f'n = {n_list[i]}', fontsize=10)
    axes[m,n].legend(loc=3, prop={'size': 6})
    n += 1
plt.show()


# Kjøretest fra terminal:
"""
PS C:\Python\Oblig uke 46 IN1900> python compare_methods.py
PS C:\Python\Oblig uke 46 IN1900>
"""
