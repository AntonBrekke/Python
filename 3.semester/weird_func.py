import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.linspace(0, 100, 11)
f = x % n
g = x // n

plt.plot(x, f, 'r', marker='o', label='%')
plt.plot(x, g, 'b', marker='o', label='//')
plt.legend()
plt.show()

plt.plot(f, g, 'g', marker='o')
plt.show()
