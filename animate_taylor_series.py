import numpy as np
import matplotlib.pyplot as plt

def animate_series(fk, M, N, xmin, ymin, xmax, ymax, n, exact):
    plt.axis([xmin, xmax, ymin, ymax])
    plt.xlabel('x')
    plt.ylabel('y')

    x = np.linspace(xmin, xmax, n)
    s = 0

    lines = plt.plot(x, fk(x, N), linewidth = 3)
    for k in range(M, N+1):
        s += fk(x, k)
        lines[0].set_ydata(s)
        plt.plot(x, exact(x),'g--')
        plt.draw()
        plt.pause(0.3)

# Example sin(x):
exact = lambda x: np.sin(x)
def fk(x,k):
    return (-1)**k * x**(2*k+1) / np.math.factorial(2*k+1)
M = 0
N = 40
xmin = 0
xmax = 13 * np.pi
ymin = -2
ymax = 2
n = 100
animate_series(fk, M, N, xmin, ymin, xmax, ymax, n, exact)
