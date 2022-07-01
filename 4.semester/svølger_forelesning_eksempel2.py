import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
b = 0.03

omega = np.sqrt(k/m)
gamma = b / (2*m)
omegap = np.sqrt(omega**2 - gamma**2)

N_per = 20
N = 1000
T = 2*np.pi / omega
t = np.linspace(0, N_per * T, N)

A = 1
phi = 0

x = A*np.exp(-gamma*t)*np.cos(omegap*t + phi)

Q = np.sqrt(k*m / b**2)
print(Q)

plt.plot(t, x, 'blue', linestyle='dashed')
plt.xlabel('t'); plt.ylabel('x')
plt.grid()
plt.show()
