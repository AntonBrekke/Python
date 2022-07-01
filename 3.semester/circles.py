import numpy as np
import matplotlib.pyplot as plt

N = 100

np.random.seed(114201514)
t = np.linspace(0, 2*np.pi, 6000)[None,:]
T0 = np.random.uniform(1, 10, N)[:,None]
r0 = np.random.uniform(1, 10, (N, 1))


def circles(t, T0, r0):
    return np.sum(r0*np.exp(2j*np.pi*t / T0), axis=0)

circ = circles(t, T0, r0)

print(np.shape(circ))
plt.plot(circ.real, circ.imag)
plt.show()
