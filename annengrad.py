import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**2

x = np.linspace(-5,5,100)
y = np.zeros(100)

y = f(x)

plt.plot(x,y, 'r', label = "f(x) = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis([-6,6,0,26])
plt.show()
