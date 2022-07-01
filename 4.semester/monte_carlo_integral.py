import numpy as np
import matplotlib.pyplot as plt
from numba import njit
import time

a = 0
b = np.pi
N = 25000
M = 100000

t0 = time.time()

@njit(cache=True)
def monte_carlo(func):
    mc = np.zeros(M)
    for i in range(M):
        randx = np.random.uniform(a, b, N)
        sum = np.sum(func(randx))
        integral = (b-a) / N * sum          # Uniformt så er sannsnylighet = areal_graf / areal_boks
        mc[i] = integral
    return mc

@njit
def f(x):
    return np.sin(x)

mc = monte_carlo(f)

t1 = time.time()
print(f'Computation time {t1 - t0}s')

# Lager en figur som skal se kulere ut
fig = plt.figure(facecolor='k')
ax = fig.add_subplot(facecolor='k')
ax.spines['bottom'].set_color('w')      # Setter aksen hvit
ax.spines['left'].set_color('w')
ax.tick_params(axis='x', colors='w')    # Setter ticks hvit
ax.tick_params(axis='y', colors='w')

# Henter fargekart for histogram
get_cmap = plt.get_cmap('jet')
n, bins, patches = ax.hist(mc, bins=75)
cmap = np.array(get_cmap(n / np.max(n)))    # Må normalisere data

for color, p in zip(cmap, patches):
    plt.setp(p, 'facecolor', color)

plt.show()
