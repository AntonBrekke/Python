import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

h = 4.135667696e-15         # eV/s
hbar = h / (2*np.pi)        # eV / s
c = sc.c
V0 = 10         # eV
L = 0.2e-9          # m
m = 511*1e3 / c**2      # eV / c^2

def T1(E):
    k_a = np.sqrt(2*m*(E - V0)) / hbar
    K = V0**2 / (4*E*(E - V0))
    return 1 / (1 + K*np.sin(k_a*L)**2)

def T2(E):
    k_b = np.sqrt(2*m*(V0 - E)) / hbar
    K = V0**2 / (4*E*(V0 - E))
    return 1 / (1 + K*np.sinh(k_b*L)**2)

def T3(V0):
    return 1 / (1 + m*L**2 / (2*hbar**2)*V0)

E1 = np.linspace(V0+1e-3, 10*V0, 1000)
E2 = np.linspace(0.1, V0-1e-3, 1000)
V = np.linspace(0, V0, 1000)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.plot(E1, T1(E1), color='r', label='T(E)')
ax1.set_title('E > V0', fontsize=16, weight='bold')
ax1.set_xlabel('E', fontsize=14, weight='bold')

ax2.plot(E2, T2(E2), color='royalblue', label='T(E)')
ax2.set_title('E < V0', fontsize=16, weight='bold')
ax2.set_xlabel('E', fontsize=14, weight='bold')

ax3.plot(V, T3(V), color='tab:orange', label='T(V0)')
ax3.set_title('E = V0', fontsize=16, weight='bold')
ax3.set_xlabel('V0', fontsize=14, weight='bold')

fig.tight_layout()
ax1.legend(prop={'size': 16})
ax2.legend(prop={'size': 16})
ax3.legend(prop={'size': 16})
plt.show()

# Plotter felles også
plt.plot(E2, T2(E2))
plt.plot(E1, T1(E1))
plt.show()
