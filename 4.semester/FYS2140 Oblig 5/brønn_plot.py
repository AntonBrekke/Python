import numpy as np
import matplotlib.pyplot as plt

a = 1
def f(x):
    f_arr = np.zeros(len(x))
    f_arr[np.logical_and(x > 0, x < a/2)] = 2 / a
    return f_arr

x = np.linspace(-0.2, a + 0.2, 1000)

plt.plot([0, 0], [0, 3], 'k')
plt.plot([a, a], [0, 3], 'k')
plt.plot(x, f(x), 'r', label=r'$|\Psi(x,0)|^2$')
fill_array = np.logical_or(x < 0, x > a)
plt.fill_between(x, 3*np.ones(len(x)), where=fill_array, alpha=0.2, color='k')
plt.xticks([0, a/2, a], ['0', 'a/2', 'a'])

plt.legend(prop={'size': 16})
plt.show()
