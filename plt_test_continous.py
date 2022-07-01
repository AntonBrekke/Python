import numpy as np
import matplotlib.pyplot as plt


f1 = lambda x: x**2
f2 = lambda x: -x**2 + 8*x - 8
int_point = [2, 5]
t1 = np.linspace(-1, int_point[0], 500)
t2 = np.linspace(int_point[0], int_point[1], 500)

plt.plot(t1, f1(t1))
plt.plot(t2, f2(t2))

plt.show()
