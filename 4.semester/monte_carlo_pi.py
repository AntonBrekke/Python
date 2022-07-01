import numpy as np
from numba import njit
import matplotlib.pyplot as plt

"""
Dersom vi har en plate med et kvadrat med sidelengde a,
og en sirkel med radius a, og slipper baller ovenfra og ned med uniform
sannsynlighet for alle punkter på platen, vil forholdet mellom antall
baller som havner i sirkelen og antall baller som havner i kvadratet
konvergere mot pi når N går mot uendelig
"""

X = 4
Y = 3
a = 1
N = 30000

@njit
def square_and_circle_bowl():
    ball_count_circle = 0
    ball_count_square = 0
    for i in range(N):
        x = np.random.uniform(0, X)
        y = np.random.uniform(0, Y)
        if np.sqrt((x-2.5)**2 + (y-1.5)**2) <= a:
            ball_count_circle += 1
        if abs(x - 1.5) <= a/2 and abs(y - 1.5) <= a/2:
            ball_count_square += 1
    return ball_count_circle, ball_count_square

a, b = square_and_circle_bowl()
print(a, b)
ratio = a / b
print(ratio)

M = 20000
@njit
def hist():
    data = np.zeros(M)
    for i in range(M):
        a, b = square_and_circle_bowl()
        data[i] = a / b

    return data

hist_data = hist()

get_cmap = plt.get_cmap('jet')
n, bins, patches = plt.hist(hist_data, bins=100)
cmap = np.array(get_cmap(n / np.max(n)))

for color, p in zip(cmap, patches):
    plt.setp(p, 'facecolor', color)

plt.show()
