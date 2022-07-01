# Exercise E.3 oppgaveheftet
import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ForwardEuler

# a - d) likt som E.1 med bruk av ODESolver

f = lambda u, t: u/5        # Diff, u' = u/5
U0 = 0.1
T_0 = 0
T = 20
N = 4
time_points = np.linspace(T_0, T, N+1)    # t-array med dt = 5, likt som i E.1

method = ForwardEuler(f)
method.set_initial_condition(U0)
u, t = method.solve(time_points)
plt.plot(t,u, label = 'ForwardEuler-method')

# Analytisk:
def exact(t):
    return 0.1*np.exp(t/5)

t = np.linspace(0, T, 1000)
plt.plot(t, exact(t), 'r', label='Analytical')

plt.legend()
plt.show()

# f)
# Simulering av approksimasjon:
N_list = *range(2,202,5),       # Former tuppel med verdier fra range()
for N in N_list:
    time_points = np.linspace(T_0, T, N+1)    # t-array med dt = 5, likt som i E.1

    method = ForwardEuler(f)
    method.set_initial_condition(U0)
    u, t = method.solve(time_points)
    plt.plot(t,u, label = 'ForwardEuler-method')

    t = np.linspace(0, T, 1000)
    plt.plot(t, exact(t), 'r', label='Analytical')

    plt.legend()
    plt.draw()
    plt.pause(0.1)
    plt.clf()

# Kjøretest fra terminal:
"""
PS C:\Python\Oblig uke 46 IN1900> python simple_ODE_class_ODESolver.py
PS C:\Python\Oblig uke 46 IN1900>
"""
