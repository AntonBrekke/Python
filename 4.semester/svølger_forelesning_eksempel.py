import numpy as np
import matplotlib.pyplot as plt

# Definerer systemet
k = 1
m = 1
omega = np.sqrt(k/m)

# Definerer perioder
N_per = 5   # Antall perioder
T = 2*np.pi/omega   # Periode
N = 1000

t = np.linspace(0, N_per*T, N)

A1 = 1
phi1 = 0

A2 = 2
phi2 = 3*np.pi/4

x1 = A1*np.cos(omega*t + phi1)
x2 = A2*np.cos(omega*t + phi2)
x3 = x1 + x2

plt.plot(t, x1, 'royalblue', linestyle='dashed')
plt.plot(t, x2, 'r', linestyle='dashed')
plt.plot(t, x3, 'purple')
plt.xlabel('t')
plt.grid()
plt.show()
