# Plotting, Exercise 5.11 Primer
import numpy as np
import matplotlib.pyplot as plt
import sys

v0_list = sys.argv[1:]
g = 9.81

max_t = 0
max_y = 0

n = int(input("Input number of points:"))
for v0 in v0_list:
    v0 = float(v0)

    t_stop = 2*v0/g
    if t_stop > max_t:
        max_t = t_stop

    t = np.linspace(0, t_stop, n+1)
    y = v0*t - 0.5*g*t**2
    if np.max(y) > max_y:
        max_y = np.max(y)

    plt.plot(t, y, label = f'v0 = {v0}')



plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.title('Ball in vertical motion')
plt.savefig('ball_plot3.pdf')
plt.legend()
plt.axis([0, max_t, 0, max_y])

plt.show()
