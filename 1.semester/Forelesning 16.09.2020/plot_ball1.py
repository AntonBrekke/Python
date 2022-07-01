# Plotting, Exercise 5.9 Primer
import numpy as np
import matplotlib.pyplot as plt

v0 = 10
g = 9.81

t_stop = 2*v0/g
n = int(input("Input number of points:"))

t = np.linspace(0, t_stop, n)

y = v0*t - 0.5*g*t**2

plt.plot(t, y)
plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.title('Ball in vertical motion')
plt.savefig('ball_plot.pdf')

plt.show()
