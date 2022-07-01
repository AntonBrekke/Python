import numpy as np
import matplotlib.pyplot as plt

def dirac_delta(x, a):
    if isinstance(a, (int, float)):
        a = a,
    s = np.zeros_like(x)
    epsilon = 1e-2
    print(a)
    for j in range(len(a)):
        d = x.copy()
        for i in range(len(d)):
            if x[i] <= a[j] + epsilon and x[i] >= a[j] - epsilon:
                d[i] = 1
            else:
                d[i] = 0
        s += d

    return s


x = np.linspace(-10, 10, 1000)
plt.plot(x, dirac_delta(x, [0.01]))
plt.show()
