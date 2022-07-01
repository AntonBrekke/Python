import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(0,4, 100)
y = f(x)
plt.plot(x,y)
plt.plot(-x,y)
plt.axis([-x[-1],x[-1], 0.0, 16])
plt.show()
