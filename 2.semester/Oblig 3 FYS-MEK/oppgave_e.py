import numpy as np
import matplotlib.pyplot as plt

m = 5
k = 500
l0 = 0.5
h = 0.3

x = np.linspace(-0.75, 0.75, 101)
Fx = -k*x*(1 - l0/np.sqrt(x**2 + h**2))


plt.plot(x, Fx, label=r'$F_x$')
plt.xlabel('x [m]')
plt.ylabel(r'$F_x$ [N]')
plt.legend(loc='upper right')
# plt.savefig('oppgave_e')
plt.show()
