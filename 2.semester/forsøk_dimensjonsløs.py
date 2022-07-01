import numpy as np
import matplotlib.pyplot as plt

"""
Kast dimensjonsløst skalert med
t* = t / t_m med t_m fra v_y(t) = 0
h* = h / h_m med h_m = h(t_m)
x* = x / x_m med x_m = x(t_m)
"""

t = np.linspace(0, 2, 1000)    # Merk: 2 fordi t* = t / t_m, der t_m er tiden halveis i kastet

h = 2*t - t**2
x = 4*t

plt.plot(x, h)
plt.show()

"""
Kast dimensjonsløst skalert med
t* = t / t_m med t_m fra v_y(t) = 0
h* = h / h_m med h_m = h(t_m)
x* = x / x_m med x_m = x(t -> y=0)
"""

t = np.linspace(0, 2, 1000)    # Merk: 2 fordi t* = t / t_m, der t_m er tiden halveis i kastet

h = 2*t - t**2
x = t/2

plt.plot(x, h)
plt.show()
