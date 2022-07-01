import numpy as np
import matplotlib.pyplot as plt

# alias-frekvens
def f_a(m, f_n, f):
    return abs(2*m*f_n - f)

lim = 4
m = np.linspace(0, lim, lim + 1)        # negative m gir ikke informasjon, m = 0 => f_a = f
f = 1800        # Hz, signalfrekvens
f_n = 500   # Hz, Nyquist-frekvens

# kun m s.a f_a < f gir alias

plt.plot(m, f_a(m, f_n, f), marker='o')
plt.plot(m, np.ones_like(m) * f)
plt.show()
