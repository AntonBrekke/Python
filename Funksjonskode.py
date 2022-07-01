import numpy as np
import matplotlib.pyplot as plt

def plot_function(f, start, stop):
    x = np.linspace(start, stop, 101)
    plt.plot(x, f(x))
    plt.show()

f = lambda x: np.sin(x)
plot_function(f, 0, 2*np.pi)

plot_function(np.sin, 0, 2*np.pi)

def g(x):
    return np.sin(x)
plot_function(g, 0, 2*np.pi)
