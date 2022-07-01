import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, np.pi, 100)

g = 9.81
v0 = 5
t = np.linspace(0, 2*v0/g, 100)
v0y = v0*np.sin(theta)

def h(t):
    return v0y*t - 0.5*g*t**2

plt.axis([t[0], t[-1], -100.0, 20])
plt.xlabel('time[s]')
plt.ylabel('height[m]')

for t in theta:
    plt.plot(t, h(t))
    plt.set_ydata(h(t))   #update plot and data redraw
    plt.draw()
    plt.pause(0.01)
